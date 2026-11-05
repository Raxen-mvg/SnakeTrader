# Paper trading report

Updated 2026-11-05 12:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,012 | +9.01% | 0 | - | 236 |
| snake_abs_exit_conv | 213,783 | +6.89% | 1 | 100% | 255 |
| snake_abs_exit | 213,476 | +6.74% | 1 | 100% | 260 |
| benchmark | 212,653 | +6.33% | 0 | - | 237 |
| intraweek | 210,953 | +5.48% | 25 | 48% | 2,757 |
| snake_abs | 210,670 | +5.33% | 1 | 100% | 255 |
| snake_abs_conv | 210,535 | +5.27% | 1 | 100% | 255 |
| intramonth | 209,909 | +4.95% | 0 | - | 235 |
| snake_viper_wild | 206,771 | +3.38% | 3 | 33% | 702 |
| random_hold | 206,650 | +3.33% | 8 | 62% | 649 |
| oracle | 204,138 | +2.07% | 0 | - | 233 |
| snake_viper_tick | 203,214 | +1.61% | 2 | 0% | 532 |
| snake_anaconda | 202,045 | +1.02% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,114 | -0.44% | 0 | - | 237 |
| gold | 194,304 | -2.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,060 (-4.97%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,894 | +1.86% |
| unified | +3,572 | +1.67% |
| random_hold | +3,341 | +1.64% |
| gold | +2,910 | +1.52% |
| intramonth | +2,893 | +1.40% |
| benchmark_smallcap | +2,444 | +1.24% |
| oracle | +2,346 | +1.16% |
| intraweek | +1,255 | +0.60% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,223 | -0.58% |
| snake_abs_exit_conv | -1,231 | -0.57% |
| snake_abs | -1,233 | -0.58% |
| snake_abs_exit | -1,425 | -0.66% |
| snake_anaconda | -1,775 | -0.87% |
| snake_viper_tick | -2,186 | -1.06% |
| snake_viper_wild | -2,259 | -1.08% |

Average per day so far: unified Rs +643, snake_abs_exit_conv Rs +551, snake_abs_exit Rs +539, benchmark Rs +452, snake_abs_conv Rs +421, snake_abs Rs +410, intraweek Rs +391, intramonth Rs +354, snake_viper_wild Rs +339, random_hold Rs +238, snake_viper_tick Rs +189, oracle Rs +148, snake_anaconda Rs +89, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -203, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.