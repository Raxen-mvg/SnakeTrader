# Paper trading report

Updated 2026-11-06 11:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,781 | +7.39% | 0 | - | 236 |
| benchmark | 214,642 | +7.32% | 0 | - | 237 |
| intraweek | 211,042 | +5.52% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,155 | +4.58% | 1 | 100% | 255 |
| snake_abs_exit | 208,942 | +4.47% | 1 | 100% | 260 |
| intramonth | 206,830 | +3.42% | 0 | - | 235 |
| snake_abs | 206,114 | +3.06% | 1 | 100% | 255 |
| snake_abs_conv | 205,945 | +2.97% | 1 | 100% | 255 |
| oracle | 204,595 | +2.30% | 0 | - | 233 |
| random_hold | 203,341 | +1.67% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,536 | -1.73% | 3 | 33% | 374 |
| snake_viper_wild | 195,336 | -2.33% | 3 | 33% | 702 |
| benchmark_smallcap | 194,809 | -2.60% | 0 | - | 237 |
| snake_viper_tick | 192,028 | -3.99% | 2 | 0% | 532 |
| gold | 190,111 | -4.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,247 (-6.38%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,624 | +0.78% |
| benchmark | +872 | +0.41% |
| oracle | +523 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -982 | -0.48% |
| intramonth | -1,118 | -0.54% |
| unified | -1,202 | -0.56% |
| benchmark_smallcap | -3,879 | -1.95% |
| gold | -4,110 | -2.12% |
| snake_abs | -5,574 | -2.63% |
| snake_abs_conv | -5,600 | -2.65% |
| snake_abs_exit_conv | -5,648 | -2.63% |
| snake_abs_exit | -5,717 | -2.66% |
| snake_anaconda | -5,944 | -2.94% |
| snake_viper_tick | -9,110 | -4.53% |
| snake_viper_wild | -9,320 | -4.55% |

Average per day so far: unified Rs +510, benchmark Rs +505, intraweek Rs +381, snake_abs_exit_conv Rs +352, snake_abs_exit Rs +344, intramonth Rs +236, snake_abs_conv Rs +229, snake_abs Rs +226, oracle Rs +158, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -144, benchmark_smallcap Rs -208, snake_viper_wild Rs -222, gold Rs -341, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -443

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.