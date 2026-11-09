# Paper trading report

Updated 2026-11-09 09:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,434 | +10.72% | 0 | - | 236 |
| benchmark | 217,220 | +8.61% | 0 | - | 237 |
| intraweek | 214,947 | +7.47% | 25 | 48% | 2,757 |
| intramonth | 211,483 | +5.74% | 0 | - | 235 |
| snake_abs_exit_conv | 210,974 | +5.49% | 1 | 100% | 255 |
| snake_abs_exit | 210,910 | +5.46% | 1 | 100% | 260 |
| oracle | 208,423 | +4.21% | 0 | - | 233 |
| snake_abs | 207,949 | +3.97% | 1 | 100% | 255 |
| snake_abs_conv | 207,759 | +3.88% | 1 | 100% | 255 |
| random_hold | 205,185 | +2.59% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,625 | -0.19% | 4 | 25% | 842 |
| benchmark_smallcap | 197,903 | -1.05% | 0 | - | 237 |
| snake_anaconda | 197,875 | -1.06% | 3 | 33% | 374 |
| snake_viper_tick | 196,255 | -1.87% | 3 | 0% | 672 |
| gold | 192,873 | -3.56% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,495 (-4.75%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +5,825 | +2.70% |
| intraweek | +4,585 | +2.18% |
| intramonth | +3,880 | +1.87% |
| snake_viper_wild | +3,588 | +1.83% |
| snake_viper_tick | +3,545 | +1.84% |
| snake_abs_exit | +2,598 | +1.25% |
| oracle | +2,596 | +1.26% |
| snake_abs_exit_conv | +2,553 | +1.23% |
| snake_abs_conv | +2,532 | +1.23% |
| snake_abs | +2,530 | +1.23% |
| snake_anaconda | +2,048 | +1.05% |
| gold | +1,825 | +0.95% |
| random_hold | +1,278 | +0.63% |
| benchmark_smallcap | +1,110 | +0.56% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -268 | -0.12% |

Average per day so far: unified Rs +714, benchmark Rs +574, intraweek Rs +498, snake_abs_exit_conv Rs +406, snake_abs_exit Rs +404, intramonth Rs +383, snake_abs_conv Rs +287, snake_abs Rs +284, oracle Rs +281, random_hold Rs +173, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -17, benchmark_smallcap Rs -81, snake_anaconda Rs -85, snake_viper_tick Rs -197, gold Rs -238, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.