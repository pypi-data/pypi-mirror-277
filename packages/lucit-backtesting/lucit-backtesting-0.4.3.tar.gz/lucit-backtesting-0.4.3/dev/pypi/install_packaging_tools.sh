#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/install_packaging_tools.sh
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

set -xeuo pipefail

python3 -m pip install --user --upgrade pip setuptools wheel twine tqdm
