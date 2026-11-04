# Paper trading report

Updated 2026-11-04 11:46 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,088 | +6.54% | 0 | - | 236 |
| intraweek | 208,961 | +4.48% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,821 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,701 | +4.35% | 1 | 100% | 260 |
| benchmark | 207,390 | +3.69% | 0 | - | 237 |
| snake_viper_wild | 206,823 | +3.41% | 3 | 33% | 702 |
| snake_abs | 205,727 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,578 | +2.79% | 1 | 100% | 255 |
| intramonth | 205,511 | +2.75% | 0 | - | 235 |
| snake_viper_tick | 203,221 | +1.61% | 2 | 0% | 532 |
| random_hold | 202,811 | +1.41% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,842 | +0.42% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,689 | -1.16% | 3 | 33% | 361 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| gold | 190,309 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,887 (-5.56%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,031 | +2.71% |
| snake_abs_exit | +4,687 | +2.30% |
| snake_abs_exit_conv | +4,483 | +2.19% |
| snake_abs_conv | +4,437 | +2.21% |
| snake_abs | +4,418 | +2.19% |
| intraweek | +3,875 | +1.89% |
| snake_anaconda | +3,865 | +1.99% |
| random_hold | +2,343 | +1.17% |
| benchmark_smallcap | +1,850 | +0.96% |
| intramonth | +1,540 | +0.76% |
| unified | +1,087 | +0.51% |
| oracle | +853 | +0.43% |
| benchmark | +688 | +0.33% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,946 | -1.91% |
| snake_viper_wild | -4,069 | -1.93% |

Average per day so far: unified Rs +485, snake_abs_exit_conv Rs +368, snake_abs_exit Rs +363, snake_viper_wild Rs +359, intraweek Rs +332, benchmark Rs +274, snake_abs_conv Rs +232, snake_abs Rs +229, intramonth Rs +204, snake_viper_tick Rs +201, random_hold Rs +104, nifty_calls Rs +68, oracle Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -105, benchmark_smallcap Rs -227, gold Rs -359, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.