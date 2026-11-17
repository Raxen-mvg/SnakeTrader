# Paper trading report

Updated 2026-11-17 13:35 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,581 | +10.79% | 0 | - | 236 |
| benchmark | 221,466 | +10.73% | 0 | - | 237 |
| snake_abs_exit | 214,548 | +7.27% | 2 | 50% | 345 |
| intraweek | 213,411 | +6.71% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,935 | +6.47% | 2 | 50% | 345 |
| oracle | 212,191 | +6.10% | 0 | - | 233 |
| intramonth | 211,584 | +5.79% | 0 | - | 235 |
| snake_abs | 209,743 | +4.87% | 1 | 100% | 255 |
| snake_abs_conv | 209,605 | +4.80% | 1 | 100% | 255 |
| snake_viper_wild | 209,270 | +4.63% | 14 | 50% | 2,496 |
| random_hold | 207,417 | +3.71% | 10 | 70% | 733 |
| snake_viper_tick | 205,693 | +2.85% | 13 | 46% | 2,299 |
| snake_anaconda | 205,408 | +2.70% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,020 | +0.51% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,152 | -9.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,092 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,125 | +1.52% |
| snake_viper_tick | +3,073 | +1.52% |
| intraweek | +2,145 | +1.01% |
| benchmark | +1,385 | +0.63% |
| snake_anaconda | +306 | +0.15% |
| gold | +197 | +0.11% |
| benchmark_smallcap | +191 | +0.10% |
| oracle | +168 | +0.08% |
| unified | +144 | +0.07% |
| snake_abs_exit | +139 | +0.07% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -35 | -0.02% |
| snake_abs_exit_conv | -282 | -0.13% |
| random_hold | -376 | -0.18% |
| snake_abs_conv | -384 | -0.18% |
| snake_abs | -391 | -0.19% |

Average per day so far: unified Rs +617, benchmark Rs +613, snake_abs_exit Rs +455, snake_abs_exit_conv Rs +404, intraweek Rs +383, oracle Rs +348, snake_viper_wild Rs +343, intramonth Rs +331, snake_abs_conv Rs +300, snake_abs Rs +295, snake_viper_tick Rs +237, random_hold Rs +212, snake_anaconda Rs +180, nifty_calls Rs +52, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -539

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.