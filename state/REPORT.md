# Paper trading report

Updated 2026-11-05 14:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,261 | +8.13% | 0 | - | 236 |
| snake_abs_exit_conv | 214,583 | +7.29% | 1 | 100% | 255 |
| snake_abs_exit | 214,296 | +7.15% | 1 | 100% | 260 |
| benchmark | 214,053 | +7.03% | 0 | - | 237 |
| snake_abs | 211,471 | +5.74% | 1 | 100% | 255 |
| snake_abs_conv | 211,325 | +5.66% | 1 | 100% | 255 |
| intraweek | 209,951 | +4.97% | 25 | 48% | 2,757 |
| intramonth | 208,176 | +4.09% | 0 | - | 235 |
| snake_viper_wild | 205,429 | +2.71% | 3 | 33% | 702 |
| random_hold | 204,710 | +2.35% | 8 | 62% | 649 |
| oracle | 204,456 | +2.23% | 0 | - | 233 |
| snake_anaconda | 202,114 | +1.06% | 3 | 33% | 374 |
| snake_viper_tick | 201,899 | +0.95% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,192 | -0.40% | 0 | - | 237 |
| gold | 194,320 | -2.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,594 (-5.20%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,294 | +2.54% |
| gold | +2,926 | +1.53% |
| oracle | +2,664 | +1.32% |
| benchmark_smallcap | +2,522 | +1.28% |
| unified | +1,822 | +0.85% |
| random_hold | +1,401 | +0.69% |
| intramonth | +1,160 | +0.56% |
| intraweek | +253 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -432 | -0.20% |
| snake_abs | -432 | -0.20% |
| snake_abs_conv | -433 | -0.20% |
| snake_abs_exit | -605 | -0.28% |
| snake_anaconda | -1,706 | -0.84% |
| snake_viper_tick | -3,502 | -1.71% |
| snake_viper_wild | -3,601 | -1.72% |

Average per day so far: snake_abs_exit_conv Rs +583, unified Rs +581, snake_abs_exit Rs +572, benchmark Rs +502, snake_abs_conv Rs +453, snake_abs Rs +441, intraweek Rs +355, intramonth Rs +292, snake_viper_wild Rs +271, random_hold Rs +168, oracle Rs +159, snake_viper_tick Rs +112, snake_anaconda Rs +92, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, gold Rs -203, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.