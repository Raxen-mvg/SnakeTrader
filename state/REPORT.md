# Paper trading report

Updated 2026-11-09 12:53 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,064 | +10.03% | 0 | - | 236 |
| benchmark | 217,319 | +8.66% | 0 | - | 237 |
| intraweek | 214,819 | +7.41% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,262 | +6.13% | 2 | 50% | 330 |
| snake_abs_exit | 211,930 | +5.96% | 2 | 50% | 308 |
| intramonth | 210,135 | +5.07% | 0 | - | 235 |
| snake_abs | 209,626 | +4.81% | 1 | 100% | 255 |
| oracle | 209,506 | +4.75% | 0 | - | 233 |
| snake_abs_conv | 209,447 | +4.72% | 1 | 100% | 255 |
| random_hold | 204,499 | +2.25% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,614 | -0.19% | 7 | 57% | 1,332 |
| snake_anaconda | 199,371 | -0.32% | 3 | 33% | 374 |
| benchmark_smallcap | 198,609 | -0.69% | 0 | - | 237 |
| snake_viper_tick | 196,225 | -1.89% | 6 | 50% | 1,154 |
| gold | 192,479 | -3.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,326 (-4.84%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,457 | +2.12% |
| unified | +4,455 | +2.07% |
| snake_abs_conv | +4,220 | +2.06% |
| snake_abs | +4,207 | +2.05% |
| snake_abs_exit_conv | +3,840 | +1.84% |
| oracle | +3,679 | +1.79% |
| snake_abs_exit | +3,619 | +1.74% |
| snake_viper_wild | +3,577 | +1.82% |
| snake_anaconda | +3,544 | +1.81% |
| snake_viper_tick | +3,515 | +1.82% |
| intramonth | +2,532 | +1.22% |
| benchmark_smallcap | +1,816 | +0.92% |
| gold | +1,430 | +0.75% |
| random_hold | +593 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -168 | -0.08% |

Average per day so far: unified Rs +669, benchmark Rs +577, intraweek Rs +494, snake_abs_exit_conv Rs +454, snake_abs_exit Rs +442, snake_abs_conv Rs +350, snake_abs Rs +344, intramonth Rs +338, oracle Rs +317, random_hold Rs +150, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -18, snake_anaconda Rs -25, benchmark_smallcap Rs -53, snake_viper_tick Rs -199, gold Rs -251, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.