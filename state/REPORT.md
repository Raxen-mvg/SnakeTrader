# Paper trading report

Updated 2026-11-18 14:42 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,220 | +11.11% | 0 | - | 236 |
| benchmark | 220,326 | +10.16% | 0 | - | 237 |
| snake_abs_exit | 214,309 | +7.16% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,659 | +6.33% | 2 | 50% | 345 |
| intramonth | 211,861 | +5.93% | 0 | - | 235 |
| intraweek | 211,732 | +5.87% | 35 | 54% | 3,851 |
| oracle | 211,508 | +5.75% | 0 | - | 233 |
| snake_abs | 209,778 | +4.89% | 1 | 100% | 255 |
| snake_abs_conv | 209,667 | +4.83% | 1 | 100% | 255 |
| snake_viper_wild | 207,198 | +3.60% | 16 | 50% | 2,827 |
| random_hold | 206,865 | +3.43% | 10 | 70% | 733 |
| snake_anaconda | 204,602 | +2.30% | 3 | 33% | 374 |
| snake_viper_tick | 203,658 | +1.83% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,222 | -11.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,695 (-4.65%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,248 | +0.60% |
| snake_abs | +1,219 | +0.58% |
| snake_abs_exit | +1,167 | +0.55% |
| snake_abs_exit_conv | +1,086 | +0.51% |
| unified | +781 | +0.35% |
| snake_anaconda | +547 | +0.27% |
| intramonth | +319 | +0.15% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -979 | -0.46% |
| benchmark_smallcap | -1,020 | -0.51% |
| benchmark | -1,278 | -0.58% |
| random_hold | -1,567 | -0.75% |
| intraweek | -1,590 | -0.75% |
| snake_viper_tick | -2,178 | -1.06% |
| snake_viper_wild | -2,217 | -1.06% |
| gold | -3,502 | -1.94% |

Average per day so far: unified Rs +617, benchmark Rs +565, snake_abs_exit Rs +434, snake_abs_exit_conv Rs +384, intramonth Rs +329, intraweek Rs +326, oracle Rs +320, snake_abs_conv Rs +293, snake_abs Rs +288, snake_viper_wild Rs +257, random_hold Rs +191, snake_anaconda Rs +148, snake_viper_tick Rs +146, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -14, snake_nonews Rs -326, snake Rs -347, gold Rs -633

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.