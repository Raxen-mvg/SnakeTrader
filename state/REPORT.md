# Paper trading report

Updated 2026-11-26 10:48 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,155 | +13.08% | 0 | - | 237 |
| unified | 223,549 | +11.78% | 0 | - | 236 |
| oracle | 212,857 | +6.43% | 0 | - | 233 |
| intramonth | 210,849 | +5.42% | 0 | - | 235 |
| random_hold | 209,742 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 207,830 | +3.92% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,152 | +1.08% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,564 | +0.78% | 2 | 50% | 345 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,766 | -0.12% | 1 | 100% | 255 |
| snake_abs_conv | 199,580 | -0.21% | 1 | 100% | 255 |
| snake_anaconda | 193,449 | -3.27% | 3 | 33% | 374 |
| snake_viper_wild | 193,257 | -3.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,970 | -5.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,737 | -16.13% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,886 (-5.56%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,140 | +1.91% |
| benchmark_smallcap | +1,894 | +0.95% |
| benchmark | +1,132 | +0.50% |
| intraweek | +1,087 | +0.53% |
| random_hold | +249 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -104 | -0.05% |
| snake_abs | -384 | -0.19% |
| snake_abs_conv | -392 | -0.20% |
| snake_abs_exit_conv | -412 | -0.20% |
| unified | -551 | -0.25% |
| intramonth | -844 | -0.40% |
| oracle | -939 | -0.44% |
| snake_anaconda | -1,104 | -0.57% |
| snake_viper_tick | -4,206 | -2.17% |
| snake_viper_wild | -4,287 | -2.17% |

Average per day so far: benchmark Rs +638, unified Rs +574, oracle Rs +314, intramonth Rs +265, random_hold Rs +238, intraweek Rs +191, snake_abs_exit Rs +57, nifty_calls Rs +45, snake_abs_exit_conv Rs +41, benchmark_smallcap Rs +19, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, snake_anaconda Rs -182, snake_viper_wild Rs -204, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -334, gold Rs -787

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.