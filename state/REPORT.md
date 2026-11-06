# Paper trading report

Updated 2026-11-06 13:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,055 | +7.53% | 0 | - | 237 |
| unified | 214,477 | +7.24% | 0 | - | 236 |
| snake_abs_exit_conv | 208,407 | +4.20% | 1 | 100% | 255 |
| intraweek | 208,385 | +4.19% | 25 | 48% | 2,757 |
| snake_abs_exit | 208,289 | +4.14% | 1 | 100% | 260 |
| intramonth | 206,734 | +3.37% | 0 | - | 235 |
| snake_abs | 205,395 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,211 | +2.60% | 1 | 100% | 255 |
| oracle | 204,975 | +2.49% | 0 | - | 233 |
| random_hold | 203,086 | +1.54% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,762 | -1.62% | 3 | 33% | 702 |
| snake_anaconda | 195,848 | -2.08% | 3 | 33% | 374 |
| benchmark_smallcap | 194,563 | -2.72% | 0 | - | 237 |
| snake_viper_tick | 193,430 | -3.29% | 2 | 0% | 532 |
| gold | 189,947 | -5.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,750 (-6.63%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,285 | +0.60% |
| oracle | +903 | +0.44% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -1,033 | -0.49% |
| intramonth | -1,215 | -0.58% |
| random_hold | -1,237 | -0.60% |
| unified | -1,507 | -0.70% |
| benchmark_smallcap | -4,125 | -2.08% |
| gold | -4,274 | -2.20% |
| snake_abs | -6,294 | -2.97% |
| snake_abs_conv | -6,334 | -2.99% |
| snake_abs_exit | -6,370 | -2.97% |
| snake_abs_exit_conv | -6,397 | -2.98% |
| snake_anaconda | -6,632 | -3.27% |
| snake_viper_tick | -7,708 | -3.83% |
| snake_viper_wild | -7,894 | -3.86% |

Average per day so far: benchmark Rs +519, unified Rs +499, snake_abs_exit_conv Rs +323, snake_abs_exit Rs +319, intraweek Rs +289, intramonth Rs +232, snake_abs_conv Rs +200, snake_abs Rs +200, oracle Rs +172, random_hold Rs +106, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -154, snake_anaconda Rs -173, benchmark_smallcap Rs -217, gold Rs -347, snake_viper_tick Rs -365, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.