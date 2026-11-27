# Paper trading report

Updated 2026-11-27 12:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,403 | +12.20% | 0 | - | 237 |
| unified | 223,403 | +11.70% | 0 | - | 236 |
| oracle | 211,932 | +5.97% | 0 | - | 233 |
| intramonth | 211,097 | +5.55% | 0 | - | 235 |
| random_hold | 210,203 | +5.10% | 13 | 69% | 1,037 |
| intraweek | 208,043 | +4.02% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,096 | +2.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,924 | +1.96% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,714 | +0.36% | 1 | 100% | 255 |
| snake_abs_conv | 200,538 | +0.27% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,056 | -2.97% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,815 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,018 | +2.00% |
| snake_abs_exit_conv | +3,527 | +1.76% |
| gold | +3,239 | +1.95% |
| snake_abs_conv | +2,171 | +1.09% |
| snake_abs | +2,162 | +1.09% |
| snake_anaconda | +1,760 | +0.92% |
| random_hold | +1,609 | +0.77% |
| intraweek | +994 | +0.48% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +564 | +0.27% |
| unified | +325 | +0.15% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -304 | -0.14% |
| benchmark | -1,584 | -0.70% |

Average per day so far: benchmark Rs +581, unified Rs +557, oracle Rs +284, intramonth Rs +264, random_hold Rs +243, intraweek Rs +191, snake_abs_exit Rs +131, snake_abs_exit_conv Rs +101, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +18, snake_abs_conv Rs +14, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -161, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.