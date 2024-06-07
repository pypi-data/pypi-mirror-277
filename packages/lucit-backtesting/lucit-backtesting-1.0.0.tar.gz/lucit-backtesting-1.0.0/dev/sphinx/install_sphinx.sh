#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: sphinx/install_sphinx.sh
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://www.lucit.tech/lucit-backtesting.html
# Github: https://github.com/LUCIT-Systems-and-Development/lucit-backtesting
# Documentation: https://lucit-backtesting.docs.lucit.tech
# PyPI: https://pypi.org/project/lucit-backtesting
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.
set -xeuo pipefail
python3 -m pip install sphinx --upgrade
python3 -m pip install python-docs-theme-lucit --upgrade
python3 -m pip install rich --upgrade
python3 -m pip install myst-parser --upgrade
python3 -m pip install sphinx-markdown-tables --upgrade