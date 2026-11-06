# Paper trading report

Updated 2026-11-06 13:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,904 | +7.95% | 0 | - | 237 |
| unified | 214,704 | +7.35% | 0 | - | 236 |
| snake_abs_exit_conv | 208,340 | +4.17% | 1 | 100% | 255 |
| snake_abs_exit | 208,237 | +4.12% | 1 | 100% | 260 |
| intraweek | 208,163 | +4.08% | 25 | 48% | 2,757 |
| intramonth | 207,031 | +3.52% | 0 | - | 235 |
| snake_abs | 205,338 | +2.67% | 1 | 100% | 255 |
| oracle | 205,324 | +2.66% | 0 | - | 233 |
| snake_abs_conv | 205,145 | +2.57% | 1 | 100% | 255 |
| random_hold | 203,307 | +1.65% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,164 | -1.92% | 3 | 33% | 702 |
| snake_anaconda | 195,591 | -2.21% | 3 | 33% | 374 |
| benchmark_smallcap | 195,157 | -2.42% | 0 | - | 237 |
| snake_viper_tick | 192,837 | -3.58% | 2 | 0% | 532 |
| gold | 190,358 | -4.82% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,801 (-6.60%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,134 | +1.00% |
| oracle | +1,252 | +0.61% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -918 | -0.44% |
| random_hold | -1,016 | -0.50% |
| intraweek | -1,255 | -0.60% |
| unified | -1,279 | -0.59% |
| benchmark_smallcap | -3,531 | -1.78% |
| gold | -3,863 | -1.99% |
| snake_abs | -6,351 | -3.00% |
| snake_abs_conv | -6,400 | -3.02% |
| snake_abs_exit | -6,422 | -2.99% |
| snake_abs_exit_conv | -6,464 | -3.01% |
| snake_anaconda | -6,888 | -3.40% |
| snake_viper_tick | -8,301 | -4.13% |
| snake_viper_wild | -8,492 | -4.15% |

Average per day so far: benchmark Rs +548, unified Rs +507, snake_abs_exit_conv Rs +321, snake_abs_exit Rs +317, intraweek Rs +281, intramonth Rs +242, snake_abs_conv Rs +198, snake_abs Rs +198, oracle Rs +184, random_hold Rs +114, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -183, snake_anaconda Rs -184, benchmark_smallcap Rs -194, gold Rs -332, snake_viper_tick Rs -398, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.