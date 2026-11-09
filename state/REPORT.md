# Paper trading report

Updated 2026-11-09 14:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,778 | +9.89% | 0 | - | 236 |
| benchmark | 217,618 | +8.81% | 0 | - | 237 |
| intraweek | 214,861 | +7.43% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,187 | +6.59% | 2 | 50% | 330 |
| snake_abs_exit | 212,591 | +6.29% | 2 | 50% | 308 |
| snake_abs | 210,004 | +5.00% | 1 | 100% | 255 |
| intramonth | 209,878 | +4.94% | 0 | - | 235 |
| snake_abs_conv | 209,836 | +4.92% | 1 | 100% | 255 |
| oracle | 209,448 | +4.72% | 0 | - | 233 |
| random_hold | 204,327 | +2.16% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,387 | +0.19% | 7 | 57% | 1,332 |
| snake_anaconda | 200,055 | +0.03% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,150 | -0.93% | 0 | - | 237 |
| snake_viper_tick | 196,983 | -1.51% | 6 | 50% | 1,154 |
| gold | 192,166 | -3.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,308 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,765 | +2.29% |
| snake_abs_conv | +4,609 | +2.25% |
| snake_abs | +4,585 | +2.23% |
| intraweek | +4,498 | +2.14% |
| snake_viper_wild | +4,350 | +2.22% |
| snake_abs_exit | +4,279 | +2.05% |
| snake_viper_tick | +4,273 | +2.22% |
| snake_anaconda | +4,228 | +2.16% |
| unified | +4,169 | +1.93% |
| oracle | +3,622 | +1.76% |
| intramonth | +2,275 | +1.10% |
| benchmark_smallcap | +1,356 | +0.69% |
| gold | +1,118 | +0.58% |
| random_hold | +421 | +0.21% |
| benchmark | +130 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +659, benchmark Rs +587, intraweek Rs +495, snake_abs_exit_conv Rs +488, snake_abs_exit Rs +466, snake_abs_conv Rs +364, snake_abs Rs +357, intramonth Rs +329, oracle Rs +315, random_hold Rs +144, nifty_calls Rs +61, snake_viper_wild Rs +18, snake_anaconda Rs +2, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -71, snake_viper_tick Rs -159, gold Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.