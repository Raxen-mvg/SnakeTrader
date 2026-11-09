# Paper trading report

Updated 2026-11-09 12:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,163 | +10.08% | 0 | - | 236 |
| benchmark | 217,151 | +8.57% | 0 | - | 237 |
| intraweek | 214,737 | +7.37% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,555 | +6.28% | 2 | 50% | 330 |
| snake_abs_exit | 212,142 | +6.07% | 2 | 50% | 308 |
| intramonth | 210,387 | +5.19% | 0 | - | 235 |
| snake_abs | 209,937 | +4.97% | 1 | 100% | 255 |
| snake_abs_conv | 209,760 | +4.88% | 1 | 100% | 255 |
| oracle | 209,702 | +4.85% | 0 | - | 233 |
| random_hold | 204,514 | +2.26% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,613 | -0.19% | 3 | 33% | 374 |
| snake_viper_wild | 199,229 | -0.39% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,677 | -0.66% | 0 | - | 237 |
| snake_viper_tick | 195,844 | -2.08% | 6 | 50% | 1,154 |
| gold | 192,561 | -3.72% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,426 (-4.79%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,554 | +2.11% |
| snake_abs_conv | +4,533 | +2.21% |
| snake_abs | +4,518 | +2.20% |
| intraweek | +4,374 | +2.08% |
| snake_abs_exit_conv | +4,133 | +1.98% |
| oracle | +3,875 | +1.88% |
| snake_abs_exit | +3,830 | +1.84% |
| snake_anaconda | +3,786 | +1.93% |
| snake_viper_wild | +3,192 | +1.63% |
| snake_viper_tick | +3,134 | +1.63% |
| intramonth | +2,784 | +1.34% |
| benchmark_smallcap | +1,883 | +0.96% |
| gold | +1,512 | +0.79% |
| random_hold | +608 | +0.30% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -337 | -0.15% |

Average per day so far: unified Rs +672, benchmark Rs +572, intraweek Rs +491, snake_abs_exit_conv Rs +465, snake_abs_exit Rs +450, snake_abs_conv Rs +361, snake_abs Rs +355, intramonth Rs +346, oracle Rs +323, random_hold Rs +150, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -15, snake_viper_wild Rs -35, benchmark_smallcap Rs -51, snake_viper_tick Rs -219, gold Rs -248, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.