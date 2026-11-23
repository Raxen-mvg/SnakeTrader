# Paper trading report

Updated 2026-11-23 14:22 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,115 | +12.06% | 0 | - | 236 |
| benchmark | 222,231 | +11.12% | 0 | - | 237 |
| intraweek | 212,334 | +6.17% | 40 | 55% | 4,400 |
| intramonth | 212,210 | +6.11% | 0 | - | 235 |
| oracle | 211,944 | +5.97% | 0 | - | 233 |
| random_hold | 208,965 | +4.48% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,210 | +3.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,544 | +3.27% | 2 | 50% | 345 |
| snake_abs | 204,928 | +2.46% | 1 | 100% | 255 |
| snake_abs_conv | 204,752 | +2.38% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,239 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| snake_anaconda | 198,204 | -0.90% | 3 | 33% | 374 |
| snake_viper_tick | 197,805 | -1.10% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,479 | -15.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,265 (-4.87%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,430 | +0.85% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -72 | -0.04% |
| oracle | -535 | -0.25% |
| snake_abs | -992 | -0.48% |
| snake_abs_conv | -1,031 | -0.50% |
| benchmark_smallcap | -1,256 | -0.62% |
| snake_abs_exit | -1,353 | -0.65% |
| snake_viper_tick | -1,566 | -0.79% |
| snake_viper_wild | -1,590 | -0.78% |
| snake_anaconda | -1,701 | -0.85% |
| random_hold | -1,794 | -0.85% |
| unified | -2,066 | -0.91% |
| intramonth | -2,794 | -1.30% |
| benchmark | -2,907 | -1.29% |
| intraweek | -3,378 | -1.57% |

Average per day so far: unified Rs +618, benchmark Rs +570, intraweek Rs +316, intramonth Rs +313, oracle Rs +306, random_hold Rs +230, snake_abs_exit Rs +200, snake_abs_exit_conv Rs +182, snake_abs Rs +133, snake_abs_conv Rs +132, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_anaconda Rs -53, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.