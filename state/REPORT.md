# Paper trading report

Updated 2026-11-09 14:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,015 | +10.01% | 0 | - | 236 |
| benchmark | 217,442 | +8.72% | 0 | - | 237 |
| intraweek | 214,701 | +7.35% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,485 | +6.74% | 2 | 50% | 330 |
| snake_abs_exit | 213,011 | +6.50% | 2 | 50% | 308 |
| snake_abs | 210,370 | +5.18% | 1 | 100% | 255 |
| snake_abs_conv | 210,203 | +5.10% | 1 | 100% | 255 |
| intramonth | 210,058 | +5.03% | 0 | - | 235 |
| oracle | 209,348 | +4.67% | 0 | - | 233 |
| random_hold | 204,444 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,414 | +0.21% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,597 | -0.20% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,094 | -0.95% | 0 | - | 237 |
| snake_viper_tick | 196,207 | -1.90% | 6 | 50% | 1,154 |
| gold | 192,101 | -3.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,387 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,064 | +2.43% |
| snake_abs_conv | +4,976 | +2.42% |
| snake_abs | +4,950 | +2.41% |
| snake_abs_exit | +4,699 | +2.26% |
| snake_anaconda | +4,586 | +2.34% |
| unified | +4,405 | +2.04% |
| intraweek | +4,338 | +2.06% |
| snake_viper_wild | +3,560 | +1.82% |
| oracle | +3,521 | +1.71% |
| snake_viper_tick | +3,497 | +1.81% |
| intramonth | +2,455 | +1.18% |
| benchmark_smallcap | +1,300 | +0.66% |
| gold | +1,052 | +0.55% |
| random_hold | +537 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -46 | -0.02% |

Average per day so far: unified Rs +667, benchmark Rs +581, snake_abs_exit_conv Rs +499, intraweek Rs +490, snake_abs_exit Rs +482, snake_abs_conv Rs +378, snake_abs Rs +370, intramonth Rs +335, oracle Rs +312, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +17, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -18, benchmark_smallcap Rs -73, snake_viper_tick Rs -200, gold Rs -263, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.