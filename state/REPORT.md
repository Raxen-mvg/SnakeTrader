# Paper trading report

Updated 2026-11-11 12:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,877 | +10.44% | 0 | - | 237 |
| unified | 220,671 | +10.34% | 0 | - | 236 |
| snake_abs_exit_conv | 216,137 | +8.07% | 2 | 50% | 345 |
| snake_abs_exit | 214,956 | +7.48% | 2 | 50% | 345 |
| intraweek | 214,202 | +7.10% | 30 | 53% | 3,302 |
| snake_abs | 212,454 | +6.23% | 1 | 100% | 255 |
| snake_abs_conv | 212,301 | +6.15% | 1 | 100% | 255 |
| oracle | 212,036 | +6.02% | 0 | - | 233 |
| intramonth | 211,665 | +5.83% | 0 | - | 235 |
| random_hold | 207,074 | +3.54% | 9 | 67% | 709 |
| snake_anaconda | 202,773 | +1.39% | 3 | 33% | 374 |
| snake_viper_wild | 202,518 | +1.26% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,759 | +0.88% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,072 | -0.46% | 9 | 44% | 1,639 |
| gold | 189,963 | -5.02% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,364 (-4.32%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +5,088 | +2.58% |
| snake_viper_tick | +4,995 | +2.57% |
| snake_abs_exit_conv | +4,228 | +2.00% |
| benchmark_smallcap | +3,587 | +1.81% |
| snake_anaconda | +3,307 | +1.66% |
| snake_abs_exit | +2,972 | +1.40% |
| snake_abs_conv | +2,823 | +1.35% |
| snake_abs | +2,807 | +1.34% |
| benchmark | +2,785 | +1.28% |
| oracle | +2,118 | +1.01% |
| random_hold | +2,113 | +1.03% |
| intramonth | +1,056 | +0.50% |
| unified | +924 | +0.42% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -340 | -0.16% |
| gold | -2,170 | -1.13% |

Average per day so far: benchmark Rs +673, unified Rs +667, snake_abs_exit_conv Rs +576, snake_abs_exit Rs +534, intraweek Rs +458, snake_abs_conv Rs +439, snake_abs Rs +429, oracle Rs +388, intramonth Rs +376, random_hold Rs +228, snake_viper_wild Rs +109, snake_anaconda Rs +107, benchmark_smallcap Rs +65, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -46, gold Rs -324, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.