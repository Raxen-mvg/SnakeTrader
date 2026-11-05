# Paper trading report

Updated 2026-11-05 14:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,041 | +8.02% | 0 | - | 236 |
| snake_abs_exit_conv | 214,357 | +7.18% | 1 | 100% | 255 |
| snake_abs_exit | 214,100 | +7.05% | 1 | 100% | 260 |
| benchmark | 213,724 | +6.86% | 0 | - | 237 |
| snake_abs | 211,254 | +5.63% | 1 | 100% | 255 |
| snake_abs_conv | 211,105 | +5.55% | 1 | 100% | 255 |
| intraweek | 210,425 | +5.21% | 25 | 48% | 2,757 |
| intramonth | 207,633 | +3.82% | 0 | - | 235 |
| snake_viper_wild | 205,445 | +2.72% | 3 | 33% | 702 |
| random_hold | 204,894 | +2.45% | 8 | 62% | 649 |
| oracle | 203,958 | +1.98% | 0 | - | 233 |
| snake_anaconda | 202,114 | +1.06% | 3 | 33% | 374 |
| snake_viper_tick | 201,913 | +0.96% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| gold | 194,254 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,547 (-5.23%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,965 | +2.38% |
| gold | +2,861 | +1.50% |
| benchmark_smallcap | +2,433 | +1.24% |
| oracle | +2,166 | +1.07% |
| unified | +1,601 | +0.75% |
| random_hold | +1,585 | +0.78% |
| intraweek | +727 | +0.35% |
| intramonth | +617 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -650 | -0.31% |
| snake_abs_conv | -653 | -0.31% |
| snake_abs_exit_conv | -658 | -0.31% |
| snake_abs_exit | -800 | -0.37% |
| snake_anaconda | -1,706 | -0.84% |
| snake_viper_tick | -3,488 | -1.70% |
| snake_viper_wild | -3,585 | -1.72% |

Average per day so far: snake_abs_exit_conv Rs +574, unified Rs +573, snake_abs_exit Rs +564, benchmark Rs +490, snake_abs_conv Rs +444, snake_abs Rs +433, intraweek Rs +372, intramonth Rs +273, snake_viper_wild Rs +272, random_hold Rs +175, oracle Rs +141, snake_viper_tick Rs +113, snake_anaconda Rs +92, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.