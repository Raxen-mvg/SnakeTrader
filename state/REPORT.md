# Paper trading report

Updated 2026-11-05 14:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,966 | +7.98% | 0 | - | 236 |
| snake_abs_exit_conv | 214,743 | +7.37% | 1 | 100% | 255 |
| snake_abs_exit | 214,445 | +7.22% | 1 | 100% | 260 |
| benchmark | 213,992 | +7.00% | 0 | - | 237 |
| snake_abs | 211,627 | +5.81% | 1 | 100% | 255 |
| snake_abs_conv | 211,485 | +5.74% | 1 | 100% | 255 |
| intraweek | 209,869 | +4.93% | 25 | 48% | 2,757 |
| intramonth | 207,478 | +3.74% | 0 | - | 235 |
| snake_viper_wild | 205,502 | +2.75% | 3 | 33% | 702 |
| random_hold | 204,679 | +2.34% | 8 | 62% | 649 |
| oracle | 203,905 | +1.95% | 0 | - | 233 |
| snake_anaconda | 202,451 | +1.23% | 3 | 33% | 374 |
| snake_viper_tick | 201,970 | +0.98% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| gold | 194,484 | -2.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,558 (-5.22%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,233 | +2.51% |
| gold | +3,091 | +1.61% |
| benchmark_smallcap | +2,433 | +1.24% |
| oracle | +2,113 | +1.05% |
| unified | +1,527 | +0.71% |
| random_hold | +1,370 | +0.67% |
| intramonth | +463 | +0.22% |
| intraweek | +171 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -272 | -0.13% |
| snake_abs_conv | -273 | -0.13% |
| snake_abs | -277 | -0.13% |
| snake_abs_exit | -455 | -0.21% |
| snake_anaconda | -1,369 | -0.67% |
| snake_viper_tick | -3,430 | -1.67% |
| snake_viper_wild | -3,528 | -1.69% |

Average per day so far: snake_abs_exit_conv Rs +590, snake_abs_exit Rs +578, unified Rs +570, benchmark Rs +500, snake_abs_conv Rs +459, snake_abs Rs +447, intraweek Rs +352, snake_viper_wild Rs +275, intramonth Rs +267, random_hold Rs +167, oracle Rs +139, snake_viper_tick Rs +116, snake_anaconda Rs +107, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -197, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.