# Paper trading report

Updated 2026-11-26 12:39 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,155 | +13.08% | 0 | - | 237 |
| unified | 223,458 | +11.73% | 0 | - | 236 |
| oracle | 213,344 | +6.67% | 0 | - | 233 |
| intramonth | 210,528 | +5.26% | 0 | - | 235 |
| random_hold | 209,865 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 208,330 | +4.17% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,276 | +0.14% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,765 | -0.12% | 2 | 50% | 345 |
| snake_abs | 198,193 | -0.90% | 1 | 100% | 255 |
| snake_abs_conv | 197,993 | -1.00% | 1 | 100% | 255 |
| snake_anaconda | 191,946 | -4.03% | 3 | 33% | 374 |
| snake_viper_wild | 191,846 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,589 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,837 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,760 | +0.89% |
| gold | +1,644 | +1.00% |
| intraweek | +1,587 | +0.77% |
| benchmark | +1,132 | +0.50% |
| random_hold | +373 | +0.18% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -452 | -0.21% |
| unified | -642 | -0.29% |
| intramonth | -1,166 | -0.55% |
| snake_abs | -1,957 | -0.98% |
| snake_abs_conv | -1,979 | -0.99% |
| snake_abs_exit | -1,980 | -0.98% |
| snake_abs_exit_conv | -2,211 | -1.09% |
| snake_anaconda | -2,607 | -1.34% |
| snake_viper_tick | -5,588 | -2.88% |
| snake_viper_wild | -5,698 | -2.88% |

Average per day so far: benchmark Rs +638, unified Rs +572, oracle Rs +325, intramonth Rs +257, random_hold Rs +241, intraweek Rs +203, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -6, snake_abs Rs -46, snake_abs_conv Rs -53, snake_anaconda Rs -224, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -380, gold Rs -823

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.