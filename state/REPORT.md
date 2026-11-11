# Paper trading report

Updated 2026-11-11 09:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,907 | +10.45% | 0 | - | 237 |
| unified | 219,972 | +9.99% | 0 | - | 236 |
| snake_abs_exit_conv | 215,144 | +7.57% | 2 | 50% | 330 |
| snake_abs_exit | 214,502 | +7.25% | 2 | 50% | 308 |
| intraweek | 214,258 | +7.13% | 30 | 53% | 3,302 |
| snake_abs | 212,884 | +6.44% | 1 | 100% | 255 |
| snake_abs_conv | 212,724 | +6.36% | 1 | 100% | 255 |
| oracle | 211,085 | +5.54% | 0 | - | 233 |
| intramonth | 210,942 | +5.47% | 0 | - | 235 |
| random_hold | 205,991 | +3.00% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,694 | +0.85% | 3 | 33% | 374 |
| snake_viper_wild | 200,643 | +0.32% | 7 | 57% | 1,332 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,236 | -1.38% | 6 | 50% | 1,154 |
| gold | 189,470 | -5.26% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,931 (-4.53%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +3,246 | +1.55% |
| snake_abs | +3,237 | +1.54% |
| snake_abs_exit_conv | +3,235 | +1.53% |
| snake_viper_wild | +3,213 | +1.63% |
| snake_viper_tick | +3,159 | +1.63% |
| benchmark | +2,815 | +1.29% |
| snake_abs_exit | +2,518 | +1.19% |
| benchmark_smallcap | +2,365 | +1.19% |
| snake_anaconda | +2,228 | +1.12% |
| oracle | +1,167 | +0.56% |
| random_hold | +1,031 | +0.50% |
| intramonth | +333 | +0.16% |
| unified | +225 | +0.10% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -284 | -0.13% |
| gold | -2,663 | -1.39% |

Average per day so far: benchmark Rs +674, unified Rs +644, snake_abs_exit_conv Rs +541, snake_abs_exit Rs +518, intraweek Rs +460, snake_abs_conv Rs +454, snake_abs Rs +444, oracle Rs +358, intramonth Rs +353, random_hold Rs +193, snake_anaconda Rs +65, nifty_calls Rs +59, snake_viper_wild Rs +28, benchmark_smallcap Rs +20, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -138, gold Rs -340, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.