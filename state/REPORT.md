# Paper trading report

Updated 2026-11-26 12:25 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,270 | +13.13% | 0 | - | 237 |
| unified | 223,492 | +11.75% | 0 | - | 236 |
| oracle | 213,251 | +6.62% | 0 | - | 233 |
| intramonth | 210,643 | +5.32% | 0 | - | 235 |
| random_hold | 209,825 | +4.91% | 13 | 69% | 1,037 |
| intraweek | 208,322 | +4.16% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,758 | +0.38% | 2 | 50% | 345 |
| benchmark_smallcap | 200,650 | +0.33% | 0 | - | 237 |
| snake_abs_exit_conv | 200,159 | +0.08% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,434 | -0.78% | 1 | 100% | 255 |
| snake_abs_conv | 198,239 | -0.88% | 1 | 100% | 255 |
| snake_anaconda | 192,316 | -3.84% | 3 | 33% | 374 |
| snake_viper_wild | 192,038 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,777 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,862 | -17.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,868 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,838 | +0.93% |
| intraweek | +1,579 | +0.76% |
| gold | +1,266 | +0.77% |
| benchmark | +1,247 | +0.55% |
| random_hold | +332 | +0.16% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -545 | -0.26% |
| unified | -608 | -0.27% |
| intramonth | -1,051 | -0.50% |
| snake_abs_exit | -1,498 | -0.74% |
| snake_abs | -1,716 | -0.86% |
| snake_abs_conv | -1,734 | -0.87% |
| snake_abs_exit_conv | -1,817 | -0.90% |
| snake_anaconda | -2,237 | -1.15% |
| snake_viper_tick | -5,400 | -2.78% |
| snake_viper_wild | -5,506 | -2.79% |

Average per day so far: benchmark Rs +641, unified Rs +573, oracle Rs +323, intramonth Rs +260, random_hold Rs +240, intraweek Rs +203, nifty_calls Rs +45, snake_abs_exit Rs +20, benchmark_smallcap Rs +18, snake_abs_exit_conv Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -40, snake_abs_conv Rs -46, snake_anaconda Rs -213, snake_viper_wild Rs -241, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -374, gold Rs -833

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.