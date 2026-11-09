# Paper trading report

Updated 2026-11-09 10:50 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,010 | +10.01% | 0 | - | 236 |
| benchmark | 217,029 | +8.51% | 0 | - | 237 |
| intraweek | 216,159 | +8.08% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,121 | +6.06% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,106 | +6.05% | 2 | 50% | 330 |
| intramonth | 210,138 | +5.07% | 0 | - | 235 |
| snake_abs | 209,924 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,752 | +4.88% | 1 | 100% | 255 |
| oracle | 209,657 | +4.83% | 0 | - | 233 |
| random_hold | 204,023 | +2.01% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,638 | -0.18% | 3 | 33% | 374 |
| benchmark_smallcap | 198,363 | -0.82% | 0 | - | 237 |
| snake_viper_wild | 197,312 | -1.34% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,958 | -3.02% | 6 | 50% | 1,154 |
| gold | 193,087 | -3.46% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,586 (-4.71%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +5,797 | +2.76% |
| snake_abs_conv | +4,525 | +2.21% |
| snake_abs | +4,505 | +2.19% |
| unified | +4,401 | +2.04% |
| oracle | +3,830 | +1.86% |
| snake_anaconda | +3,811 | +1.95% |
| snake_abs_exit | +3,809 | +1.83% |
| snake_abs_exit_conv | +3,685 | +1.77% |
| intramonth | +2,535 | +1.22% |
| gold | +2,039 | +1.07% |
| benchmark_smallcap | +1,569 | +0.80% |
| snake_viper_wild | +1,274 | +0.65% |
| snake_viper_tick | +1,249 | +0.65% |
| random_hold | +116 | +0.06% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -459 | -0.21% |

Average per day so far: unified Rs +667, benchmark Rs +568, intraweek Rs +539, snake_abs_exit Rs +449, snake_abs_exit_conv Rs +448, snake_abs_conv Rs +361, snake_abs Rs +354, intramonth Rs +338, oracle Rs +322, random_hold Rs +134, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -14, benchmark_smallcap Rs -63, snake_viper_wild Rs -122, gold Rs -230, snake_viper_tick Rs -318, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.