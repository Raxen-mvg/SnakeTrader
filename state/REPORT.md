# Paper trading report

Updated 2026-11-17 13:19 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,574 | +10.79% | 0 | - | 236 |
| benchmark | 221,427 | +10.71% | 0 | - | 237 |
| snake_abs_exit | 214,165 | +7.08% | 2 | 50% | 345 |
| intraweek | 213,907 | +6.95% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,582 | +6.29% | 2 | 50% | 345 |
| oracle | 212,006 | +6.00% | 0 | - | 233 |
| intramonth | 211,385 | +5.69% | 0 | - | 235 |
| snake_abs | 209,480 | +4.74% | 1 | 100% | 255 |
| snake_abs_conv | 209,340 | +4.67% | 1 | 100% | 255 |
| snake_viper_wild | 208,962 | +4.48% | 14 | 50% | 2,496 |
| random_hold | 207,416 | +3.71% | 10 | 70% | 733 |
| snake_viper_tick | 205,391 | +2.69% | 13 | 46% | 2,299 |
| snake_anaconda | 205,059 | +2.53% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,964 | +0.48% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,267 | -9.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,078 (-4.46%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +2,818 | +1.37% |
| snake_viper_tick | +2,771 | +1.37% |
| intraweek | +2,641 | +1.25% |
| benchmark | +1,346 | +0.61% |
| gold | +312 | +0.17% |
| unified | +137 | +0.06% |
| benchmark_smallcap | +135 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| oracle | -17 | -0.01% |
| snake_anaconda | -44 | -0.02% |
| intramonth | -234 | -0.11% |
| snake_abs_exit | -244 | -0.11% |
| random_hold | -377 | -0.18% |
| snake_abs_exit_conv | -636 | -0.30% |
| snake_abs_conv | -650 | -0.31% |
| snake_abs | -654 | -0.31% |

Average per day so far: unified Rs +616, benchmark Rs +612, snake_abs_exit Rs +443, intraweek Rs +397, snake_abs_exit_conv Rs +393, oracle Rs +343, snake_viper_wild Rs +332, intramonth Rs +325, snake_abs_conv Rs +292, snake_abs Rs +287, snake_viper_tick Rs +225, random_hold Rs +212, snake_anaconda Rs +169, nifty_calls Rs +52, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -535

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.