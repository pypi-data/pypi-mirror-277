import logging
import time
from enum import Enum
from threading import Event
from typing import Optional

import numpy
from epics import caget, camonitor, caput
from numpy.typing import ArrayLike
from p4p.client.thread import Context

import b22ao.pvs as pvs

logger = logging.getLogger("b22ao.aosystem")


class AOSystem:
    def __init__(self):
        self.cam = AreaDetector(pvs.AD_PVBASE)
        self.dm = None  # DM of choice

    def select_dm(self, dm):
        logger.info(f"DM {dm} selected")
        self.dm = DeformableMirror(dm)

    def deform(self, mask: ArrayLike, dm: Optional[int] = None):
        try:
            DeformableMirror(dm).deform(mask)
        except ValueError:  # no dm provided
            try:
                self.dm.deform(mask)
            except AttributeError:
                raise NameError(
                    "Call #select_dm(dm) first or specify a DM in #deform(mask, dm)"
                )

    def capture(self):
        return self.cam.acquire()

    def get_metadata(self):
        return {"cam": self.cam.get_metadata(), "dm": self.dm.get_metadata()}


class DeformableMirror(Enum):

    DM1 = 1
    DM2 = 2

    def deform(self, mask: ArrayLike):
        logger.debug("Deforming mirror")
        for actuator in range(len(mask)):
            act_sp_pv = self._get_actuator_sp_pv(actuator)
            caput(act_sp_pv, mask[actuator])
        caput(self._get_pv_base() + pvs.DM_APPLY_MASK, 1)

    def _get_pv_base(self):
        if self is DeformableMirror.DM1:
            return standardise_pv(pvs.DM1_PVBASE)
        elif self is DeformableMirror.DM2:
            return standardise_pv(pvs.DM2_PVBASE)

    def _get_actuator_sp_pv(self, actuator: int):
        """Individual actuator setpoing PV should be: BASE:ACT{num}:SP"""
        return f"{self._get_pv_base()}ACT{actuator}{pvs.DM_ACTUATOR_SETPOINT}"

    def get_metadata(self):
        return {"mirror": self.value}


class AreaDetector:
    def __init__(self, pv_base: str):
        pv_base = standardise_pv(pv_base)
        self.acquisition_allowed = Event()
        self.acquisition_complete = Event()
        self.data_ready = Event()
        self.error_state = False
        self.current_frame = None
        self.frame_counter_pv = pv_base + pvs.AD_ARRAY_COUNTER
        self.acquire_pv = pv_base + pvs.AD_ACQUIRE
        self.data_pv = pv_base + pvs.AD_ARRAY_DATA
        self.size_x_pv = pv_base + pvs.AD_ARRAY_SIZE_X
        self.size_y_pv = pv_base + pvs.AD_ARRAY_SIZE_Y
        self.gain_pv = pv_base + pvs.AD_GAIN
        self.shutter_pv = pv_base + pvs.AD_SHUTTER_STATE
        self.state_pv = pv_base + pvs.AD_STATE

        caput(pv_base + pvs.AD_IMAGE_MODE, pvs.AD_IMAGE_MODE_SINGLE)

        camonitor(self.state_pv, callback=self.state_callback)
        camonitor(self.frame_counter_pv, callback=self.frame_counter_callback)
        camonitor(pvs.ALLOW_ACQUISITION, callback=self.allow_acquisition_callback)

        # synchronise acquisition_allowed event with current PV value
        self.allow_acquisition_callback(value=caget(pvs.ALLOW_ACQUISITION))

        self.pva_ctxt = Context("pva")

    def acquire(self):
        """
        Returns a valid frame
        (acquires and reads shutter state:
        repeats until shutter is open)
        """
        # request frames until shutter is open
        while True:
            self.acquisition_allowed.wait()
            self.request_frame()
            if caget(self.shutter_pv, as_string=True) == "Open":
                break
            logger.debug("Frame received, but shutter closed. Reacquiring...")

        # shutter is open; read data
        flat_data = caget(self.data_pv)
        data = numpy.reshape(
            flat_data.data, [caget(self.size_x_pv), caget(self.size_y_pv)]
        )
        logger.debug("Acquisition successful")
        return data

    def request_frame(
        self, attempt: int = 0, max_attempts: int = 5, time_before_retry: int = 5
    ):
        """
        Hits the 'Acquire' button and blocks
        until data is ready to be read from Array plugin
        """
        self.current_frame = caget(self.frame_counter_pv)
        logger.debug("Acquiring")
        caput(self.acquire_pv, "Acquire")
        self.acquisition_complete.wait()

        if self.error_state:

            if attempt >= max_attempts:
                raise Exception("Max retries reached - giving up")

            logger.error(
                f"IOC in Error state. Retrying acquisition in {time_before_retry} seconds"
            )
            caput(self.acquire_pv, "Done")  # i.e. smash the stop button
            time.sleep(time_before_retry)
            self.request_frame(attempt=attempt + 1)
            # and critically, return
            return

        # Hooray: Acquisition done and detector not in error state.
        logger.debug("Waiting for frame to appear in Area Detector")
        self.data_ready.wait()
        self.data_ready.clear()

    def state_callback(self, **kwargs):
        state = kwargs["value"]
        if state == 1:  # Acquire
            self.acquisition_complete.clear()
        elif state == 0:  # Idle
            self.error_state = False
            self.acquisition_complete.set()
        elif state == 6:  # Error
            self.error_state = True
            self.acquisition_complete.set()

    def frame_counter_callback(self):
        """
        The IOC has a quirk where unique IDs are reset to 0 after an error.
        For this reason, we do not compare the value passed to this callback function,
        but simply assume that once this is called, data is ready to be read.
        """
        self.data_ready.set()

    def allow_acquisition_callback(self, **kwargs):
        value = kwargs["value"]
        if value == 0:
            logger.info("Acquisition disallowed")
            self.acquisition_allowed.clear()
        elif value == 1:
            logger.info("Acquisition allowed")
            self.acquisition_allowed.set()

    def get_metadata(self):
        metadata = dict()
        metadata["gain"] = caget(self.gain_pv)
        return metadata


def standardise_pv(pv: str):
    return pv if pv.endswith(":") else pv + ":"
