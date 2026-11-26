# Paper trading report

Updated 2026-11-26 14:29 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,382 | +12.69% | 0 | - | 237 |
| unified | 223,291 | +11.64% | 0 | - | 236 |
| oracle | 213,107 | +6.55% | 0 | - | 233 |
| intramonth | 210,515 | +5.26% | 0 | - | 235 |
| random_hold | 209,316 | +4.66% | 13 | 69% | 1,037 |
| intraweek | 207,923 | +3.96% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| snake_abs_exit | 200,078 | +0.04% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,459 | -0.27% | 2 | 50% | 345 |
| snake_abs | 197,758 | -1.12% | 1 | 100% | 255 |
| snake_abs_conv | 197,552 | -1.22% | 1 | 100% | 255 |
| snake_viper_wild | 192,345 | -3.83% | 16 | 50% | 2,827 |
| snake_anaconda | 191,511 | -4.25% | 3 | 33% | 374 |
| snake_viper_tick | 189,077 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,438 | -16.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,616 (-5.69%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,861 | +0.94% |
| gold | +1,841 | +1.12% |
| intraweek | +1,180 | +0.57% |
| benchmark | +360 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -176 | -0.08% |
| oracle | -688 | -0.32% |
| unified | -809 | -0.36% |
| intramonth | -1,178 | -0.56% |
| snake_abs_exit | -2,178 | -1.08% |
| snake_abs | -2,392 | -1.20% |
| snake_abs_conv | -2,420 | -1.21% |
| snake_abs_exit_conv | -2,517 | -1.25% |
| snake_anaconda | -3,042 | -1.56% |
| snake_viper_tick | -5,099 | -2.63% |
| snake_viper_wild | -5,199 | -2.63% |

Average per day so far: benchmark Rs +619, unified Rs +568, oracle Rs +320, intramonth Rs +256, random_hold Rs +227, intraweek Rs +193, nifty_calls Rs +45, benchmark_smallcap Rs +18, snake_abs_exit Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -14, snake_abs Rs -57, snake_abs_conv Rs -64, snake_viper_wild Rs -232, snake_anaconda Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -819

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.