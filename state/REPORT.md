# Paper trading report

Updated 2026-11-09 12:15 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,093 | +10.05% | 0 | - | 236 |
| benchmark | 217,419 | +8.71% | 0 | - | 237 |
| intraweek | 214,170 | +7.08% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,385 | +6.19% | 2 | 50% | 330 |
| snake_abs_exit | 211,930 | +5.96% | 2 | 50% | 308 |
| intramonth | 210,204 | +5.10% | 0 | - | 235 |
| snake_abs | 209,702 | +4.85% | 1 | 100% | 255 |
| snake_abs_conv | 209,525 | +4.76% | 1 | 100% | 255 |
| oracle | 209,278 | +4.64% | 0 | - | 233 |
| random_hold | 204,361 | +2.18% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,397 | -0.30% | 3 | 33% | 374 |
| snake_viper_wild | 199,359 | -0.32% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,677 | -0.66% | 0 | - | 237 |
| snake_viper_tick | 195,972 | -2.01% | 6 | 50% | 1,154 |
| gold | 192,643 | -3.68% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,185 (-4.91%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,484 | +2.08% |
| snake_abs_conv | +4,298 | +2.09% |
| snake_abs | +4,283 | +2.08% |
| snake_abs_exit_conv | +3,963 | +1.90% |
| intraweek | +3,808 | +1.81% |
| snake_abs_exit | +3,618 | +1.74% |
| snake_anaconda | +3,570 | +1.82% |
| oracle | +3,452 | +1.68% |
| snake_viper_wild | +3,322 | +1.69% |
| snake_viper_tick | +3,262 | +1.69% |
| intramonth | +2,601 | +1.25% |
| benchmark_smallcap | +1,883 | +0.96% |
| gold | +1,595 | +0.83% |
| random_hold | +454 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -69 | -0.03% |

Average per day so far: unified Rs +670, benchmark Rs +581, intraweek Rs +472, snake_abs_exit_conv Rs +459, snake_abs_exit Rs +442, snake_abs_conv Rs +353, snake_abs Rs +347, intramonth Rs +340, oracle Rs +309, random_hold Rs +145, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -24, snake_viper_wild Rs -29, benchmark_smallcap Rs -51, snake_viper_tick Rs -212, gold Rs -245, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.