# Paper trading report

Updated 2026-11-13 10:04 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,025 | +10.51% | 0 | - | 236 |
| benchmark | 219,806 | +9.90% | 0 | - | 237 |
| snake_abs_exit_conv | 217,508 | +8.75% | 2 | 50% | 345 |
| snake_abs_exit | 216,953 | +8.48% | 2 | 50% | 345 |
| intraweek | 214,805 | +7.40% | 30 | 53% | 3,302 |
| oracle | 214,187 | +7.09% | 0 | - | 233 |
| snake_abs | 213,618 | +6.81% | 1 | 100% | 255 |
| snake_abs_conv | 213,454 | +6.73% | 1 | 100% | 255 |
| intramonth | 211,692 | +5.85% | 0 | - | 235 |
| random_hold | 207,607 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 205,448 | +2.72% | 14 | 50% | 2,496 |
| snake_anaconda | 205,350 | +2.67% | 3 | 33% | 374 |
| benchmark_smallcap | 203,744 | +1.87% | 0 | - | 237 |
| snake_viper_tick | 201,935 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,275 | -7.86% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,107 (-3.95%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,071 | +0.50% |
| benchmark_smallcap | +538 | +0.27% |
| unified | +328 | +0.15% |
| snake_viper_wild | +155 | +0.08% |
| snake_viper_tick | +153 | +0.08% |
| intraweek | +146 | +0.07% |
| intramonth | +99 | +0.05% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -447 | -0.21% |
| snake_abs_exit | -490 | -0.23% |
| snake_anaconda | -577 | -0.28% |
| benchmark | -742 | -0.34% |
| gold | -1,036 | -0.56% |
| snake_abs_exit_conv | -1,166 | -0.53% |
| snake_abs_conv | -2,081 | -0.96% |
| snake_abs | -2,094 | -0.97% |

Average per day so far: unified Rs +637, benchmark Rs +600, snake_abs_exit_conv Rs +584, snake_abs_exit Rs +565, intraweek Rs +449, snake_abs_conv Rs +448, snake_abs Rs +439, oracle Rs +430, intramonth Rs +354, random_hold Rs +231, snake_viper_wild Rs +218, snake_anaconda Rs +191, benchmark_smallcap Rs +129, snake_viper_tick Rs +88, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -477

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.