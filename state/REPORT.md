# Paper trading report

Updated 2026-11-06 15:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,472 | +8.74% | 0 | - | 237 |
| unified | 215,232 | +7.62% | 0 | - | 236 |
| intraweek | 209,080 | +4.54% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,647 | +4.32% | 1 | 100% | 255 |
| snake_abs_exit | 208,528 | +4.26% | 1 | 100% | 260 |
| intramonth | 207,491 | +3.75% | 0 | - | 235 |
| oracle | 205,782 | +2.89% | 0 | - | 233 |
| snake_abs | 205,637 | +2.82% | 1 | 100% | 255 |
| snake_abs_conv | 205,448 | +2.72% | 1 | 100% | 255 |
| random_hold | 203,568 | +1.78% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,715 | -1.64% | 0 | - | 237 |
| snake_anaconda | 196,006 | -2.00% | 3 | 33% | 374 |
| snake_viper_wild | 195,981 | -2.01% | 4 | 25% | 842 |
| snake_viper_tick | 192,655 | -3.67% | 3 | 0% | 672 |
| gold | 190,999 | -4.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,193 (-6.40%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,703 | +1.73% |
| oracle | +1,710 | +0.84% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -338 | -0.16% |
| intramonth | -458 | -0.22% |
| unified | -752 | -0.35% |
| random_hold | -755 | -0.37% |
| benchmark_smallcap | -1,973 | -0.99% |
| gold | -3,222 | -1.66% |
| snake_abs | -6,052 | -2.86% |
| snake_abs_conv | -6,097 | -2.88% |
| snake_abs_exit | -6,131 | -2.86% |
| snake_abs_exit_conv | -6,157 | -2.87% |
| snake_anaconda | -6,473 | -3.20% |
| snake_viper_tick | -8,483 | -4.22% |
| snake_viper_wild | -8,675 | -4.24% |

Average per day so far: benchmark Rs +602, unified Rs +525, snake_abs_exit_conv Rs +333, snake_abs_exit Rs +328, intraweek Rs +313, intramonth Rs +258, snake_abs_conv Rs +210, snake_abs Rs +209, oracle Rs +199, random_hold Rs +123, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -131, snake_anaconda Rs -166, snake_viper_wild Rs -191, gold Rs -310, snake_viper_tick Rs -408, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.