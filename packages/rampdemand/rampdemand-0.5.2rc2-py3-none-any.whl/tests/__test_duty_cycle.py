import os
import pytest
import numpy as np

from ramp.ramp_run import run_usecase

TEST_PATH = os.path.dirname(os.path.abspath(__file__))


def test_minimal_time_appliance_is_switched_on_respected():
    profile = run_usecase(
        fname=os.path.join(TEST_PATH, "test_inputs", "func_cycle.xlsx"),
        num_profiles=1,
        postprocess=False,
    )
    profile = profile[0]
    switch_on_intervals = np.abs(np.diff(profile))

    # get the indices of the steps (first one is trivial).
    icsplus = np.where(switch_on_intervals > 0)
    icsminus = np.where(switch_on_intervals < 0)

    # get the first dimension and shift by one as you want
    # the index of the element right of the step

    ics_shiftplus = np.concatenate(([-1], icsplus[0])) + 1
    ics_shiftminus = np.concatenate((icsminus[0], [len(profile) - 1])) + 1

    # and if you need a list
    ics_list = ics_shiftplus  # .tolist()
    print(ics_shiftplus)
    print(ics_shiftminus)
    print(profile[: ics_shiftplus[3]])
    for i in range(len(ics_shiftplus) - 1):
        print(profile[ics_shiftplus[i] : ics_shiftplus[i + 1]] > 0)
        if (profile[ics_shiftplus[i] : ics_shiftplus[i + 1]] > 0).all():
            if ics_shiftplus[i + 1] - ics_shiftplus[i] < 30:
                if (profile[ics_shiftplus[i - 1] : ics_shiftplus[i]] == 0).all():
                    print(ics_shiftplus[i], ics_shiftplus[i + 1])
                    pytest.fail()

    switch_on_length = ics_shiftminus - ics_shiftplus
    print(np.where(switch_on_length < 3)[0].any())

    # print(ics_list)
    # #.tolist()
    # print(ics_shiftminus)
    # print(profile[:ics_shiftplus[2]])
    # for s, e in zip(icsplus[0] + 1, icsminus[0]+1):
    #     print(s,e)
    #     print(profile[s:e])

    # pytest.fail()
