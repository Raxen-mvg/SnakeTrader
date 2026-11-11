# Paper trading report

Updated 2026-11-11 12:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,030 | +10.52% | 0 | - | 237 |
| unified | 220,464 | +10.23% | 0 | - | 236 |
| snake_abs_exit_conv | 216,027 | +8.01% | 2 | 50% | 345 |
| snake_abs_exit | 214,844 | +7.42% | 2 | 50% | 345 |
| intraweek | 214,274 | +7.14% | 30 | 53% | 3,302 |
| snake_abs | 212,476 | +6.24% | 1 | 100% | 255 |
| snake_abs_conv | 212,319 | +6.16% | 1 | 100% | 255 |
| oracle | 211,881 | +5.94% | 0 | - | 233 |
| intramonth | 211,408 | +5.70% | 0 | - | 235 |
| random_hold | 206,850 | +3.42% | 9 | 67% | 709 |
| snake_anaconda | 202,692 | +1.35% | 3 | 33% | 374 |
| snake_viper_wild | 201,895 | +0.95% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,748 | +0.87% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 198,463 | -0.77% | 9 | 44% | 1,639 |
| gold | 189,832 | -5.08% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,263 (-4.37%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +4,465 | +2.26% |
| snake_viper_tick | +4,387 | +2.26% |
| snake_abs_exit_conv | +4,118 | +1.94% |
| benchmark_smallcap | +3,576 | +1.80% |
| snake_anaconda | +3,225 | +1.62% |
| benchmark | +2,938 | +1.35% |
| snake_abs_exit | +2,860 | +1.35% |
| snake_abs_conv | +2,841 | +1.36% |
| snake_abs | +2,830 | +1.35% |
| oracle | +1,963 | +0.94% |
| random_hold | +1,890 | +0.92% |
| intramonth | +798 | +0.38% |
| unified | +717 | +0.33% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -268 | -0.12% |
| gold | -2,302 | -1.20% |

Average per day so far: benchmark Rs +678, unified Rs +660, snake_abs_exit_conv Rs +572, snake_abs_exit Rs +530, intraweek Rs +460, snake_abs_conv Rs +440, snake_abs Rs +430, oracle Rs +383, intramonth Rs +368, random_hold Rs +221, snake_anaconda Rs +104, snake_viper_wild Rs +82, benchmark_smallcap Rs +65, nifty_calls Rs +59, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -77, gold Rs -328, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.