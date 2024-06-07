#!/usr/bin/bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/create_wheel.sh
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

#set -xeuo pipefail
#set -xeu pipefail

security-check() {
    echo -n "Did you change the version in \`CHANGELOG.md\`, \`sphins-config\` and \`git tag v0.4.3\` and \`git push origin v0.4.3\`? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
}

compile-check() {
    echo -n "Compile local? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "ok, lets go ..."
    python3 setup.py bdist_wheel sdist
}

security-check
compile-check
