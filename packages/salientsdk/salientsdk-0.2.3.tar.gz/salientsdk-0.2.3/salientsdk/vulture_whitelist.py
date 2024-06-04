#!/usr/bin/env python
# Copyright Salient Predictions 2024

"""Whitelist file for vulture.

We use the vulture tool to make sure that we don't have dead code
hanging around. Sometimes vulture falsely flags a function as unused.
In that case, we add the function to this whitelist file so they are
explicitly registered as used.
"""

from .hydro import calc_swe
from .upload_file_api import user_files
from .wind import calc_wind_power_all

calc_swe  # unused function (salientsdk/hydro.py:11)
user_files  # unused function (salientsdk/upload_file_api.py:220)
calc_wind_power_all  # unused function (salientsdk/wind.py:22)
