# Paper trading report

Updated 2026-11-04 12:19 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,742 | +6.87% | 0 | - | 236 |
| snake_abs_exit_conv | 210,835 | +5.42% | 1 | 100% | 255 |
| snake_abs_exit | 210,706 | +5.35% | 1 | 100% | 260 |
| intraweek | 208,447 | +4.22% | 25 | 48% | 2,757 |
| snake_abs | 207,745 | +3.87% | 1 | 100% | 255 |
| snake_abs_conv | 207,586 | +3.79% | 1 | 100% | 255 |
| benchmark | 207,260 | +3.63% | 0 | - | 237 |
| snake_viper_wild | 206,887 | +3.44% | 3 | 33% | 702 |
| intramonth | 206,096 | +3.05% | 0 | - | 235 |
| snake_viper_tick | 203,281 | +1.64% | 2 | 0% | 532 |
| random_hold | 202,719 | +1.36% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,102 | +0.55% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,235 | -0.38% | 3 | 33% | 361 |
| benchmark_smallcap | 194,473 | -2.76% | 0 | - | 237 |
| gold | 190,753 | -4.62% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,048 (-5.48%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +6,692 | +3.28% |
| snake_abs_exit_conv | +6,497 | +3.18% |
| snake_abs_conv | +6,445 | +3.20% |
| snake_abs | +6,436 | +3.20% |
| gold | +5,475 | +2.96% |
| snake_anaconda | +5,411 | +2.79% |
| intraweek | +3,362 | +1.64% |
| random_hold | +2,251 | +1.12% |
| intramonth | +2,125 | +1.04% |
| unified | +1,741 | +0.82% |
| benchmark_smallcap | +1,536 | +0.80% |
| oracle | +1,113 | +0.56% |
| benchmark | +558 | +0.27% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,886 | -1.88% |
| snake_viper_wild | -4,005 | -1.90% |

Average per day so far: unified Rs +509, snake_abs_exit_conv Rs +451, snake_abs_exit Rs +446, snake_viper_wild Rs +362, snake_abs_conv Rs +316, intraweek Rs +313, snake_abs Rs +310, benchmark Rs +269, intramonth Rs +226, snake_viper_tick Rs +205, random_hold Rs +101, nifty_calls Rs +68, oracle Rs +41, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -35, benchmark_smallcap Rs -240, gold Rs -342, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.