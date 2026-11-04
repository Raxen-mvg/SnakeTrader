# Paper trading report

Updated 2026-11-04 14:31 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,456 | +7.23% | 0 | - | 236 |
| snake_abs_exit_conv | 213,864 | +6.93% | 1 | 100% | 255 |
| snake_abs_exit | 213,732 | +6.87% | 1 | 100% | 260 |
| snake_abs | 210,742 | +5.37% | 1 | 100% | 255 |
| snake_abs_conv | 210,604 | +5.30% | 1 | 100% | 255 |
| intraweek | 209,978 | +4.99% | 25 | 48% | 2,757 |
| benchmark | 208,529 | +4.26% | 0 | - | 237 |
| snake_viper_wild | 207,625 | +3.81% | 3 | 33% | 702 |
| intramonth | 206,837 | +3.42% | 0 | - | 235 |
| snake_viper_tick | 204,003 | +2.00% | 2 | 0% | 532 |
| random_hold | 203,010 | +1.50% | 8 | 62% | 649 |
| snake_anaconda | 202,685 | +1.34% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,037 | +0.52% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,244 | -1.88% | 0 | - | 237 |
| gold | 191,246 | -4.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,730 (-5.13%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,717 | +4.76% |
| snake_abs_exit_conv | +9,526 | +4.66% |
| snake_abs_conv | +9,463 | +4.70% |
| snake_abs | +9,433 | +4.69% |
| snake_anaconda | +8,861 | +4.57% |
| gold | +5,968 | +3.22% |
| intraweek | +4,892 | +2.38% |
| benchmark_smallcap | +3,307 | +1.71% |
| intramonth | +2,866 | +1.41% |
| random_hold | +2,542 | +1.27% |
| unified | +2,455 | +1.16% |
| benchmark | +1,828 | +0.89% |
| oracle | +1,047 | +0.52% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,164 | -1.53% |
| snake_viper_wild | -3,268 | -1.55% |

Average per day so far: snake_abs_exit_conv Rs +578, snake_abs_exit Rs +572, unified Rs +535, snake_abs_conv Rs +442, snake_abs Rs +430, snake_viper_wild Rs +401, intraweek Rs +370, benchmark Rs +316, intramonth Rs +253, snake_viper_tick Rs +250, snake_anaconda Rs +122, random_hold Rs +111, nifty_calls Rs +68, oracle Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -163, gold Rs -324, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.