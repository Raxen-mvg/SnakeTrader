# Paper trading report

Updated 2026-11-25 14:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,816 | +12.41% | 0 | - | 237 |
| unified | 224,503 | +12.25% | 0 | - | 236 |
| oracle | 212,615 | +6.31% | 0 | - | 233 |
| intramonth | 212,044 | +6.02% | 0 | - | 235 |
| random_hold | 209,450 | +4.72% | 12 | 75% | 1,009 |
| intraweek | 206,876 | +3.44% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,329 | +0.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,116 | +0.56% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,714 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,515 | -0.24% | 1 | 100% | 255 |
| benchmark_smallcap | 198,654 | -0.67% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,181 | -3.41% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,155 | -17.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,841 (-5.58%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,343 | +1.51% |
| random_hold | +1,024 | +0.49% |
| oracle | +273 | +0.13% |
| unified | +218 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -325 | -0.16% |
| intramonth | -707 | -0.33% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| gold | -4,274 | -2.52% |
| intraweek | -4,743 | -2.24% |
| snake_anaconda | -5,522 | -2.78% |
| snake_abs | -5,747 | -2.80% |
| snake_abs_conv | -5,788 | -2.82% |
| snake_abs_exit_conv | -5,929 | -2.86% |
| snake_abs_exit | -6,166 | -2.97% |

Average per day so far: benchmark Rs +620, unified Rs +613, oracle Rs +315, intramonth Rs +301, random_hold Rs +236, intraweek Rs +172, nifty_calls Rs +46, snake_abs_exit Rs +36, snake_abs_exit_conv Rs +30, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, benchmark_smallcap Rs -37, snake_viper_wild Rs -88, snake_anaconda Rs -195, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -871

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.