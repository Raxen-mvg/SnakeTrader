# Paper trading report

Updated 2026-11-06 14:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,906 | +8.45% | 0 | - | 237 |
| unified | 215,091 | +7.54% | 0 | - | 236 |
| intraweek | 209,286 | +4.64% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,949 | +4.47% | 1 | 100% | 255 |
| snake_abs_exit | 208,866 | +4.43% | 1 | 100% | 260 |
| intramonth | 207,321 | +3.66% | 0 | - | 235 |
| snake_abs | 205,936 | +2.97% | 1 | 100% | 255 |
| snake_abs_conv | 205,747 | +2.87% | 1 | 100% | 255 |
| oracle | 205,453 | +2.73% | 0 | - | 233 |
| random_hold | 203,540 | +1.77% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,192 | -1.90% | 3 | 33% | 374 |
| benchmark_smallcap | 196,188 | -1.91% | 0 | - | 237 |
| snake_viper_wild | 196,059 | -1.97% | 4 | 25% | 842 |
| snake_viper_tick | 192,731 | -3.63% | 3 | 0% | 672 |
| gold | 191,575 | -4.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,225 (-6.39%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,137 | +1.47% |
| oracle | +1,381 | +0.68% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -133 | -0.06% |
| intramonth | -628 | -0.30% |
| random_hold | -783 | -0.38% |
| unified | -893 | -0.41% |
| benchmark_smallcap | -2,500 | -1.26% |
| gold | -2,647 | -1.36% |
| snake_abs | -5,752 | -2.72% |
| snake_abs_exit | -5,792 | -2.70% |
| snake_abs_conv | -5,798 | -2.74% |
| snake_abs_exit_conv | -5,854 | -2.73% |
| snake_anaconda | -6,288 | -3.10% |
| snake_viper_tick | -8,407 | -4.18% |
| snake_viper_wild | -8,597 | -4.20% |

Average per day so far: benchmark Rs +583, unified Rs +520, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +341, intraweek Rs +320, intramonth Rs +252, snake_abs_conv Rs +221, snake_abs Rs +220, oracle Rs +188, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -152, snake_anaconda Rs -159, snake_viper_wild Rs -188, gold Rs -291, snake_viper_tick Rs -404, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.