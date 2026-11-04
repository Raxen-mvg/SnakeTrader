# Paper trading report

Updated 2026-11-04 12:43 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,858 | +6.93% | 0 | - | 236 |
| snake_abs_exit_conv | 212,654 | +6.33% | 1 | 100% | 255 |
| snake_abs_exit | 212,508 | +6.25% | 1 | 100% | 260 |
| snake_abs | 209,555 | +4.78% | 1 | 100% | 255 |
| snake_abs_conv | 209,400 | +4.70% | 1 | 100% | 255 |
| intraweek | 209,375 | +4.69% | 25 | 48% | 2,757 |
| benchmark | 207,986 | +3.99% | 0 | - | 237 |
| snake_viper_wild | 207,037 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,213 | +3.11% | 0 | - | 235 |
| snake_viper_tick | 203,429 | +1.71% | 2 | 0% | 532 |
| random_hold | 202,869 | +1.44% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,181 | +0.59% | 0 | - | 233 |
| snake_anaconda | 201,067 | +0.53% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,157 | -2.42% | 0 | - | 237 |
| gold | 190,588 | -4.71% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,263 (-5.37%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,494 | +4.16% |
| snake_abs_exit_conv | +8,316 | +4.07% |
| snake_abs_conv | +8,259 | +4.11% |
| snake_abs | +8,246 | +4.10% |
| snake_anaconda | +7,243 | +3.74% |
| gold | +5,310 | +2.87% |
| intraweek | +4,290 | +2.09% |
| random_hold | +2,401 | +1.20% |
| intramonth | +2,242 | +1.10% |
| benchmark_smallcap | +2,220 | +1.15% |
| unified | +1,857 | +0.88% |
| benchmark | +1,285 | +0.62% |
| oracle | +1,191 | +0.60% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,738 | -1.80% |
| snake_viper_wild | -3,856 | -1.83% |

Average per day so far: snake_abs_exit_conv Rs +527, snake_abs_exit Rs +521, unified Rs +513, snake_abs_conv Rs +392, snake_abs Rs +382, snake_viper_wild Rs +370, intraweek Rs +347, benchmark Rs +296, intramonth Rs +230, snake_viper_tick Rs +214, random_hold Rs +106, nifty_calls Rs +68, snake_anaconda Rs +49, oracle Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -211, gold Rs -349, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.