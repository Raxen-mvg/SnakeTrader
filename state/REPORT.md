# Paper trading report

Updated 2026-11-05 13:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,509 | +8.75% | 0 | - | 236 |
| snake_abs_exit_conv | 213,784 | +6.89% | 1 | 100% | 255 |
| snake_abs_exit | 213,482 | +6.74% | 1 | 100% | 260 |
| benchmark | 213,181 | +6.59% | 0 | - | 237 |
| intraweek | 210,704 | +5.35% | 25 | 48% | 2,757 |
| snake_abs | 210,668 | +5.33% | 1 | 100% | 255 |
| snake_abs_conv | 210,532 | +5.27% | 1 | 100% | 255 |
| intramonth | 209,631 | +4.82% | 0 | - | 235 |
| snake_viper_wild | 206,239 | +3.12% | 3 | 33% | 702 |
| random_hold | 205,868 | +2.93% | 8 | 62% | 649 |
| oracle | 203,937 | +1.97% | 0 | - | 233 |
| snake_viper_tick | 202,691 | +1.35% | 2 | 0% | 532 |
| snake_anaconda | 201,867 | +0.93% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,170 | -0.41% | 0 | - | 237 |
| gold | 193,958 | -3.02% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,852 (-5.07%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,422 | +2.12% |
| unified | +3,069 | +1.43% |
| intramonth | +2,615 | +1.26% |
| gold | +2,565 | +1.34% |
| random_hold | +2,560 | +1.26% |
| benchmark_smallcap | +2,500 | +1.27% |
| oracle | +2,144 | +1.06% |
| intraweek | +1,006 | +0.48% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,226 | -0.58% |
| snake_abs_exit_conv | -1,231 | -0.57% |
| snake_abs | -1,235 | -0.58% |
| snake_abs_exit | -1,418 | -0.66% |
| snake_anaconda | -1,953 | -0.96% |
| snake_viper_tick | -2,709 | -1.32% |
| snake_viper_wild | -2,791 | -1.33% |

Average per day so far: unified Rs +625, snake_abs_exit_conv Rs +551, snake_abs_exit Rs +539, benchmark Rs +471, snake_abs_conv Rs +421, snake_abs Rs +410, intraweek Rs +382, intramonth Rs +344, snake_viper_wild Rs +312, random_hold Rs +210, snake_viper_tick Rs +158, oracle Rs +141, snake_anaconda Rs +81, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -216, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.