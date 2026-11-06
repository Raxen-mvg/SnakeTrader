# Paper trading report

Updated 2026-11-06 15:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,541 | +8.77% | 0 | - | 237 |
| unified | 215,614 | +7.81% | 0 | - | 236 |
| intraweek | 209,304 | +4.65% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,586 | +4.29% | 1 | 100% | 255 |
| snake_abs_exit | 208,473 | +4.24% | 1 | 100% | 260 |
| intramonth | 207,616 | +3.81% | 0 | - | 235 |
| oracle | 205,903 | +2.95% | 0 | - | 233 |
| snake_abs | 205,577 | +2.79% | 1 | 100% | 255 |
| snake_abs_conv | 205,388 | +2.69% | 1 | 100% | 255 |
| random_hold | 203,521 | +1.76% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,749 | -1.63% | 0 | - | 237 |
| snake_viper_wild | 196,015 | -1.99% | 4 | 25% | 842 |
| snake_anaconda | 195,911 | -2.04% | 3 | 33% | 374 |
| snake_viper_tick | 192,687 | -3.66% | 3 | 0% | 672 |
| gold | 190,917 | -4.54% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,281 (-6.36%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,771 | +1.76% |
| oracle | +1,831 | +0.90% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -115 | -0.06% |
| intramonth | -332 | -0.16% |
| unified | -369 | -0.17% |
| random_hold | -803 | -0.39% |
| benchmark_smallcap | -1,939 | -0.98% |
| gold | -3,304 | -1.70% |
| snake_abs | -6,111 | -2.89% |
| snake_abs_conv | -6,157 | -2.91% |
| snake_abs_exit | -6,185 | -2.88% |
| snake_abs_exit_conv | -6,218 | -2.90% |
| snake_anaconda | -6,568 | -3.24% |
| snake_viper_tick | -8,451 | -4.20% |
| snake_viper_wild | -8,641 | -4.22% |

Average per day so far: benchmark Rs +605, unified Rs +538, snake_abs_exit_conv Rs +330, snake_abs_exit Rs +326, intraweek Rs +321, intramonth Rs +263, snake_abs_conv Rs +207, snake_abs Rs +207, oracle Rs +204, random_hold Rs +121, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -130, snake_anaconda Rs -170, snake_viper_wild Rs -190, gold Rs -313, snake_viper_tick Rs -406, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.