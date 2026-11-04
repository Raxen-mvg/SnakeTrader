# Paper trading report

Updated 2026-11-04 12:01 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,547 | +6.77% | 0 | - | 236 |
| snake_abs_exit_conv | 209,371 | +4.69% | 1 | 100% | 255 |
| snake_abs_exit | 209,252 | +4.63% | 1 | 100% | 260 |
| intraweek | 208,306 | +4.15% | 25 | 48% | 2,757 |
| benchmark | 207,183 | +3.59% | 0 | - | 237 |
| snake_viper_wild | 206,803 | +3.40% | 3 | 33% | 702 |
| snake_abs | 206,282 | +3.14% | 1 | 100% | 255 |
| snake_abs_conv | 206,131 | +3.06% | 1 | 100% | 255 |
| intramonth | 205,768 | +2.88% | 0 | - | 235 |
| snake_viper_tick | 203,200 | +1.60% | 2 | 0% | 532 |
| random_hold | 202,476 | +1.24% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,868 | +0.43% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,272 | -0.86% | 3 | 33% | 361 |
| benchmark_smallcap | 194,720 | -2.64% | 0 | - | 237 |
| gold | 190,687 | -4.66% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,918 (-5.54%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,409 | +2.92% |
| snake_abs_exit | +5,238 | +2.57% |
| snake_abs_exit_conv | +5,033 | +2.46% |
| snake_abs_conv | +4,990 | +2.48% |
| snake_abs | +4,973 | +2.47% |
| snake_anaconda | +4,448 | +2.29% |
| intraweek | +3,221 | +1.57% |
| random_hold | +2,007 | +1.00% |
| intramonth | +1,797 | +0.88% |
| benchmark_smallcap | +1,782 | +0.92% |
| unified | +1,546 | +0.73% |
| oracle | +879 | +0.44% |
| benchmark | +482 | +0.23% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,967 | -1.92% |
| snake_viper_wild | -4,090 | -1.94% |

Average per day so far: unified Rs +502, snake_abs_exit_conv Rs +390, snake_abs_exit Rs +386, snake_viper_wild Rs +358, intraweek Rs +308, benchmark Rs +266, snake_abs_conv Rs +255, snake_abs Rs +251, intramonth Rs +214, snake_viper_tick Rs +200, random_hold Rs +92, nifty_calls Rs +68, oracle Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -79, benchmark_smallcap Rs -230, gold Rs -345, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.