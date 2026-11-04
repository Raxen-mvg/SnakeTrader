# Paper trading report

Updated 2026-11-04 10:07 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,205 | +6.60% | 0 | - | 236 |
| snake_abs_exit_conv | 209,664 | +4.83% | 1 | 100% | 255 |
| snake_abs_exit | 209,497 | +4.75% | 1 | 100% | 260 |
| benchmark | 208,621 | +4.31% | 0 | - | 237 |
| intraweek | 208,049 | +4.02% | 25 | 48% | 2,757 |
| snake_abs | 206,550 | +3.27% | 1 | 100% | 255 |
| snake_abs_conv | 206,407 | +3.20% | 1 | 100% | 255 |
| snake_viper_wild | 206,356 | +3.18% | 3 | 33% | 702 |
| intramonth | 205,733 | +2.87% | 0 | - | 235 |
| random_hold | 202,915 | +1.46% | 8 | 62% | 649 |
| snake_viper_tick | 202,756 | +1.38% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,545 | +0.27% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,246 | -0.88% | 3 | 33% | 361 |
| benchmark_smallcap | 194,294 | -2.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,856 | -6.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,674 (-5.66%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +5,483 | +2.69% |
| snake_abs_exit_conv | +5,326 | +2.61% |
| snake_abs_conv | +5,266 | +2.62% |
| snake_abs | +5,241 | +2.60% |
| snake_anaconda | +4,422 | +2.28% |
| intraweek | +2,964 | +1.45% |
| random_hold | +2,447 | +1.22% |
| benchmark | +1,920 | +0.93% |
| intramonth | +1,762 | +0.86% |
| gold | +1,578 | +0.85% |
| benchmark_smallcap | +1,356 | +0.70% |
| unified | +1,204 | +0.57% |
| oracle | +555 | +0.28% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,411 | -2.13% |
| snake_viper_wild | -4,537 | -2.15% |

Average per day so far: unified Rs +489, snake_abs_exit_conv Rs +403, snake_abs_exit Rs +396, snake_viper_wild Rs +335, benchmark Rs +319, intraweek Rs +298, snake_abs_conv Rs +267, snake_abs Rs +262, intramonth Rs +212, snake_viper_tick Rs +172, random_hold Rs +108, nifty_calls Rs +68, oracle Rs +20, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -80, benchmark_smallcap Rs -248, snake_nonews Rs -444, snake Rs -467, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.