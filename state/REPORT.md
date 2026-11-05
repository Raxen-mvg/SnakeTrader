# Paper trading report

Updated 2026-11-05 15:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,942 | +7.97% | 0 | - | 236 |
| snake_abs_exit_conv | 213,820 | +6.91% | 1 | 100% | 255 |
| snake_abs_exit | 213,680 | +6.84% | 1 | 100% | 260 |
| benchmark | 213,410 | +6.71% | 0 | - | 237 |
| snake_abs | 210,717 | +5.36% | 1 | 100% | 255 |
| snake_abs_conv | 210,566 | +5.28% | 1 | 100% | 255 |
| intraweek | 209,685 | +4.84% | 25 | 48% | 2,757 |
| intramonth | 208,050 | +4.03% | 0 | - | 235 |
| snake_viper_wild | 205,025 | +2.51% | 3 | 33% | 702 |
| random_hold | 204,488 | +2.24% | 8 | 62% | 649 |
| oracle | 204,090 | +2.04% | 0 | - | 233 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,499 | +0.75% | 2 | 0% | 532 |
| snake_anaconda | 201,398 | +0.70% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,867 | -0.57% | 0 | - | 237 |
| gold | 194,090 | -2.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,216 (-5.39%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,651 | +2.23% |
| gold | +2,696 | +1.41% |
| oracle | +2,298 | +1.14% |
| benchmark_smallcap | +2,197 | +1.12% |
| unified | +1,503 | +0.70% |
| random_hold | +1,180 | +0.58% |
| intramonth | +1,034 | +0.50% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -13 | -0.01% |
| snake_abs | -1,186 | -0.56% |
| snake_abs_conv | -1,192 | -0.56% |
| snake_abs_exit_conv | -1,195 | -0.56% |
| snake_abs_exit | -1,220 | -0.57% |
| snake_anaconda | -2,422 | -1.19% |
| snake_viper_tick | -3,901 | -1.90% |
| snake_viper_wild | -4,005 | -1.92% |

Average per day so far: unified Rs +569, snake_abs_exit_conv Rs +553, snake_abs_exit Rs +547, benchmark Rs +479, snake_abs_conv Rs +423, snake_abs Rs +412, intraweek Rs +346, intramonth Rs +287, snake_viper_wild Rs +251, random_hold Rs +160, oracle Rs +146, snake_viper_tick Rs +88, nifty_calls Rs +66, snake_anaconda Rs +61, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -47, gold Rs -211, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.