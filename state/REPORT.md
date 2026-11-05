# Paper trading report

Updated 2026-11-05 13:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,379 | +8.69% | 0 | - | 236 |
| snake_abs_exit_conv | 213,806 | +6.90% | 1 | 100% | 255 |
| snake_abs_exit | 213,501 | +6.75% | 1 | 100% | 260 |
| benchmark | 213,181 | +6.59% | 0 | - | 237 |
| intraweek | 210,705 | +5.35% | 25 | 48% | 2,757 |
| snake_abs | 210,689 | +5.34% | 1 | 100% | 255 |
| snake_abs_conv | 210,555 | +5.28% | 1 | 100% | 255 |
| intramonth | 209,403 | +4.70% | 0 | - | 235 |
| snake_viper_wild | 206,387 | +3.19% | 3 | 33% | 702 |
| random_hold | 205,839 | +2.92% | 8 | 62% | 649 |
| oracle | 203,804 | +1.90% | 0 | - | 233 |
| snake_viper_tick | 202,840 | +1.42% | 2 | 0% | 532 |
| snake_anaconda | 202,021 | +1.01% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,957 | -0.52% | 0 | - | 237 |
| gold | 193,942 | -3.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,852 (-5.07%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,422 | +2.12% |
| unified | +2,939 | +1.37% |
| gold | +2,548 | +1.33% |
| random_hold | +2,530 | +1.24% |
| intramonth | +2,387 | +1.15% |
| benchmark_smallcap | +2,287 | +1.16% |
| oracle | +2,012 | +1.00% |
| intraweek | +1,007 | +0.48% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,204 | -0.57% |
| snake_abs_exit_conv | -1,209 | -0.56% |
| snake_abs | -1,214 | -0.57% |
| snake_abs_exit | -1,399 | -0.65% |
| snake_anaconda | -1,799 | -0.88% |
| snake_viper_tick | -2,561 | -1.25% |
| snake_viper_wild | -2,643 | -1.26% |

Average per day so far: unified Rs +621, snake_abs_exit_conv Rs +552, snake_abs_exit Rs +540, benchmark Rs +471, snake_abs_conv Rs +422, snake_abs Rs +411, intraweek Rs +382, intramonth Rs +336, snake_viper_wild Rs +319, random_hold Rs +209, snake_viper_tick Rs +167, oracle Rs +136, snake_anaconda Rs +88, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -216, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.