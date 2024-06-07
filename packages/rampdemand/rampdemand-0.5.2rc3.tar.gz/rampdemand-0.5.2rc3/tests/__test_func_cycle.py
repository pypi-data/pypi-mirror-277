import os

import mock
import pytest

# from ramp.cli import parser as ramp_parser, main as ramp_main
from ramp import Appliance

# TODO implement output file folders before these tests can be run
# this is also linked to https://github.com/RAMP-project/RAMP/issues/58


def test_impossible_option_combinaison_start_date_year():
    app = Appliance(
        name="test_func_cycle", power=10, user=None, func_cycle=30, func_time=60
    )
    app.windows([1080, 1200], 0.0)

    # calc_coincident_switch_on
