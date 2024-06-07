[![](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/lucit-backtesting/master/images/logo/lucit-backtesting.png)](https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/)

lucit-backtesting - 'backtesting.py' maintained by LUCIT
========================================================

[![GitHub Sponsors](https://img.shields.io/github/sponsors/kernc?color=pink)](https://github.com/sponsors/kernc)

Backtest trading strategies with Python.

Kudos to ***Zach Lûster*** for the original project [`kernc/backtesting.py`](https://github.com/kernc/backtesting.py) 
which he built and maintained for 5 years. 

We at [LUCIT](https://www.lucit.tech) like to use `backtesting.py` with our customers in smaller projects. 
Unfortunately the project is missing important updates and therefore we decided to fork the project and release new 
stable versions. 

We are happy to maintain the forked repository and take care of code reviews, pull requests and releases and hope for 
good support from the community!

Installation
------------

    $ pip install lucit-backtesting


Usage
-----
```
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
```

Results in:

```
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       94.27
Equity Final [$]                     68935.12
Equity Peak [$]                      68991.22
Return [%]                             589.35
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       25.42
Volatility (Ann.) [%]                   38.43
Sharpe Ratio                             0.66
Sortino Ratio                            1.30
Calmar Ratio                             0.77
Max. Drawdown [%]                      -33.08
Avg. Drawdown [%]                       -5.58
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   93
Win Rate [%]                            53.76
Best Trade [%]                          57.12
Worst Trade [%]                        -16.63
Avg. Trade [%]                           1.96
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          32 days 00:00:00
Profit Factor                            2.13
Expectancy [%]                           6.91
SQN                                      1.78
Kelly Criterion                        0.6134
_strategy              SmaCross(n1=10, n2=20)
_equity_curve                          Equ...
_trades                       Size  EntryB...
dtype: object
```

Features
--------
* Simple, well-documented API
* Blazing fast execution
* Built-in optimizer
* Library of composable base strategies and utilities
* Indicator-library-agnostic
* Supports _any_ financial instrument with candlestick data
* Detailed results
* Interactive visualizations

![xkcd.com/1570](https://imgs.xkcd.com/comics/engineer_syllogism.png)


Bugs
----
Before [reporting bugs](https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/issues) or posting to the
[discussion board](https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/discussions),
please read [contributing guidelines](CONTRIBUTING.md), particularly the section
about crafting useful bug reports and ```` ``` ````-fencing your code. We thank you!

