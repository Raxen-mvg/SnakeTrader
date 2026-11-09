# Paper trading report

Updated 2026-11-09 14:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,006 | +10.00% | 0 | - | 236 |
| benchmark | 217,962 | +8.98% | 0 | - | 237 |
| intraweek | 214,330 | +7.17% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,578 | +6.29% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,435 | +6.22% | 2 | 50% | 330 |
| intramonth | 210,050 | +5.03% | 0 | - | 235 |
| snake_abs | 209,940 | +4.97% | 1 | 100% | 255 |
| snake_abs_conv | 209,775 | +4.89% | 1 | 100% | 255 |
| oracle | 209,221 | +4.61% | 0 | - | 233 |
| random_hold | 204,382 | +2.19% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,990 | -0.01% | 3 | 33% | 374 |
| benchmark_smallcap | 198,094 | -0.95% | 0 | - | 237 |
| snake_viper_wild | 197,841 | -1.08% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,483 | -2.76% | 6 | 50% | 1,154 |
| gold | 192,183 | -3.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,213 (-4.89%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,548 | +2.22% |
| snake_abs | +4,521 | +2.20% |
| unified | +4,396 | +2.04% |
| snake_abs_exit | +4,266 | +2.05% |
| snake_anaconda | +4,163 | +2.13% |
| snake_abs_exit_conv | +4,013 | +1.93% |
| intraweek | +3,967 | +1.89% |
| oracle | +3,394 | +1.65% |
| intramonth | +2,447 | +1.18% |
| snake_viper_wild | +1,804 | +0.92% |
| snake_viper_tick | +1,773 | +0.92% |
| benchmark_smallcap | +1,300 | +0.66% |
| gold | +1,134 | +0.59% |
| random_hold | +475 | +0.23% |
| benchmark | +474 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +667, benchmark Rs +599, intraweek Rs +478, snake_abs_exit Rs +466, snake_abs_exit_conv Rs +461, snake_abs_conv Rs +362, snake_abs Rs +355, intramonth Rs +335, oracle Rs +307, random_hold Rs +146, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -0, benchmark_smallcap Rs -73, snake_viper_wild Rs -98, gold Rs -261, snake_viper_tick Rs -290, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.