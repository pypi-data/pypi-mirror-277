#!/usr/bin/bash

rm *.log
rm dev/*.log

rm .eggs -r
rm build -r
rm dist -r
rm *.egg-info -r
rm stubs -r
rm out -r

rm backtesting/*.c
rm backtesting/*.html
rm backtesting/*.dll
rm backtesting/*.so
rm backtesting/*.pyi
