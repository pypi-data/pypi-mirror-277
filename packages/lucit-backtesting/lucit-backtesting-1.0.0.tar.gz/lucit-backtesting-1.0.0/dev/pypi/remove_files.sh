#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/remove_files.sh
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

set -xeuo pipefail

rm ./build -r
rm ./dist -r
rm ./lucit_backtesting.egg-info -r

rm lucit_backtesting/*.so
rm lucit_backtesting/*.c
