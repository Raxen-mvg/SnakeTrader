# Paper trading report

Updated 2026-11-05 09:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,257 | +8.63% | 0 | - | 236 |
| snake_abs_exit_conv | 216,715 | +8.36% | 1 | 100% | 255 |
| snake_abs_exit | 216,554 | +8.28% | 1 | 100% | 260 |
| snake_abs | 213,580 | +6.79% | 1 | 100% | 255 |
| snake_abs_conv | 213,438 | +6.72% | 1 | 100% | 255 |
| benchmark | 212,079 | +6.04% | 0 | - | 237 |
| intraweek | 209,855 | +4.93% | 25 | 48% | 2,757 |
| intramonth | 209,723 | +4.86% | 0 | - | 235 |
| snake_viper_wild | 206,250 | +3.12% | 3 | 33% | 702 |
| random_hold | 204,471 | +2.23% | 8 | 62% | 649 |
| oracle | 204,298 | +2.15% | 0 | - | 233 |
| snake_anaconda | 204,029 | +2.02% | 3 | 33% | 361 |
| snake_viper_tick | 202,722 | +1.36% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,800 | -0.60% | 0 | - | 237 |
| gold | 195,471 | -2.27% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,595 (-4.70%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,077 | +2.13% |
| benchmark | +3,320 | +1.59% |
| unified | +2,818 | +1.31% |
| intramonth | +2,708 | +1.31% |
| oracle | +2,506 | +1.24% |
| benchmark_smallcap | +2,130 | +1.08% |
| snake_abs_exit_conv | +1,700 | +0.79% |
| snake_abs_conv | +1,680 | +0.79% |
| snake_abs | +1,676 | +0.79% |
| snake_abs_exit | +1,654 | +0.77% |
| random_hold | +1,162 | +0.57% |
| snake_anaconda | +209 | +0.10% |
| intraweek | +157 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,678 | -1.30% |
| snake_viper_wild | -2,780 | -1.33% |

Average per day so far: snake_abs_exit_conv Rs +669, snake_abs_exit Rs +662, unified Rs +616, snake_abs_conv Rs +538, snake_abs Rs +522, benchmark Rs +431, intraweek Rs +352, intramonth Rs +347, snake_viper_wild Rs +312, snake_anaconda Rs +175, snake_viper_tick Rs +160, random_hold Rs +160, oracle Rs +154, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -50, gold Rs -162, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.