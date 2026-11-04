# Paper trading report

Updated 2026-11-04 10:36 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,963 | +6.48% | 0 | - | 236 |
| snake_abs_exit_conv | 208,795 | +4.40% | 1 | 100% | 255 |
| snake_abs_exit | 208,638 | +4.32% | 1 | 100% | 260 |
| intraweek | 208,494 | +4.25% | 25 | 48% | 2,757 |
| benchmark | 207,741 | +3.87% | 0 | - | 237 |
| snake_viper_wild | 206,786 | +3.39% | 3 | 33% | 702 |
| snake_abs | 205,704 | +2.85% | 1 | 100% | 255 |
| snake_abs_conv | 205,550 | +2.77% | 1 | 100% | 255 |
| intramonth | 205,382 | +2.69% | 0 | - | 235 |
| snake_viper_tick | 203,178 | +1.59% | 2 | 0% | 532 |
| random_hold | 202,235 | +1.12% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,133 | +0.07% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,530 | -1.24% | 3 | 33% | 361 |
| benchmark_smallcap | 194,507 | -2.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,448 | -6.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,759 (-5.62%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,623 | +2.27% |
| snake_abs_exit_conv | +4,457 | +2.18% |
| snake_abs_conv | +4,409 | +2.19% |
| snake_abs | +4,395 | +2.18% |
| snake_anaconda | +3,706 | +1.91% |
| intraweek | +3,408 | +1.66% |
| gold | +2,170 | +1.17% |
| random_hold | +1,767 | +0.88% |
| benchmark_smallcap | +1,569 | +0.81% |
| intramonth | +1,411 | +0.69% |
| benchmark | +1,040 | +0.50% |
| unified | +962 | +0.45% |
| oracle | +144 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,988 | -1.93% |
| snake_viper_wild | -4,106 | -1.95% |

Average per day so far: unified Rs +480, snake_abs_exit_conv Rs +366, snake_abs_exit Rs +360, snake_viper_wild Rs +357, intraweek Rs +315, benchmark Rs +287, snake_abs_conv Rs +231, snake_abs Rs +228, intramonth Rs +199, snake_viper_tick Rs +199, random_hold Rs +83, nifty_calls Rs +68, oracle Rs +5, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -112, benchmark_smallcap Rs -239, snake_nonews Rs -444, gold Rs -465, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.