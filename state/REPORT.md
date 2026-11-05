# Paper trading report

Updated 2026-11-05 12:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,874 | +8.94% | 0 | - | 236 |
| snake_abs_exit_conv | 213,657 | +6.83% | 1 | 100% | 255 |
| snake_abs_exit | 213,349 | +6.67% | 1 | 100% | 260 |
| benchmark | 212,959 | +6.48% | 0 | - | 237 |
| intraweek | 211,404 | +5.70% | 25 | 48% | 2,757 |
| snake_abs | 210,544 | +5.27% | 1 | 100% | 255 |
| snake_abs_conv | 210,408 | +5.20% | 1 | 100% | 255 |
| intramonth | 209,593 | +4.80% | 0 | - | 235 |
| random_hold | 206,482 | +3.24% | 8 | 62% | 649 |
| snake_viper_wild | 206,407 | +3.20% | 3 | 33% | 702 |
| oracle | 203,892 | +1.95% | 0 | - | 233 |
| snake_viper_tick | 202,858 | +1.43% | 2 | 0% | 532 |
| snake_anaconda | 201,858 | +0.93% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,957 | -0.52% | 0 | - | 237 |
| gold | 194,123 | -2.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,998 (-5.00%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,200 | +2.01% |
| unified | +3,434 | +1.60% |
| random_hold | +3,173 | +1.56% |
| gold | +2,729 | +1.43% |
| intramonth | +2,577 | +1.25% |
| benchmark_smallcap | +2,287 | +1.16% |
| oracle | +2,100 | +1.04% |
| intraweek | +1,706 | +0.81% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,350 | -0.64% |
| snake_abs_exit_conv | -1,358 | -0.63% |
| snake_abs | -1,359 | -0.64% |
| snake_abs_exit | -1,551 | -0.72% |
| snake_anaconda | -1,962 | -0.96% |
| snake_viper_tick | -2,543 | -1.24% |
| snake_viper_wild | -2,623 | -1.25% |

Average per day so far: unified Rs +638, snake_abs_exit_conv Rs +546, snake_abs_exit Rs +534, benchmark Rs +463, snake_abs_conv Rs +416, intraweek Rs +407, snake_abs Rs +406, intramonth Rs +343, snake_viper_wild Rs +320, random_hold Rs +232, snake_viper_tick Rs +168, oracle Rs +139, snake_anaconda Rs +81, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.