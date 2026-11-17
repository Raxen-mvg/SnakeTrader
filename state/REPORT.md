# Paper trading report

Updated 2026-11-17 12:13 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,368 | +11.18% | 0 | - | 237 |
| unified | 222,027 | +11.01% | 0 | - | 236 |
| snake_abs_exit | 214,798 | +7.40% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,041 | +6.52% | 2 | 50% | 345 |
| intraweek | 212,301 | +6.15% | 35 | 54% | 3,851 |
| oracle | 212,189 | +6.09% | 0 | - | 233 |
| intramonth | 211,928 | +5.96% | 0 | - | 235 |
| snake_abs | 209,742 | +4.87% | 1 | 100% | 255 |
| snake_abs_conv | 209,593 | +4.80% | 1 | 100% | 255 |
| random_hold | 207,709 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,213 | +3.61% | 14 | 50% | 2,496 |
| snake_anaconda | 205,243 | +2.62% | 3 | 33% | 374 |
| snake_viper_tick | 203,670 | +1.83% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,141 | +1.07% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,267 | -9.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,135 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,287 | +1.04% |
| benchmark_smallcap | +1,312 | +0.65% |
| snake_viper_wild | +1,069 | +0.52% |
| snake_viper_tick | +1,050 | +0.52% |
| intraweek | +1,036 | +0.49% |
| unified | +589 | +0.27% |
| snake_abs_exit | +388 | +0.18% |
| gold | +312 | +0.17% |
| intramonth | +309 | +0.15% |
| oracle | +166 | +0.08% |
| snake_anaconda | +140 | +0.07% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -84 | -0.04% |
| snake_abs_exit_conv | -176 | -0.08% |
| snake_abs | -391 | -0.19% |
| snake_abs_conv | -397 | -0.19% |

Average per day so far: benchmark Rs +639, unified Rs +629, snake_abs_exit Rs +462, snake_abs_exit_conv Rs +408, intraweek Rs +351, oracle Rs +348, intramonth Rs +341, snake_abs_conv Rs +300, snake_abs Rs +295, snake_viper_wild Rs +267, random_hold Rs +220, snake_anaconda Rs +175, snake_viper_tick Rs +153, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -535

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.