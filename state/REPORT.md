# Paper trading report

Updated 2026-11-04 10:43 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,508 | +6.25% | 0 | - | 236 |
| snake_abs_exit_conv | 208,697 | +4.35% | 1 | 100% | 255 |
| snake_abs_exit | 208,540 | +4.27% | 1 | 100% | 260 |
| intraweek | 207,830 | +3.92% | 25 | 48% | 2,757 |
| benchmark | 207,611 | +3.81% | 0 | - | 237 |
| snake_viper_wild | 206,885 | +3.44% | 3 | 33% | 702 |
| snake_abs | 205,605 | +2.80% | 1 | 100% | 255 |
| snake_abs_conv | 205,453 | +2.73% | 1 | 100% | 255 |
| intramonth | 205,287 | +2.64% | 0 | - | 235 |
| snake_viper_tick | 203,275 | +1.64% | 2 | 0% | 532 |
| random_hold | 202,291 | +1.15% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,248 | +0.12% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,484 | -1.26% | 3 | 33% | 361 |
| benchmark_smallcap | 194,484 | -2.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,448 | -6.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,583 (-5.71%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,526 | +2.22% |
| snake_abs_exit_conv | +4,358 | +2.13% |
| snake_abs_conv | +4,312 | +2.14% |
| snake_abs | +4,296 | +2.13% |
| snake_anaconda | +3,660 | +1.89% |
| intraweek | +2,745 | +1.34% |
| gold | +2,170 | +1.17% |
| random_hold | +1,822 | +0.91% |
| benchmark_smallcap | +1,547 | +0.80% |
| intramonth | +1,316 | +0.65% |
| benchmark | +910 | +0.44% |
| unified | +507 | +0.24% |
| oracle | +258 | +0.13% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,892 | -1.88% |
| snake_viper_wild | -4,007 | -1.90% |

Average per day so far: unified Rs +463, snake_viper_wild Rs +362, snake_abs_exit_conv Rs +362, snake_abs_exit Rs +356, intraweek Rs +290, benchmark Rs +282, snake_abs_conv Rs +227, snake_abs Rs +224, snake_viper_tick Rs +205, intramonth Rs +196, random_hold Rs +85, nifty_calls Rs +68, oracle Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -114, benchmark_smallcap Rs -240, snake_nonews Rs -444, gold Rs -465, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.