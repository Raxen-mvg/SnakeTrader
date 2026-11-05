# Paper trading report

Updated 2026-11-05 15:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,640 | +7.82% | 0 | - | 236 |
| snake_abs_exit_conv | 213,896 | +6.95% | 1 | 100% | 255 |
| snake_abs_exit | 213,775 | +6.89% | 1 | 100% | 260 |
| benchmark | 213,724 | +6.86% | 0 | - | 237 |
| snake_abs | 210,779 | +5.39% | 1 | 100% | 255 |
| snake_abs_conv | 210,638 | +5.32% | 1 | 100% | 255 |
| intraweek | 209,973 | +4.99% | 25 | 48% | 2,757 |
| intramonth | 207,546 | +3.77% | 0 | - | 235 |
| snake_viper_wild | 204,677 | +2.34% | 3 | 33% | 702 |
| random_hold | 204,378 | +2.19% | 8 | 62% | 649 |
| oracle | 204,107 | +2.05% | 0 | - | 233 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,540 | +0.77% | 3 | 33% | 374 |
| snake_viper_tick | 201,159 | +0.58% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,935 | -0.53% | 0 | - | 237 |
| gold | 194,221 | -2.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,160 (-5.42%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,965 | +2.38% |
| gold | +2,828 | +1.48% |
| oracle | +2,315 | +1.15% |
| benchmark_smallcap | +2,264 | +1.15% |
| unified | +1,201 | +0.56% |
| random_hold | +1,069 | +0.53% |
| intramonth | +531 | +0.26% |
| intraweek | +275 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -1,119 | -0.52% |
| snake_abs_conv | -1,120 | -0.53% |
| snake_abs | -1,124 | -0.53% |
| snake_abs_exit | -1,125 | -0.52% |
| snake_anaconda | -2,280 | -1.12% |
| snake_viper_tick | -4,241 | -2.06% |
| snake_viper_wild | -4,353 | -2.08% |

Average per day so far: unified Rs +559, snake_abs_exit_conv Rs +556, snake_abs_exit Rs +551, benchmark Rs +490, snake_abs_conv Rs +426, snake_abs Rs +415, intraweek Rs +356, intramonth Rs +270, snake_viper_wild Rs +234, random_hold Rs +156, oracle Rs +147, snake_viper_tick Rs +68, snake_anaconda Rs +67, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -44, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.