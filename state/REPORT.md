# Paper trading report

Updated 2026-11-17 09:32 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,192 | +11.60% | 0 | - | 236 |
| benchmark | 220,953 | +10.48% | 0 | - | 237 |
| snake_abs_exit | 214,633 | +7.32% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,746 | +6.87% | 2 | 50% | 345 |
| intramonth | 213,283 | +6.64% | 0 | - | 235 |
| intraweek | 213,048 | +6.52% | 35 | 54% | 3,851 |
| oracle | 212,753 | +6.38% | 0 | - | 233 |
| snake_abs | 210,433 | +5.22% | 1 | 100% | 255 |
| snake_abs_conv | 210,288 | +5.14% | 1 | 100% | 255 |
| random_hold | 208,240 | +4.12% | 10 | 70% | 733 |
| snake_viper_wild | 206,768 | +3.38% | 14 | 50% | 2,496 |
| snake_anaconda | 205,692 | +2.85% | 3 | 33% | 374 |
| snake_viper_tick | 203,233 | +1.62% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,331 | +1.17% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,184 | -9.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,927 (-4.04%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,782 | +0.84% |
| unified | +1,754 | +0.79% |
| intramonth | +1,664 | +0.79% |
| benchmark_smallcap | +1,502 | +0.75% |
| benchmark | +872 | +0.40% |
| oracle | +730 | +0.34% |
| snake_viper_wild | +623 | +0.30% |
| snake_viper_tick | +613 | +0.30% |
| snake_anaconda | +589 | +0.29% |
| snake_abs_exit_conv | +529 | +0.25% |
| random_hold | +447 | +0.21% |
| snake_abs | +299 | +0.14% |
| snake_abs_conv | +298 | +0.14% |
| gold | +230 | +0.13% |
| snake_abs_exit | +224 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +663, benchmark Rs +599, snake_abs_exit Rs +457, snake_abs_exit_conv Rs +430, intramonth Rs +380, intraweek Rs +373, oracle Rs +364, snake_abs_conv Rs +321, snake_abs Rs +316, snake_viper_wild Rs +251, random_hold Rs +235, snake_anaconda Rs +190, snake_viper_tick Rs +135, benchmark_smallcap Rs +75, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -538

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.