# Paper trading report

Updated 2026-11-17 09:36 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,698 | +11.35% | 0 | - | 236 |
| benchmark | 220,838 | +10.42% | 0 | - | 237 |
| snake_abs_exit | 214,294 | +7.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,272 | +6.64% | 2 | 50% | 345 |
| intramonth | 212,772 | +6.39% | 0 | - | 235 |
| intraweek | 212,529 | +6.26% | 35 | 54% | 3,851 |
| oracle | 212,319 | +6.16% | 0 | - | 233 |
| snake_abs | 210,137 | +5.07% | 1 | 100% | 255 |
| snake_abs_conv | 209,988 | +4.99% | 1 | 100% | 255 |
| random_hold | 207,855 | +3.93% | 10 | 70% | 733 |
| snake_viper_wild | 206,604 | +3.30% | 14 | 50% | 2,496 |
| snake_anaconda | 205,417 | +2.71% | 3 | 33% | 374 |
| snake_viper_tick | 203,071 | +1.54% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,827 | +0.91% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,201 | -9.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,503 (-4.25%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,264 | +0.60% |
| unified | +1,260 | +0.57% |
| intramonth | +1,154 | +0.55% |
| benchmark_smallcap | +998 | +0.50% |
| benchmark | +757 | +0.34% |
| snake_viper_wild | +459 | +0.22% |
| snake_viper_tick | +452 | +0.22% |
| snake_anaconda | +315 | +0.15% |
| oracle | +296 | +0.14% |
| gold | +247 | +0.14% |
| random_hold | +62 | +0.03% |
| snake_abs_exit_conv | +55 | +0.03% |
| snake_abs | +3 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1 | -0.00% |
| snake_abs_exit | -115 | -0.05% |

Average per day so far: unified Rs +649, benchmark Rs +595, snake_abs_exit Rs +447, snake_abs_exit_conv Rs +415, intramonth Rs +365, intraweek Rs +358, oracle Rs +352, snake_abs_conv Rs +312, snake_abs Rs +307, snake_viper_wild Rs +245, random_hold Rs +224, snake_anaconda Rs +181, snake_viper_tick Rs +128, benchmark_smallcap Rs +59, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -537

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.