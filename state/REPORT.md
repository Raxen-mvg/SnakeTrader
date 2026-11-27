# Paper trading report

Updated 2026-11-27 12:16 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,396 | +12.20% | 0 | - | 237 |
| unified | 223,286 | +11.64% | 0 | - | 236 |
| oracle | 211,916 | +5.96% | 0 | - | 233 |
| intramonth | 210,946 | +5.47% | 0 | - | 235 |
| random_hold | 210,145 | +5.07% | 13 | 69% | 1,037 |
| intraweek | 207,950 | +3.98% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,098 | +2.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,827 | +1.91% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,688 | +0.34% | 1 | 100% | 255 |
| snake_abs_conv | 200,511 | +0.26% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,030 | -2.98% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,249 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,751 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,020 | +2.00% |
| snake_abs_exit_conv | +3,430 | +1.71% |
| gold | +3,255 | +1.96% |
| snake_abs_conv | +2,145 | +1.08% |
| snake_abs | +2,136 | +1.08% |
| snake_anaconda | +1,734 | +0.90% |
| random_hold | +1,551 | +0.74% |
| intraweek | +901 | +0.43% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +412 | +0.20% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| unified | +207 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -319 | -0.15% |
| benchmark | -1,591 | -0.70% |

Average per day so far: benchmark Rs +581, unified Rs +554, oracle Rs +284, intramonth Rs +261, random_hold Rs +242, intraweek Rs +189, snake_abs_exit Rs +131, snake_abs_exit_conv Rs +98, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +17, snake_abs_conv Rs +13, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -161, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -732

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.