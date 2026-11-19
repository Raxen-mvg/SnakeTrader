# Paper trading report

Updated 2026-11-19 12:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,813 | +11.91% | 0 | - | 236 |
| benchmark | 221,519 | +10.76% | 0 | - | 237 |
| intramonth | 213,380 | +6.69% | 0 | - | 235 |
| snake_abs_exit | 213,185 | +6.59% | 2 | 50% | 345 |
| intraweek | 211,454 | +5.73% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,343 | +5.67% | 2 | 50% | 345 |
| oracle | 210,942 | +5.47% | 0 | - | 233 |
| snake_abs | 208,922 | +4.46% | 1 | 100% | 255 |
| snake_abs_conv | 208,799 | +4.40% | 1 | 100% | 255 |
| snake_viper_wild | 207,595 | +3.80% | 16 | 50% | 2,827 |
| random_hold | 207,532 | +3.77% | 10 | 70% | 733 |
| snake_viper_tick | 204,047 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,203 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,582 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,740 | -12.63% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,154 (-4.42%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,256 | +0.63% |
| benchmark | +1,224 | +0.56% |
| unified | +1,202 | +0.54% |
| intramonth | +1,106 | +0.52% |
| random_hold | +600 | +0.29% |
| snake_viper_wild | +555 | +0.27% |
| snake_viper_tick | +544 | +0.27% |
| oracle | +146 | +0.07% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -385 | -0.18% |
| snake_abs | -514 | -0.25% |
| snake_abs_conv | -526 | -0.25% |
| snake_abs_exit | -847 | -0.40% |
| snake_abs_exit_conv | -1,041 | -0.49% |
| snake_anaconda | -1,198 | -0.59% |
| gold | -2,581 | -1.46% |

Average per day so far: unified Rs +644, benchmark Rs +582, snake_abs_exit Rs +388, intramonth Rs +362, snake_abs_exit_conv Rs +334, intraweek Rs +310, oracle Rs +296, snake_viper_wild Rs +262, snake_abs_conv Rs +259, snake_abs Rs +255, random_hold Rs +204, snake_viper_tick Rs +156, snake_anaconda Rs +100, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -683

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.