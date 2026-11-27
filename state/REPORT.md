# Paper trading report

Updated 2026-11-27 13:34 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,937 | +11.97% | 0 | - | 237 |
| unified | 223,359 | +11.68% | 0 | - | 236 |
| oracle | 211,817 | +5.91% | 0 | - | 233 |
| intramonth | 210,928 | +5.46% | 0 | - | 235 |
| random_hold | 210,715 | +5.36% | 13 | 69% | 1,037 |
| intraweek | 208,297 | +4.15% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,499 | +2.75% | 2 | 50% | 345 |
| snake_abs_exit | 204,498 | +2.25% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| snake_abs | 200,250 | +0.12% | 1 | 100% | 255 |
| snake_abs_conv | 200,068 | +0.03% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,548 | -3.23% | 3 | 33% | 374 |
| snake_viper_wild | 192,044 | -3.98% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,783 | -5.61% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,956 | -15.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,845 (-5.58%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,102 | +2.55% |
| gold | +3,962 | +2.39% |
| snake_abs_exit | +3,421 | +1.70% |
| random_hold | +2,121 | +1.02% |
| snake_abs_conv | +1,702 | +0.86% |
| snake_abs | +1,698 | +0.85% |
| snake_anaconda | +1,252 | +0.65% |
| intraweek | +1,248 | +0.60% |
| benchmark_smallcap | +504 | +0.25% |
| intramonth | +395 | +0.19% |
| unified | +280 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -158 | -0.08% |
| snake_viper_wild | -162 | -0.08% |
| oracle | -419 | -0.20% |
| benchmark | -2,050 | -0.91% |

Average per day so far: benchmark Rs +570, unified Rs +556, oracle Rs +281, intramonth Rs +260, random_hold Rs +255, intraweek Rs +198, snake_abs_exit_conv Rs +141, snake_abs_exit Rs +115, nifty_calls Rs +44, benchmark_smallcap Rs +35, snake_abs Rs +6, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -174, snake_viper_wild Rs -234, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -362, gold Rs -715

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.