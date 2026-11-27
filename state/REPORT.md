# Paper trading report

Updated 2026-11-27 14:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,112 | +12.06% | 0 | - | 237 |
| unified | 223,643 | +11.82% | 0 | - | 236 |
| oracle | 211,946 | +5.97% | 0 | - | 233 |
| random_hold | 211,200 | +5.60% | 13 | 69% | 1,037 |
| intramonth | 210,984 | +5.49% | 0 | - | 235 |
| intraweek | 208,026 | +4.01% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,578 | +3.29% | 2 | 50% | 345 |
| snake_abs_exit | 204,275 | +2.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,614 | +0.81% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,798 | -0.10% | 1 | 100% | 255 |
| snake_abs_conv | 199,614 | -0.19% | 1 | 100% | 255 |
| snake_anaconda | 193,097 | -3.45% | 3 | 33% | 374 |
| snake_viper_wild | 192,313 | -3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,047 | -5.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,761 | -14.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,018 (-5.49%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,181 | +3.08% |
| gold | +4,768 | +2.87% |
| snake_abs_exit | +3,198 | +1.59% |
| random_hold | +2,606 | +1.25% |
| snake_abs_conv | +1,248 | +0.63% |
| snake_abs | +1,246 | +0.63% |
| intraweek | +977 | +0.47% |
| snake_anaconda | +800 | +0.42% |
| benchmark_smallcap | +773 | +0.39% |
| unified | +565 | +0.25% |
| intramonth | +451 | +0.21% |
| snake_viper_wild | +107 | +0.06% |
| snake_viper_tick | +106 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -289 | -0.14% |
| benchmark | -1,874 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +563, oracle Rs +284, random_hold Rs +267, intramonth Rs +262, intraweek Rs +191, snake_abs_exit_conv Rs +169, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -5, snake_abs_conv Rs -10, snake_anaconda Rs -187, snake_viper_wild Rs -226, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -353, gold Rs -696

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.