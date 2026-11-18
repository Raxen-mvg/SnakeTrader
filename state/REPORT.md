# Paper trading report

Updated 2026-11-18 12:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,122 | +11.06% | 0 | - | 236 |
| benchmark | 219,828 | +9.91% | 0 | - | 237 |
| intraweek | 213,101 | +6.55% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,288 | +6.14% | 2 | 50% | 345 |
| intramonth | 212,264 | +6.13% | 0 | - | 235 |
| oracle | 211,481 | +5.74% | 0 | - | 233 |
| snake_abs_exit_conv | 210,511 | +5.25% | 2 | 50% | 345 |
| snake_abs | 207,645 | +3.82% | 1 | 100% | 255 |
| snake_abs_conv | 207,505 | +3.75% | 1 | 100% | 255 |
| random_hold | 206,964 | +3.48% | 10 | 70% | 733 |
| snake_viper_wild | 206,651 | +3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,123 | +1.56% | 15 | 47% | 2,625 |
| snake_anaconda | 202,464 | +1.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,058 | -0.47% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,976 | -11.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,855 (-4.57%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +721 | +0.34% |
| unified | +683 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -222 | -0.10% |
| snake_abs_exit | -854 | -0.40% |
| snake_abs | -914 | -0.44% |
| snake_abs_conv | -915 | -0.44% |
| oracle | -1,005 | -0.47% |
| snake_abs_exit_conv | -1,063 | -0.50% |
| random_hold | -1,468 | -0.70% |
| benchmark_smallcap | -1,513 | -0.76% |
| snake_anaconda | -1,591 | -0.78% |
| benchmark | -1,775 | -0.80% |
| snake_viper_tick | -2,714 | -1.32% |
| snake_viper_wild | -2,764 | -1.32% |
| gold | -3,748 | -2.07% |

Average per day so far: unified Rs +614, benchmark Rs +551, snake_abs_exit Rs +372, intraweek Rs +364, intramonth Rs +341, oracle Rs +319, snake_abs_exit_conv Rs +319, snake_viper_wild Rs +238, snake_abs_conv Rs +227, snake_abs Rs +225, random_hold Rs +193, snake_viper_tick Rs +125, snake_anaconda Rs +79, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.