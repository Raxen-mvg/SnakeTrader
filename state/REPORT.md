# Paper trading report

Updated 2026-11-05 15:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,116 | +8.06% | 0 | - | 236 |
| snake_abs_exit_conv | 214,980 | +7.49% | 1 | 100% | 255 |
| snake_abs_exit | 214,802 | +7.40% | 1 | 100% | 260 |
| benchmark | 213,953 | +6.98% | 0 | - | 237 |
| snake_abs | 211,855 | +5.93% | 1 | 100% | 255 |
| snake_abs_conv | 211,717 | +5.86% | 1 | 100% | 255 |
| intraweek | 209,260 | +4.63% | 25 | 48% | 2,757 |
| intramonth | 208,025 | +4.01% | 0 | - | 235 |
| snake_viper_wild | 204,692 | +2.35% | 3 | 33% | 702 |
| random_hold | 204,580 | +2.29% | 8 | 62% | 649 |
| oracle | 204,145 | +2.07% | 0 | - | 233 |
| snake_anaconda | 202,757 | +1.38% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,176 | +0.59% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,733 | -0.63% | 0 | - | 237 |
| gold | 194,304 | -2.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,461 (-5.27%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,194 | +2.49% |
| gold | +2,910 | +1.52% |
| oracle | +2,353 | +1.17% |
| benchmark_smallcap | +2,063 | +1.05% |
| unified | +1,676 | +0.78% |
| random_hold | +1,271 | +0.62% |
| intramonth | +1,009 | +0.49% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -35 | -0.02% |
| snake_abs_conv | -41 | -0.02% |
| snake_abs | -48 | -0.02% |
| snake_abs_exit | -98 | -0.05% |
| intraweek | -437 | -0.21% |
| snake_anaconda | -1,063 | -0.52% |
| snake_viper_tick | -4,224 | -2.06% |
| snake_viper_wild | -4,338 | -2.08% |

Average per day so far: snake_abs_exit_conv Rs +599, snake_abs_exit Rs +592, unified Rs +576, benchmark Rs +498, snake_abs_conv Rs +469, snake_abs Rs +456, intraweek Rs +331, intramonth Rs +287, snake_viper_wild Rs +235, random_hold Rs +164, oracle Rs +148, snake_anaconda Rs +120, snake_viper_tick Rs +69, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -53, gold Rs -203, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.