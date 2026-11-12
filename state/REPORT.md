# Paper trading report

Updated 2026-11-12 15:16 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,719 | +10.36% | 0 | - | 236 |
| benchmark | 220,532 | +10.27% | 0 | - | 237 |
| snake_abs_exit_conv | 219,501 | +9.75% | 2 | 50% | 345 |
| snake_abs_exit | 218,241 | +9.12% | 2 | 50% | 345 |
| snake_abs | 216,449 | +8.22% | 1 | 100% | 255 |
| snake_abs_conv | 216,277 | +8.14% | 1 | 100% | 255 |
| intraweek | 214,645 | +7.32% | 30 | 53% | 3,302 |
| oracle | 213,134 | +6.57% | 0 | - | 233 |
| intramonth | 211,604 | +5.80% | 0 | - | 235 |
| random_hold | 208,052 | +4.03% | 10 | 70% | 733 |
| snake_anaconda | 206,778 | +3.39% | 3 | 33% | 374 |
| snake_viper_wild | 205,757 | +2.88% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,138 | +1.57% | 0 | - | 237 |
| snake_viper_tick | 202,238 | +1.12% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,294 | -7.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,127 (-3.94%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs | +2,825 | +1.32% |
| snake_abs_conv | +2,819 | +1.32% |
| snake_anaconda | +2,655 | +1.30% |
| snake_abs_exit_conv | +2,349 | +1.08% |
| benchmark_smallcap | +2,332 | +1.16% |
| snake_abs_exit | +2,078 | +0.96% |
| intraweek | +1,512 | +0.71% |
| benchmark | +1,270 | +0.58% |
| oracle | +1,131 | +0.53% |
| random_hold | +941 | +0.45% |
| unified | +905 | +0.41% |
| intramonth | +608 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -970 | -0.48% |
| snake_viper_wild | -985 | -0.48% |
| gold | -4,291 | -2.26% |

Average per day so far: snake_abs_exit_conv Rs +672, unified Rs +647, benchmark Rs +642, snake_abs_exit Rs +629, snake_abs_conv Rs +561, snake_abs Rs +548, intraweek Rs +458, oracle Rs +410, intramonth Rs +363, random_hold Rs +252, snake_anaconda Rs +251, snake_viper_wild Rs +240, benchmark_smallcap Rs +112, snake_viper_tick Rs +107, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -460

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.