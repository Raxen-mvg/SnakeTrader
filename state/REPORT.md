# Paper trading report

Updated 2026-11-25 12:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,765 | +12.38% | 0 | - | 236 |
| benchmark | 224,549 | +12.27% | 0 | - | 237 |
| intramonth | 212,773 | +6.39% | 0 | - | 235 |
| oracle | 212,681 | +6.34% | 0 | - | 233 |
| random_hold | 209,996 | +5.00% | 12 | 75% | 1,009 |
| intraweek | 208,489 | +4.25% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,908 | +0.95% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,616 | +0.81% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,905 | -0.05% | 1 | 100% | 255 |
| snake_abs_conv | 199,726 | -0.14% | 1 | 100% | 255 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_viper_wild | 196,742 | -1.63% | 16 | 50% | 2,827 |
| snake_anaconda | 193,632 | -3.18% | 3 | 33% | 374 |
| snake_viper_tick | 193,392 | -3.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,596 | -17.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,322 (-5.34%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,075 | +1.39% |
| random_hold | +1,570 | +0.75% |
| unified | +480 | +0.21% |
| oracle | +338 | +0.16% |
| benchmark_smallcap | +202 | +0.10% |
| intramonth | +22 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,130 | -1.48% |
| snake_viper_tick | -4,301 | -2.17% |
| snake_viper_wild | -4,383 | -2.18% |
| gold | -4,833 | -2.85% |
| snake_anaconda | -5,071 | -2.55% |
| snake_abs_exit_conv | -5,430 | -2.62% |
| snake_abs | -5,556 | -2.70% |
| snake_abs_conv | -5,577 | -2.72% |
| snake_abs_exit | -5,587 | -2.69% |

Average per day so far: unified Rs +619, benchmark Rs +614, intramonth Rs +319, oracle Rs +317, random_hold Rs +250, intraweek Rs +212, snake_abs_exit Rs +52, nifty_calls Rs +46, snake_abs_exit_conv Rs +44, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -3, snake_abs_conv Rs -7, benchmark_smallcap Rs -23, snake_viper_wild Rs -102, snake_anaconda Rs -182, snake_viper_tick Rs -228, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.