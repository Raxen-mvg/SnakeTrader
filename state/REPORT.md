# Paper trading report

Updated 2026-11-18 13:27 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,947 | +11.47% | 0 | - | 236 |
| benchmark | 219,828 | +9.91% | 0 | - | 237 |
| intramonth | 212,768 | +6.38% | 0 | - | 235 |
| snake_abs_exit | 212,582 | +6.29% | 2 | 50% | 345 |
| oracle | 212,255 | +6.13% | 0 | - | 233 |
| intraweek | 212,209 | +6.10% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,882 | +5.44% | 2 | 50% | 345 |
| snake_abs | 207,835 | +3.92% | 1 | 100% | 255 |
| snake_abs_conv | 207,700 | +3.85% | 1 | 100% | 255 |
| random_hold | 206,958 | +3.48% | 10 | 70% | 733 |
| snake_viper_wild | 206,713 | +3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,184 | +1.59% | 15 | 47% | 2,625 |
| snake_anaconda | 202,973 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,058 | -11.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,143 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,508 | +0.68% |
| intramonth | +1,226 | +0.58% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -232 | -0.11% |
| snake_abs_exit | -559 | -0.26% |
| snake_abs_exit_conv | -692 | -0.33% |
| snake_abs_conv | -720 | -0.34% |
| snake_abs | -723 | -0.35% |
| snake_anaconda | -1,082 | -0.53% |
| intraweek | -1,114 | -0.52% |
| benchmark_smallcap | -1,390 | -0.69% |
| random_hold | -1,474 | -0.71% |
| benchmark | -1,775 | -0.80% |
| snake_viper_tick | -2,653 | -1.29% |
| snake_viper_wild | -2,702 | -1.29% |
| gold | -3,666 | -2.03% |

Average per day so far: unified Rs +637, benchmark Rs +551, snake_abs_exit Rs +381, intramonth Rs +355, oracle Rs +340, intraweek Rs +339, snake_abs_exit_conv Rs +330, snake_viper_wild Rs +240, snake_abs_conv Rs +233, snake_abs Rs +230, random_hold Rs +193, snake_viper_tick Rs +127, snake_anaconda Rs +96, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -637

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.