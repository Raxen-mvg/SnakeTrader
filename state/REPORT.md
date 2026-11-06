# Paper trading report

Updated 2026-11-06 12:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,861 | +7.43% | 0 | - | 236 |
| benchmark | 214,657 | +7.33% | 0 | - | 237 |
| intraweek | 210,917 | +5.46% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,006 | +4.50% | 1 | 100% | 255 |
| snake_abs_exit | 208,823 | +4.41% | 1 | 100% | 260 |
| intramonth | 207,091 | +3.54% | 0 | - | 235 |
| snake_abs | 205,967 | +2.98% | 1 | 100% | 255 |
| snake_abs_conv | 205,795 | +2.90% | 1 | 100% | 255 |
| oracle | 204,706 | +2.35% | 0 | - | 233 |
| random_hold | 203,319 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,242 | -1.88% | 3 | 33% | 374 |
| snake_viper_wild | 195,167 | -2.42% | 3 | 33% | 702 |
| benchmark_smallcap | 194,675 | -2.66% | 0 | - | 237 |
| snake_viper_tick | 191,862 | -4.07% | 2 | 0% | 532 |
| gold | 190,095 | -4.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,234 (-6.38%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,498 | +0.71% |
| benchmark | +887 | +0.41% |
| oracle | +634 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -858 | -0.41% |
| random_hold | -1,005 | -0.49% |
| unified | -1,123 | -0.52% |
| benchmark_smallcap | -4,013 | -2.02% |
| gold | -4,126 | -2.12% |
| snake_abs | -5,722 | -2.70% |
| snake_abs_conv | -5,749 | -2.72% |
| snake_abs_exit_conv | -5,798 | -2.70% |
| snake_abs_exit | -5,836 | -2.72% |
| snake_anaconda | -6,238 | -3.08% |
| snake_viper_tick | -9,276 | -4.61% |
| snake_viper_wild | -9,489 | -4.64% |

Average per day so far: unified Rs +512, benchmark Rs +505, intraweek Rs +376, snake_abs_exit_conv Rs +346, snake_abs_exit Rs +339, intramonth Rs +245, snake_abs_conv Rs +223, snake_abs Rs +221, oracle Rs +162, random_hold Rs +114, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -157, benchmark_smallcap Rs -213, snake_viper_wild Rs -230, gold Rs -342, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -452

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.