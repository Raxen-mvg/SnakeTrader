# Paper trading report

Updated 2026-11-06 10:20 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,978 | +7.49% | 0 | - | 237 |
| unified | 214,975 | +7.49% | 0 | - | 236 |
| intraweek | 210,553 | +5.28% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,378 | +4.69% | 1 | 100% | 255 |
| snake_abs_exit | 209,168 | +4.58% | 1 | 100% | 260 |
| intramonth | 207,041 | +3.52% | 0 | - | 235 |
| snake_abs | 206,328 | +3.16% | 1 | 100% | 255 |
| snake_abs_conv | 206,160 | +3.08% | 1 | 100% | 255 |
| oracle | 204,571 | +2.29% | 0 | - | 233 |
| random_hold | 203,643 | +1.82% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,721 | -1.14% | 3 | 33% | 702 |
| snake_anaconda | 196,533 | -1.73% | 3 | 33% | 374 |
| benchmark_smallcap | 195,067 | -2.47% | 0 | - | 237 |
| snake_viper_tick | 194,364 | -2.82% | 2 | 0% | 532 |
| gold | 190,506 | -4.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,412 (-6.29%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,209 | +0.56% |
| intraweek | +1,135 | +0.54% |
| oracle | +499 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -680 | -0.33% |
| intramonth | -908 | -0.44% |
| unified | -1,008 | -0.47% |
| benchmark_smallcap | -3,621 | -1.82% |
| gold | -3,715 | -1.91% |
| snake_abs | -5,360 | -2.53% |
| snake_abs_conv | -5,385 | -2.55% |
| snake_abs_exit_conv | -5,425 | -2.53% |
| snake_abs_exit | -5,491 | -2.56% |
| snake_anaconda | -5,946 | -2.94% |
| snake_viper_tick | -6,774 | -3.37% |
| snake_viper_wild | -6,935 | -3.39% |

Average per day so far: benchmark Rs +516, unified Rs +516, intraweek Rs +364, snake_abs_exit_conv Rs +361, snake_abs_exit Rs +353, intramonth Rs +243, snake_abs_conv Rs +237, snake_abs Rs +234, oracle Rs +158, random_hold Rs +126, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -109, snake_anaconda Rs -144, benchmark_smallcap Rs -197, snake_viper_tick Rs -313, gold Rs -327, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.