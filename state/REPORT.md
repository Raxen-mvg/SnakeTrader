# Paper trading report

Updated 2026-11-16 14:11 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,590 | +10.29% | 0 | - | 236 |
| benchmark | 219,798 | +9.90% | 0 | - | 237 |
| snake_abs_exit | 213,366 | +6.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,156 | +6.08% | 2 | 50% | 345 |
| oracle | 211,302 | +5.65% | 0 | - | 233 |
| intramonth | 211,244 | +5.62% | 0 | - | 235 |
| intraweek | 210,962 | +5.48% | 35 | 54% | 3,851 |
| snake_abs | 209,448 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,287 | +4.64% | 1 | 100% | 255 |
| random_hold | 207,686 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 205,388 | +2.69% | 14 | 50% | 2,496 |
| snake_anaconda | 203,812 | +1.91% | 3 | 33% | 374 |
| snake_viper_tick | 201,876 | +0.94% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,267 | -9.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,313 (-4.84%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,570 | +0.72% |
| intramonth | +1,187 | +0.56% |
| snake_viper_wild | +631 | +0.31% |
| snake_viper_tick | +621 | +0.31% |
| random_hold | +460 | +0.22% |
| benchmark | +459 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -1,080 | -0.53% |
| oracle | -1,795 | -0.84% |
| benchmark_smallcap | -2,646 | -1.30% |
| gold | -2,729 | -1.48% |
| snake_abs_conv | -3,079 | -1.45% |
| snake_abs | -3,092 | -1.46% |
| snake_abs_exit | -3,619 | -1.67% |
| snake_abs_exit_conv | -4,226 | -1.95% |
| intraweek | -5,183 | -2.40% |

Average per day so far: unified Rs +606, benchmark Rs +582, snake_abs_exit Rs +431, snake_abs_exit_conv Rs +392, oracle Rs +332, intramonth Rs +331, intraweek Rs +322, snake_abs_conv Rs +300, snake_abs Rs +295, random_hold Rs +226, snake_viper_wild Rs +207, snake_anaconda Rs +131, snake_viper_tick Rs +82, nifty_calls Rs +54, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -551

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.