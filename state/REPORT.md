# Paper trading report

Updated 2026-11-09 11:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,290 | +10.14% | 0 | - | 236 |
| benchmark | 216,746 | +8.37% | 0 | - | 237 |
| intraweek | 215,109 | +7.55% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 211,845 | +5.92% | 2 | 50% | 330 |
| snake_abs_exit | 211,837 | +5.92% | 2 | 50% | 308 |
| intramonth | 210,520 | +5.26% | 0 | - | 235 |
| snake_abs | 209,614 | +4.81% | 1 | 100% | 255 |
| snake_abs_conv | 209,438 | +4.72% | 1 | 100% | 255 |
| oracle | 209,412 | +4.71% | 0 | - | 233 |
| random_hold | 204,154 | +2.08% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,328 | -0.34% | 3 | 33% | 374 |
| benchmark_smallcap | 198,060 | -0.97% | 0 | - | 237 |
| snake_viper_wild | 197,947 | -1.03% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,584 | -2.71% | 6 | 50% | 1,154 |
| gold | 193,005 | -3.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,421 (-4.79%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,746 | +2.26% |
| unified | +4,681 | +2.17% |
| snake_abs_conv | +4,211 | +2.05% |
| snake_abs | +4,194 | +2.04% |
| oracle | +3,585 | +1.74% |
| snake_abs_exit | +3,525 | +1.69% |
| snake_anaconda | +3,501 | +1.79% |
| snake_abs_exit_conv | +3,423 | +1.64% |
| intramonth | +2,917 | +1.41% |
| gold | +1,956 | +1.02% |
| snake_viper_wild | +1,909 | +0.97% |
| snake_viper_tick | +1,875 | +0.97% |
| benchmark_smallcap | +1,267 | +0.64% |
| random_hold | +247 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -742 | -0.34% |

Average per day so far: unified Rs +676, benchmark Rs +558, intraweek Rs +504, snake_abs_exit_conv Rs +439, snake_abs_exit Rs +438, intramonth Rs +351, snake_abs_conv Rs +350, snake_abs Rs +343, oracle Rs +314, random_hold Rs +138, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -27, benchmark_smallcap Rs -75, snake_viper_wild Rs -93, gold Rs -233, snake_viper_tick Rs -285, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.