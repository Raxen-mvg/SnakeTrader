# Paper trading report

Updated 2026-11-09 10:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,367 | +10.18% | 0 | - | 236 |
| benchmark | 217,411 | +8.71% | 0 | - | 237 |
| intraweek | 215,534 | +7.77% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,115 | +5.56% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,053 | +5.53% | 2 | 50% | 330 |
| intramonth | 210,599 | +5.30% | 0 | - | 235 |
| oracle | 209,322 | +4.66% | 0 | - | 233 |
| snake_abs | 208,798 | +4.40% | 1 | 100% | 255 |
| snake_abs_conv | 208,616 | +4.31% | 1 | 100% | 255 |
| random_hold | 203,936 | +1.97% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,568 | -0.72% | 3 | 33% | 374 |
| benchmark_smallcap | 198,408 | -0.80% | 0 | - | 237 |
| snake_viper_wild | 197,314 | -1.34% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,963 | -3.02% | 6 | 50% | 1,154 |
| gold | 193,449 | -3.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,396 (-4.80%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,171 | +2.46% |
| unified | +4,757 | +2.21% |
| oracle | +3,495 | +1.70% |
| snake_abs_conv | +3,389 | +1.65% |
| snake_abs | +3,379 | +1.65% |
| intramonth | +2,996 | +1.44% |
| snake_abs_exit | +2,803 | +1.35% |
| snake_anaconda | +2,740 | +1.40% |
| snake_abs_exit_conv | +2,632 | +1.26% |
| gold | +2,400 | +1.26% |
| benchmark_smallcap | +1,614 | +0.82% |
| snake_viper_wild | +1,276 | +0.65% |
| snake_viper_tick | +1,253 | +0.65% |
| random_hold | +29 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -76 | -0.04% |

Average per day so far: unified Rs +679, benchmark Rs +580, intraweek Rs +518, snake_abs_exit Rs +412, snake_abs_exit_conv Rs +409, intramonth Rs +353, snake_abs_conv Rs +319, snake_abs Rs +314, oracle Rs +311, random_hold Rs +131, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -57, benchmark_smallcap Rs -61, snake_viper_wild Rs -122, gold Rs -218, snake_viper_tick Rs -318, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.