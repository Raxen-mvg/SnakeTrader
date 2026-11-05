# Paper trading report

Updated 2026-11-05 14:26 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,102 | +8.05% | 0 | - | 236 |
| snake_abs_exit_conv | 214,472 | +7.24% | 1 | 100% | 255 |
| snake_abs_exit | 214,212 | +7.11% | 1 | 100% | 260 |
| benchmark | 213,686 | +6.84% | 0 | - | 237 |
| snake_abs | 211,367 | +5.68% | 1 | 100% | 255 |
| snake_abs_conv | 211,218 | +5.61% | 1 | 100% | 255 |
| intraweek | 210,334 | +5.17% | 25 | 48% | 2,757 |
| intramonth | 207,654 | +3.83% | 0 | - | 235 |
| snake_viper_wild | 205,502 | +2.75% | 3 | 33% | 702 |
| random_hold | 205,024 | +2.51% | 8 | 62% | 649 |
| oracle | 203,888 | +1.94% | 0 | - | 233 |
| snake_anaconda | 202,133 | +1.07% | 3 | 33% | 374 |
| snake_viper_tick | 201,970 | +0.98% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,024 | -0.49% | 0 | - | 237 |
| gold | 194,287 | -2.86% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,585 (-5.21%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,927 | +2.36% |
| gold | +2,893 | +1.51% |
| benchmark_smallcap | +2,354 | +1.20% |
| oracle | +2,095 | +1.04% |
| random_hold | +1,716 | +0.84% |
| unified | +1,662 | +0.78% |
| intramonth | +638 | +0.31% |
| intraweek | +636 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -536 | -0.25% |
| snake_abs_conv | -540 | -0.26% |
| snake_abs_exit_conv | -543 | -0.25% |
| snake_abs_exit | -688 | -0.32% |
| snake_anaconda | -1,688 | -0.83% |
| snake_viper_tick | -3,430 | -1.67% |
| snake_viper_wild | -3,528 | -1.69% |

Average per day so far: snake_abs_exit_conv Rs +579, unified Rs +575, snake_abs_exit Rs +568, benchmark Rs +489, snake_abs_conv Rs +449, snake_abs Rs +437, intraweek Rs +369, snake_viper_wild Rs +275, intramonth Rs +273, random_hold Rs +179, oracle Rs +139, snake_viper_tick Rs +116, snake_anaconda Rs +93, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -41, gold Rs -204, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.