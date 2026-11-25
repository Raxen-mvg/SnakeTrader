# Paper trading report

Updated 2026-11-25 12:27 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,765 | +12.88% | 0 | - | 237 |
| unified | 225,432 | +12.72% | 0 | - | 236 |
| intramonth | 213,517 | +6.76% | 0 | - | 235 |
| oracle | 212,866 | +6.43% | 0 | - | 233 |
| random_hold | 210,081 | +5.04% | 12 | 75% | 1,009 |
| intraweek | 208,149 | +4.07% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,313 | +1.16% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,849 | +0.92% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,620 | +0.31% | 1 | 100% | 255 |
| snake_abs_conv | 200,438 | +0.22% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,562 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 196,770 | -1.61% | 16 | 50% | 2,827 |
| snake_anaconda | 193,971 | -3.02% | 3 | 33% | 374 |
| snake_viper_tick | 193,420 | -3.29% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,432 | -17.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,620 (-5.19%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,292 | +1.94% |
| random_hold | +1,655 | +0.79% |
| unified | +1,147 | +0.51% |
| intramonth | +765 | +0.36% |
| benchmark_smallcap | +583 | +0.29% |
| oracle | +524 | +0.25% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,470 | -1.64% |
| snake_viper_tick | -4,272 | -2.16% |
| snake_viper_wild | -4,354 | -2.17% |
| snake_anaconda | -4,733 | -2.38% |
| snake_abs | -4,841 | -2.36% |
| snake_abs_conv | -4,865 | -2.37% |
| gold | -4,998 | -2.95% |
| snake_abs_exit | -5,182 | -2.50% |
| snake_abs_exit_conv | -5,197 | -2.51% |

Average per day so far: benchmark Rs +644, unified Rs +636, intramonth Rs +338, oracle Rs +322, random_hold Rs +252, intraweek Rs +204, snake_abs_exit Rs +63, snake_abs_exit_conv Rs +50, nifty_calls Rs +46, snake_abs Rs +16, snake_abs_conv Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -101, snake_anaconda Rs -172, snake_viper_tick Rs -227, snake_nonews Rs -292, snake Rs -311, gold Rs -889

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.