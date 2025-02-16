# -*- coding: utf-8 -*-
#
# environment.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com. 2024 Martin Chrastek, https://github.com/Martin005.
#
# This module is part of python-pptx-ng and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""
Used by behave to set testing environment before and after running acceptance
tests.
"""

import os

scratch_dir = os.path.abspath(os.path.join(os.path.split(__file__)[0], "_scratch"))


def before_all(context):
    if not os.path.isdir(scratch_dir):
        os.mkdir(scratch_dir)
