# Paper trading report

Updated 2026-11-09 13:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,113 | +10.06% | 0 | - | 236 |
| benchmark | 217,442 | +8.72% | 0 | - | 237 |
| intraweek | 214,745 | +7.37% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,301 | +6.65% | 2 | 50% | 330 |
| snake_abs_exit | 212,804 | +6.40% | 2 | 50% | 308 |
| intramonth | 210,148 | +5.07% | 0 | - | 235 |
| snake_abs | 209,984 | +4.99% | 1 | 100% | 255 |
| snake_abs_conv | 209,821 | +4.91% | 1 | 100% | 255 |
| oracle | 209,493 | +4.75% | 0 | - | 233 |
| random_hold | 204,386 | +2.19% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,208 | +0.10% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,774 | -0.11% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,307 | -0.85% | 0 | - | 237 |
| snake_viper_tick | 196,381 | -1.81% | 6 | 50% | 1,154 |
| gold | 192,166 | -3.92% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,400 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,879 | +2.34% |
| snake_abs_conv | +4,594 | +2.24% |
| snake_abs | +4,565 | +2.22% |
| unified | +4,503 | +2.09% |
| snake_abs_exit | +4,492 | +2.16% |
| intraweek | +4,382 | +2.08% |
| snake_anaconda | +4,380 | +2.24% |
| snake_viper_wild | +3,736 | +1.91% |
| snake_viper_tick | +3,671 | +1.91% |
| oracle | +3,666 | +1.78% |
| intramonth | +2,545 | +1.23% |
| benchmark_smallcap | +1,513 | +0.77% |
| gold | +1,118 | +0.58% |
| random_hold | +479 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -46 | -0.02% |

Average per day so far: unified Rs +670, benchmark Rs +581, snake_abs_exit_conv Rs +493, intraweek Rs +491, snake_abs_exit Rs +474, snake_abs_conv Rs +364, snake_abs Rs +357, intramonth Rs +338, oracle Rs +316, random_hold Rs +146, nifty_calls Rs +61, snake_anaconda Rs +8, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -10, benchmark_smallcap Rs -65, snake_viper_tick Rs -190, gold Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.