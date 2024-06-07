#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: sphinx/create_docs.sh
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

# set -xeuo pipefail

rm dev/sphinx/source/changelog.md
rm dev/sphinx/source/code_of_conduct.md
rm dev/sphinx/source/contributing.md
rm dev/sphinx/source/license.md
rm dev/sphinx/source/readme.md
rm dev/sphinx/source/security.md

cp CHANGELOG.md dev/sphinx/source/changelog.md
cp CODE_OF_CONDUCT.md dev/sphinx/source/code_of_conduct.md
cp CONTRIBUTING.md dev/sphinx/source/contributing.md
cp LICENSE.md dev/sphinx/source/license.md
cp README.md dev/sphinx/source/readme.md
cp SECURITY.md dev/sphinx/source/security.md

mkdir -vp dev/sphinx/build

cd dev/sphinx
rm build/html
ln -s ../../../docs build/html
make html -d
echo "Creating CNAME file for GitHub."
echo "lucit-backtesting.docs.lucit.tech" >> build/html/CNAME
