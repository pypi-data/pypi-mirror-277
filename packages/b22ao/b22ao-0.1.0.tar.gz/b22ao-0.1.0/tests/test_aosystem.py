from unittest.mock import ANY, MagicMock, call, patch

import numpy as np
import pytest

from b22ao.aosystem import AOSystem, DeformableMirror


@patch("b22ao.aosystem.caput")
@patch("b22ao.aosystem.camonitor")
@patch("b22ao.aosystem.AreaDetector")
def test_AOSystem_raises_error_if_no_dm_provided(
    mock_areadetector: MagicMock,
    fake_camonitor: MagicMock,
    fake_caput: MagicMock,
):
    with pytest.raises(NameError):
        AOSystem().deform([], None)


@patch("b22ao.aosystem.AreaDetector")
def test_AOSystem_select_dm(mock_areadetector: MagicMock):
    test_aosystem = AOSystem()
    test_aosystem.select_dm(1)

    assert test_aosystem.dm == DeformableMirror.DM1


def test_pv_names_from_deformable_mirror():
    dm1 = DeformableMirror(1)

    assert dm1._get_pv_base() == "BL22B-OP-ALPAO-01:"

    dm2 = DeformableMirror(2)

    assert dm2._get_actuator_sp_pv(90) == "BL22B-OP-ALPAO-02:ACT90:SP"


def test_get_metadata_out_of_dm():
    dm1 = DeformableMirror(1)

    assert dm1.get_metadata() == {"mirror": 1}


@patch("b22ao.aosystem.caput")
def test_dm_deform_calls(fake_caput: MagicMock):
    dm2 = DeformableMirror(2)
    fake_mask = np.array([[0], [1]])

    dm2.deform(fake_mask)

    assert fake_caput.call_count == 3
    calls = [call(ANY, fake_mask[0]), call(ANY, fake_mask[1]), call(ANY, 1)]
    fake_caput.assert_has_calls(calls)
