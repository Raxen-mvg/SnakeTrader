# Paper trading report

Updated 2026-11-04 15:04 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,510 | +7.25% | 0 | - | 236 |
| snake_abs_exit_conv | 214,457 | +7.23% | 1 | 100% | 255 |
| snake_abs_exit | 214,334 | +7.17% | 1 | 100% | 260 |
| snake_abs | 211,336 | +5.67% | 1 | 100% | 255 |
| snake_abs_conv | 211,195 | +5.60% | 1 | 100% | 255 |
| intraweek | 209,613 | +4.81% | 25 | 48% | 2,757 |
| benchmark | 208,644 | +4.32% | 0 | - | 237 |
| snake_viper_wild | 208,561 | +4.28% | 3 | 33% | 702 |
| intramonth | 206,978 | +3.49% | 0 | - | 235 |
| snake_viper_tick | 204,935 | +2.47% | 2 | 0% | 532 |
| snake_anaconda | 203,155 | +1.58% | 3 | 33% | 361 |
| random_hold | 202,943 | +1.47% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,567 | +0.78% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,536 | -1.73% | 0 | - | 237 |
| gold | 191,427 | -4.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,987 (-5.01%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +10,319 | +5.06% |
| snake_abs_exit_conv | +10,119 | +4.95% |
| snake_abs_conv | +10,054 | +5.00% |
| snake_abs | +10,027 | +4.98% |
| snake_anaconda | +9,331 | +4.81% |
| gold | +6,149 | +3.32% |
| intraweek | +4,528 | +2.21% |
| benchmark_smallcap | +3,598 | +1.86% |
| intramonth | +3,007 | +1.47% |
| unified | +2,509 | +1.18% |
| random_hold | +2,475 | +1.24% |
| benchmark | +1,943 | +0.94% |
| oracle | +1,577 | +0.79% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,231 | -1.08% |
| snake_viper_wild | -2,331 | -1.10% |

Average per day so far: snake_abs_exit_conv Rs +602, snake_abs_exit Rs +597, unified Rs +537, snake_abs_conv Rs +466, snake_abs Rs +453, snake_viper_wild Rs +451, intraweek Rs +356, benchmark Rs +320, snake_viper_tick Rs +308, intramonth Rs +258, snake_anaconda Rs +143, random_hold Rs +109, nifty_calls Rs +68, oracle Rs +58, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -151, gold Rs -318, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.