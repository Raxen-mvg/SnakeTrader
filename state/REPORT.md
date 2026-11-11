# Paper trading report

Updated 2026-11-11 14:09 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,337 | +10.17% | 0 | - | 236 |
| benchmark | 220,257 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 216,668 | +8.33% | 2 | 50% | 345 |
| snake_abs_exit | 215,862 | +7.93% | 2 | 50% | 345 |
| snake_abs | 213,454 | +6.73% | 1 | 100% | 255 |
| intraweek | 213,378 | +6.69% | 30 | 53% | 3,302 |
| snake_abs_conv | 213,291 | +6.65% | 1 | 100% | 255 |
| oracle | 211,857 | +5.93% | 0 | - | 233 |
| intramonth | 211,351 | +5.68% | 0 | - | 235 |
| random_hold | 207,085 | +3.54% | 9 | 67% | 709 |
| snake_viper_wild | 205,089 | +2.54% | 10 | 50% | 1,825 |
| snake_anaconda | 203,635 | +1.82% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,590 | +0.80% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,031 | +0.52% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,750 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,161 (-4.42%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,659 | +3.88% |
| snake_viper_tick | +7,513 | +3.87% |
| snake_abs_exit_conv | +4,759 | +2.25% |
| snake_anaconda | +4,169 | +2.09% |
| snake_abs_exit | +3,878 | +1.83% |
| snake_abs_conv | +3,814 | +1.82% |
| snake_abs | +3,807 | +1.82% |
| benchmark_smallcap | +2,859 | +1.44% |
| benchmark | +2,165 | +0.99% |
| random_hold | +2,124 | +1.04% |
| oracle | +1,938 | +0.92% |
| intramonth | +742 | +0.35% |
| unified | +590 | +0.27% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,164 | -0.54% |
| gold | -2,384 | -1.24% |

Average per day so far: unified Rs +656, benchmark Rs +653, snake_abs_exit_conv Rs +595, snake_abs_exit Rs +567, snake_abs_conv Rs +475, snake_abs Rs +464, intraweek Rs +432, oracle Rs +382, intramonth Rs +366, random_hold Rs +229, snake_viper_wild Rs +221, snake_anaconda Rs +140, snake_viper_tick Rs +79, nifty_calls Rs +59, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -331, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.