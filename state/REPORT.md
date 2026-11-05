# Paper trading report

Updated 2026-11-05 12:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,390 | +8.70% | 0 | - | 236 |
| snake_abs_exit_conv | 213,487 | +6.74% | 1 | 100% | 255 |
| snake_abs_exit | 213,178 | +6.59% | 1 | 100% | 260 |
| benchmark | 213,074 | +6.54% | 0 | - | 237 |
| intraweek | 210,724 | +5.36% | 25 | 48% | 2,757 |
| snake_abs | 210,377 | +5.19% | 1 | 100% | 255 |
| snake_abs_conv | 210,238 | +5.12% | 1 | 100% | 255 |
| intramonth | 209,286 | +4.64% | 0 | - | 235 |
| snake_viper_wild | 206,309 | +3.15% | 3 | 33% | 702 |
| random_hold | 205,969 | +2.98% | 8 | 62% | 649 |
| oracle | 203,975 | +1.99% | 0 | - | 233 |
| snake_viper_tick | 202,763 | +1.38% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,622 | +0.81% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,979 | -0.51% | 0 | - | 237 |
| gold | 194,287 | -2.86% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,739 (-5.13%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,315 | +2.07% |
| unified | +2,951 | +1.38% |
| gold | +2,893 | +1.51% |
| random_hold | +2,660 | +1.31% |
| benchmark_smallcap | +2,309 | +1.17% |
| intramonth | +2,270 | +1.10% |
| oracle | +2,183 | +1.08% |
| intraweek | +1,026 | +0.49% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,520 | -0.72% |
| snake_abs | -1,526 | -0.72% |
| snake_abs_exit_conv | -1,528 | -0.71% |
| snake_abs_exit | -1,723 | -0.80% |
| snake_anaconda | -2,198 | -1.08% |
| snake_viper_tick | -2,637 | -1.28% |
| snake_viper_wild | -2,721 | -1.30% |

Average per day so far: unified Rs +621, snake_abs_exit_conv Rs +539, snake_abs_exit Rs +527, benchmark Rs +467, snake_abs_conv Rs +410, snake_abs Rs +399, intraweek Rs +383, intramonth Rs +332, snake_viper_wild Rs +315, random_hold Rs +213, snake_viper_tick Rs +163, oracle Rs +142, snake_anaconda Rs +71, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -204, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.