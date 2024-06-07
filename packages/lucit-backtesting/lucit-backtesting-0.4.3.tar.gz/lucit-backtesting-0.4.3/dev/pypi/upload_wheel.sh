#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/upload_wheel.sh
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.
# ~/.pypirc

set -xeuo pipefail

python3 -m twine upload dist/*
