# Paper trading report

Updated 2026-11-18 09:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,746 | +10.87% | 0 | - | 236 |
| benchmark | 220,157 | +10.08% | 0 | - | 237 |
| intraweek | 213,213 | +6.61% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,606 | +6.30% | 2 | 50% | 345 |
| oracle | 211,862 | +5.93% | 0 | - | 233 |
| intramonth | 211,646 | +5.82% | 0 | - | 235 |
| snake_abs_exit_conv | 211,153 | +5.58% | 2 | 50% | 345 |
| snake_abs | 208,454 | +4.23% | 1 | 100% | 255 |
| snake_abs_conv | 208,307 | +4.15% | 1 | 100% | 255 |
| random_hold | 206,957 | +3.48% | 10 | 70% | 733 |
| snake_viper_wild | 206,868 | +3.43% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,335 | +1.67% | 15 | 47% | 2,625 |
| snake_anaconda | 203,298 | +1.65% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,337 | -11.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,827 (-4.59%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +308 | +0.14% |
| intramonth | +104 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs | -104 | -0.05% |
| intraweek | -110 | -0.05% |
| snake_abs_conv | -112 | -0.05% |
| snake_abs_exit_conv | -421 | -0.20% |
| snake_abs_exit | -536 | -0.25% |
| oracle | -624 | -0.29% |
| snake_anaconda | -757 | -0.37% |
| benchmark_smallcap | -964 | -0.48% |
| benchmark | -1,446 | -0.65% |
| random_hold | -1,476 | -0.71% |
| snake_viper_tick | -2,501 | -1.22% |
| snake_viper_wild | -2,547 | -1.22% |
| gold | -3,387 | -1.87% |

Average per day so far: unified Rs +604, benchmark Rs +560, snake_abs_exit Rs +382, intraweek Rs +367, snake_abs_exit_conv Rs +338, oracle Rs +329, intramonth Rs +323, snake_abs_conv Rs +252, snake_abs Rs +249, snake_viper_wild Rs +245, random_hold Rs +193, snake_viper_tick Rs +133, snake_anaconda Rs +106, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -12, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.