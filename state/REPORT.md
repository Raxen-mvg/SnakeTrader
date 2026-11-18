# Paper trading report

Updated 2026-11-18 13:20 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,057 | +11.53% | 0 | - | 236 |
| benchmark | 219,882 | +9.94% | 0 | - | 237 |
| intramonth | 212,923 | +6.46% | 0 | - | 235 |
| intraweek | 212,601 | +6.30% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,567 | +6.28% | 2 | 50% | 345 |
| oracle | 212,235 | +6.12% | 0 | - | 233 |
| snake_abs_exit_conv | 210,830 | +5.42% | 2 | 50% | 345 |
| snake_abs | 207,822 | +3.91% | 1 | 100% | 255 |
| snake_abs_conv | 207,687 | +3.84% | 1 | 100% | 255 |
| random_hold | 207,154 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 206,670 | +3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,141 | +1.57% | 15 | 47% | 2,625 |
| snake_anaconda | 202,958 | +1.48% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,192 | -0.40% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,877 | -11.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,262 (-4.37%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,619 | +0.73% |
| intramonth | +1,381 | +0.65% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -252 | -0.12% |
| snake_abs_exit | -575 | -0.27% |
| intraweek | -722 | -0.34% |
| snake_abs_conv | -733 | -0.35% |
| snake_abs | -737 | -0.35% |
| snake_abs_exit_conv | -743 | -0.35% |
| snake_anaconda | -1,097 | -0.54% |
| random_hold | -1,278 | -0.61% |
| benchmark_smallcap | -1,379 | -0.69% |
| benchmark | -1,721 | -0.78% |
| snake_viper_tick | -2,695 | -1.31% |
| snake_viper_wild | -2,745 | -1.31% |
| gold | -3,847 | -2.13% |

Average per day so far: unified Rs +640, benchmark Rs +552, snake_abs_exit Rs +381, intramonth Rs +359, intraweek Rs +350, oracle Rs +340, snake_abs_exit_conv Rs +328, snake_viper_wild Rs +238, snake_abs_conv Rs +233, snake_abs Rs +230, random_hold Rs +199, snake_viper_tick Rs +126, snake_anaconda Rs +95, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -25, snake_nonews Rs -326, snake Rs -347, gold Rs -642

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.