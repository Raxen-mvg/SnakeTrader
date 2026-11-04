# Paper trading report

Updated 2026-11-04 14:40 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,120 | +7.06% | 0 | - | 236 |
| snake_abs_exit_conv | 213,889 | +6.94% | 1 | 100% | 255 |
| snake_abs_exit | 213,768 | +6.88% | 1 | 100% | 260 |
| snake_abs | 210,775 | +5.39% | 1 | 100% | 255 |
| snake_abs_conv | 210,632 | +5.32% | 1 | 100% | 255 |
| intraweek | 209,283 | +4.64% | 25 | 48% | 2,757 |
| benchmark | 208,537 | +4.27% | 0 | - | 237 |
| snake_viper_wild | 208,152 | +4.08% | 3 | 33% | 702 |
| intramonth | 206,477 | +3.24% | 0 | - | 235 |
| snake_viper_tick | 204,531 | +2.27% | 2 | 0% | 532 |
| random_hold | 202,727 | +1.36% | 8 | 62% | 649 |
| snake_anaconda | 202,724 | +1.36% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,044 | +0.52% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,300 | -1.85% | 0 | - | 237 |
| gold | 191,525 | -4.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,670 (-5.16%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,754 | +4.78% |
| snake_abs_exit_conv | +9,550 | +4.67% |
| snake_abs_conv | +9,491 | +4.72% |
| snake_abs | +9,466 | +4.70% |
| snake_anaconda | +8,899 | +4.59% |
| gold | +6,247 | +3.37% |
| intraweek | +4,197 | +2.05% |
| benchmark_smallcap | +3,363 | +1.74% |
| intramonth | +2,506 | +1.23% |
| random_hold | +2,259 | +1.13% |
| unified | +2,119 | +1.00% |
| benchmark | +1,836 | +0.89% |
| oracle | +1,054 | +0.53% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,636 | -1.27% |
| snake_viper_wild | -2,740 | -1.30% |

Average per day so far: snake_abs_exit_conv Rs +579, snake_abs_exit Rs +574, unified Rs +523, snake_abs_conv Rs +443, snake_abs Rs +431, snake_viper_wild Rs +429, intraweek Rs +344, benchmark Rs +316, snake_viper_tick Rs +283, intramonth Rs +240, snake_anaconda Rs +124, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -161, gold Rs -314, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.