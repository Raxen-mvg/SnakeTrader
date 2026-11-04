# Paper trading report

Updated 2026-11-04 11:43 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,137 | +6.57% | 0 | - | 236 |
| intraweek | 208,855 | +4.43% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,694 | +4.35% | 1 | 100% | 255 |
| snake_abs_exit | 208,566 | +4.28% | 1 | 100% | 260 |
| benchmark | 207,374 | +3.69% | 0 | - | 237 |
| snake_viper_wild | 206,875 | +3.44% | 3 | 33% | 702 |
| snake_abs | 205,601 | +2.80% | 1 | 100% | 255 |
| intramonth | 205,543 | +2.77% | 0 | - | 235 |
| snake_abs_conv | 205,451 | +2.73% | 1 | 100% | 255 |
| snake_viper_tick | 203,272 | +1.64% | 2 | 0% | 532 |
| random_hold | 202,588 | +1.29% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,741 | +0.37% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,561 | -1.22% | 3 | 33% | 361 |
| benchmark_smallcap | 194,619 | -2.69% | 0 | - | 237 |
| gold | 190,177 | -4.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,899 (-5.55%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,899 | +2.64% |
| snake_abs_exit | +4,552 | +2.23% |
| snake_abs_exit_conv | +4,356 | +2.13% |
| snake_abs_conv | +4,310 | +2.14% |
| snake_abs | +4,292 | +2.13% |
| intraweek | +3,770 | +1.84% |
| snake_anaconda | +3,736 | +1.93% |
| random_hold | +2,120 | +1.06% |
| benchmark_smallcap | +1,682 | +0.87% |
| intramonth | +1,572 | +0.77% |
| unified | +1,136 | +0.54% |
| oracle | +752 | +0.38% |
| benchmark | +673 | +0.33% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,895 | -1.88% |
| snake_viper_wild | -4,017 | -1.91% |

Average per day so far: unified Rs +487, snake_abs_exit_conv Rs +362, snake_viper_wild Rs +362, snake_abs_exit Rs +357, intraweek Rs +328, benchmark Rs +273, snake_abs_conv Rs +227, snake_abs Rs +224, intramonth Rs +205, snake_viper_tick Rs +204, random_hold Rs +96, nifty_calls Rs +68, oracle Rs +27, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -111, benchmark_smallcap Rs -234, gold Rs -364, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.