# Paper trading report

Updated 2026-11-05 12:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,263 | +8.63% | 0 | - | 236 |
| snake_abs_exit_conv | 213,481 | +6.74% | 1 | 100% | 255 |
| snake_abs_exit | 213,179 | +6.59% | 1 | 100% | 260 |
| benchmark | 213,005 | +6.50% | 0 | - | 237 |
| intraweek | 210,742 | +5.37% | 25 | 48% | 2,757 |
| snake_abs | 210,372 | +5.19% | 1 | 100% | 255 |
| snake_abs_conv | 210,233 | +5.12% | 1 | 100% | 255 |
| intramonth | 209,465 | +4.73% | 0 | - | 235 |
| snake_viper_wild | 206,165 | +3.08% | 3 | 33% | 702 |
| random_hold | 205,710 | +2.85% | 8 | 62% | 649 |
| oracle | 203,925 | +1.96% | 0 | - | 233 |
| snake_viper_tick | 202,618 | +1.31% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,568 | +0.78% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,136 | -0.43% | 0 | - | 237 |
| gold | 193,925 | -3.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,714 (-5.14%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,246 | +2.03% |
| unified | +2,824 | +1.32% |
| gold | +2,532 | +1.32% |
| benchmark_smallcap | +2,466 | +1.25% |
| intramonth | +2,450 | +1.18% |
| random_hold | +2,401 | +1.18% |
| oracle | +2,133 | +1.06% |
| intraweek | +1,044 | +0.50% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,526 | -0.72% |
| snake_abs | -1,531 | -0.72% |
| snake_abs_exit_conv | -1,534 | -0.71% |
| snake_abs_exit | -1,721 | -0.80% |
| snake_anaconda | -2,252 | -1.10% |
| snake_viper_tick | -2,783 | -1.35% |
| snake_viper_wild | -2,865 | -1.37% |

Average per day so far: unified Rs +617, snake_abs_exit_conv Rs +539, snake_abs_exit Rs +527, benchmark Rs +464, snake_abs_conv Rs +409, snake_abs Rs +399, intraweek Rs +384, intramonth Rs +338, snake_viper_wild Rs +308, random_hold Rs +204, snake_viper_tick Rs +154, oracle Rs +140, snake_anaconda Rs +68, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -217, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.