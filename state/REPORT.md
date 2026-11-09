# Paper trading report

Updated 2026-11-09 13:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,797 | +9.90% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 214,682 | +7.34% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,299 | +6.65% | 2 | 50% | 330 |
| snake_abs_exit | 212,871 | +6.43% | 2 | 50% | 308 |
| snake_abs | 210,054 | +5.03% | 1 | 100% | 255 |
| snake_abs_conv | 209,891 | +4.95% | 1 | 100% | 255 |
| intramonth | 209,886 | +4.94% | 0 | - | 235 |
| oracle | 209,238 | +4.62% | 0 | - | 233 |
| random_hold | 204,254 | +2.13% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,279 | +0.14% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,524 | -0.24% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,385 | -0.81% | 0 | - | 237 |
| snake_viper_tick | 196,135 | -1.93% | 6 | 50% | 1,154 |
| gold | 192,133 | -3.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,262 (-4.87%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,877 | +2.34% |
| snake_abs_conv | +4,664 | +2.27% |
| snake_abs | +4,635 | +2.26% |
| snake_abs_exit | +4,559 | +2.19% |
| snake_anaconda | +4,451 | +2.27% |
| intraweek | +4,319 | +2.05% |
| unified | +4,187 | +1.94% |
| snake_viper_wild | +3,486 | +1.78% |
| snake_viper_tick | +3,425 | +1.78% |
| oracle | +3,412 | +1.66% |
| intramonth | +2,282 | +1.10% |
| benchmark_smallcap | +1,592 | +0.81% |
| gold | +1,085 | +0.57% |
| random_hold | +347 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +660, benchmark Rs +577, snake_abs_exit_conv Rs +493, intraweek Rs +489, snake_abs_exit Rs +477, snake_abs_conv Rs +366, snake_abs Rs +359, intramonth Rs +330, oracle Rs +308, random_hold Rs +142, nifty_calls Rs +61, snake_anaconda Rs +11, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -22, benchmark_smallcap Rs -62, snake_viper_tick Rs -203, gold Rs -262, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.