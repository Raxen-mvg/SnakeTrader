# Paper trading report

Updated 2026-11-17 10:15 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,715 | +11.36% | 0 | - | 236 |
| benchmark | 221,336 | +10.67% | 0 | - | 237 |
| snake_abs_exit | 215,904 | +7.95% | 2 | 50% | 345 |
| snake_abs_exit_conv | 214,471 | +7.24% | 2 | 50% | 345 |
| intraweek | 213,178 | +6.59% | 35 | 54% | 3,851 |
| oracle | 212,889 | +6.45% | 0 | - | 233 |
| intramonth | 212,714 | +6.36% | 0 | - | 235 |
| snake_abs | 210,710 | +5.36% | 1 | 100% | 255 |
| snake_abs_conv | 210,564 | +5.28% | 1 | 100% | 255 |
| random_hold | 208,097 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,240 | +3.62% | 14 | 50% | 2,496 |
| snake_anaconda | 206,063 | +3.03% | 3 | 33% | 374 |
| snake_viper_tick | 203,697 | +1.85% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,017 | +1.01% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,757 (-4.12%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,912 | +0.91% |
| snake_abs_exit | +1,494 | +0.70% |
| unified | +1,277 | +0.58% |
| benchmark | +1,255 | +0.57% |
| snake_abs_exit_conv | +1,254 | +0.59% |
| benchmark_smallcap | +1,188 | +0.59% |
| snake_viper_wild | +1,096 | +0.53% |
| intramonth | +1,095 | +0.52% |
| snake_viper_tick | +1,078 | +0.53% |
| snake_anaconda | +961 | +0.47% |
| oracle | +866 | +0.41% |
| snake_abs | +576 | +0.27% |
| snake_abs_conv | +575 | +0.27% |
| gold | +378 | +0.21% |
| random_hold | +304 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +649, benchmark Rs +610, snake_abs_exit Rs +497, snake_abs_exit_conv Rs +452, intraweek Rs +377, oracle Rs +368, intramonth Rs +363, snake_abs_conv Rs +330, snake_abs Rs +325, snake_viper_wild Rs +268, random_hold Rs +231, snake_anaconda Rs +202, snake_viper_tick Rs +154, benchmark_smallcap Rs +65, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.