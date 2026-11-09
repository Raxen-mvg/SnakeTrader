# Paper trading report

Updated 2026-11-09 12:57 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,163 | +10.08% | 0 | - | 236 |
| benchmark | 217,335 | +8.67% | 0 | - | 237 |
| intraweek | 214,947 | +7.47% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,486 | +6.24% | 2 | 50% | 330 |
| snake_abs_exit | 212,164 | +6.08% | 2 | 50% | 308 |
| intramonth | 210,218 | +5.11% | 0 | - | 235 |
| snake_abs | 209,693 | +4.85% | 1 | 100% | 255 |
| oracle | 209,622 | +4.81% | 0 | - | 233 |
| snake_abs_conv | 209,518 | +4.76% | 1 | 100% | 255 |
| random_hold | 204,534 | +2.27% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,606 | -0.20% | 3 | 33% | 374 |
| snake_viper_wild | 199,451 | -0.28% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,497 | -0.75% | 0 | - | 237 |
| snake_viper_tick | 196,064 | -1.97% | 6 | 50% | 1,154 |
| gold | 192,528 | -3.74% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,416 (-4.79%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,585 | +2.18% |
| unified | +4,553 | +2.11% |
| snake_abs_conv | +4,291 | +2.09% |
| snake_abs | +4,273 | +2.08% |
| snake_abs_exit_conv | +4,064 | +1.95% |
| snake_abs_exit | +3,852 | +1.85% |
| oracle | +3,795 | +1.84% |
| snake_anaconda | +3,779 | +1.93% |
| snake_viper_wild | +3,413 | +1.74% |
| snake_viper_tick | +3,354 | +1.74% |
| intramonth | +2,615 | +1.26% |
| benchmark_smallcap | +1,704 | +0.87% |
| gold | +1,480 | +0.77% |
| random_hold | +628 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -153 | -0.07% |

Average per day so far: unified Rs +672, benchmark Rs +578, intraweek Rs +498, snake_abs_exit_conv Rs +462, snake_abs_exit Rs +451, snake_abs_conv Rs +353, snake_abs Rs +346, intramonth Rs +341, oracle Rs +321, random_hold Rs +151, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -16, snake_viper_wild Rs -25, benchmark_smallcap Rs -58, snake_viper_tick Rs -207, gold Rs -249, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.