# Paper trading report

Updated 2026-11-25 14:04 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,702 | +12.35% | 0 | - | 237 |
| unified | 224,670 | +12.34% | 0 | - | 236 |
| oracle | 212,618 | +6.31% | 0 | - | 233 |
| intramonth | 212,264 | +6.13% | 0 | - | 235 |
| random_hold | 209,586 | +4.79% | 12 | 75% | 1,009 |
| intraweek | 207,380 | +3.69% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,383 | +0.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,104 | +0.55% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,634 | -0.18% | 1 | 100% | 255 |
| snake_abs_conv | 199,435 | -0.28% | 1 | 100% | 255 |
| benchmark_smallcap | 198,834 | -0.58% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,165 | -3.42% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,106 | -17.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,973 (-5.51%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,228 | +1.46% |
| random_hold | +1,160 | +0.56% |
| unified | +385 | +0.17% |
| oracle | +276 | +0.13% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -146 | -0.07% |
| intramonth | -488 | -0.23% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| intraweek | -4,239 | -2.00% |
| gold | -4,324 | -2.55% |
| snake_anaconda | -5,538 | -2.79% |
| snake_abs | -5,826 | -2.84% |
| snake_abs_conv | -5,867 | -2.86% |
| snake_abs_exit_conv | -5,942 | -2.87% |
| snake_abs_exit | -6,112 | -2.95% |

Average per day so far: benchmark Rs +618, unified Rs +617, oracle Rs +315, intramonth Rs +307, random_hold Rs +240, intraweek Rs +184, nifty_calls Rs +46, snake_abs_exit Rs +37, snake_abs_exit_conv Rs +30, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, benchmark_smallcap Rs -32, snake_viper_wild Rs -88, snake_anaconda Rs -195, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.