# Paper trading report

Updated 2026-11-05 14:15 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,996 | +8.00% | 0 | - | 236 |
| snake_abs_exit_conv | 214,606 | +7.30% | 1 | 100% | 255 |
| snake_abs_exit | 214,366 | +7.18% | 1 | 100% | 260 |
| benchmark | 214,037 | +7.02% | 0 | - | 237 |
| snake_abs | 211,493 | +5.75% | 1 | 100% | 255 |
| snake_abs_conv | 211,354 | +5.68% | 1 | 100% | 255 |
| intraweek | 210,455 | +5.23% | 25 | 48% | 2,757 |
| intramonth | 207,454 | +3.73% | 0 | - | 235 |
| snake_viper_wild | 205,571 | +2.79% | 3 | 33% | 702 |
| random_hold | 205,014 | +2.51% | 8 | 62% | 649 |
| oracle | 203,858 | +1.93% | 0 | - | 233 |
| snake_anaconda | 202,716 | +1.36% | 3 | 33% | 374 |
| snake_viper_tick | 202,036 | +1.02% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,766 | +0.88% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| gold | 194,271 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,632 (-5.18%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,278 | +2.53% |
| gold | +2,877 | +1.50% |
| benchmark_smallcap | +2,477 | +1.26% |
| oracle | +2,065 | +1.02% |
| random_hold | +1,706 | +0.84% |
| unified | +1,556 | +0.73% |
| intraweek | +757 | +0.36% |
| intramonth | +438 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -405 | -0.19% |
| snake_abs_exit_conv | -408 | -0.19% |
| snake_abs | -410 | -0.19% |
| snake_abs_exit | -534 | -0.25% |
| snake_anaconda | -1,105 | -0.54% |
| snake_viper_tick | -3,364 | -1.64% |
| snake_viper_wild | -3,459 | -1.66% |

Average per day so far: snake_abs_exit_conv Rs +584, snake_abs_exit Rs +575, unified Rs +571, benchmark Rs +501, snake_abs_conv Rs +454, snake_abs Rs +442, intraweek Rs +373, snake_viper_wild Rs +279, intramonth Rs +266, random_hold Rs +179, oracle Rs +138, snake_viper_tick Rs +120, snake_anaconda Rs +118, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.