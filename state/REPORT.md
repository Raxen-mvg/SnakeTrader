# Paper trading report

Updated 2026-11-09 13:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,770 | +9.88% | 0 | - | 236 |
| benchmark | 217,220 | +8.61% | 0 | - | 237 |
| intraweek | 214,733 | +7.37% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,400 | +6.70% | 2 | 50% | 330 |
| snake_abs_exit | 212,974 | +6.49% | 2 | 50% | 308 |
| snake_abs | 210,154 | +5.08% | 1 | 100% | 255 |
| snake_abs_conv | 209,991 | +5.00% | 1 | 100% | 255 |
| intramonth | 209,847 | +4.92% | 0 | - | 235 |
| oracle | 209,374 | +4.69% | 0 | - | 233 |
| random_hold | 204,291 | +2.15% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,379 | +0.19% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,563 | -0.22% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,296 | -0.85% | 0 | - | 237 |
| snake_viper_tick | 196,173 | -1.91% | 6 | 50% | 1,154 |
| gold | 192,117 | -3.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,296 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,978 | +2.39% |
| snake_abs_conv | +4,764 | +2.32% |
| snake_abs | +4,734 | +2.31% |
| snake_abs_exit | +4,662 | +2.24% |
| snake_anaconda | +4,552 | +2.33% |
| intraweek | +4,370 | +2.08% |
| unified | +4,161 | +1.93% |
| oracle | +3,547 | +1.72% |
| snake_viper_wild | +3,525 | +1.80% |
| snake_viper_tick | +3,464 | +1.80% |
| intramonth | +2,244 | +1.08% |
| benchmark_smallcap | +1,502 | +0.76% |
| gold | +1,069 | +0.56% |
| random_hold | +384 | +0.19% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -268 | -0.12% |

Average per day so far: unified Rs +659, benchmark Rs +574, snake_abs_exit_conv Rs +496, intraweek Rs +491, snake_abs_exit Rs +481, snake_abs_conv Rs +370, snake_abs Rs +363, intramonth Rs +328, oracle Rs +312, random_hold Rs +143, nifty_calls Rs +61, snake_anaconda Rs +15, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -20, benchmark_smallcap Rs -66, snake_viper_tick Rs -201, gold Rs -263, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.