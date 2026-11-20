# Paper trading report

Updated 2026-11-20 10:55 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,229 | +12.62% | 0 | - | 236 |
| benchmark | 223,064 | +11.53% | 0 | - | 237 |
| intramonth | 214,197 | +7.10% | 0 | - | 235 |
| intraweek | 213,666 | +6.83% | 35 | 54% | 3,851 |
| oracle | 212,909 | +6.45% | 0 | - | 233 |
| snake_abs_exit | 210,842 | +5.42% | 2 | 50% | 345 |
| random_hold | 209,130 | +4.57% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,417 | +4.21% | 2 | 50% | 345 |
| snake_abs | 207,558 | +3.78% | 1 | 100% | 255 |
| snake_abs_conv | 207,419 | +3.71% | 1 | 100% | 255 |
| snake_viper_wild | 206,829 | +3.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,298 | +1.65% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,619 | +0.81% | 3 | 33% | 374 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,975 | -17.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,844 (-4.08%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +820 | +0.39% |
| intraweek | +776 | +0.36% |
| benchmark | +689 | +0.31% |
| random_hold | +676 | +0.33% |
| unified | +614 | +0.27% |
| intramonth | +189 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -679 | -0.33% |
| snake_viper_wild | -694 | -0.33% |
| benchmark_smallcap | -1,076 | -0.53% |
| snake_abs | -1,422 | -0.68% |
| snake_abs_conv | -1,441 | -0.69% |
| snake_anaconda | -1,844 | -0.91% |
| snake_abs_exit | -2,509 | -1.18% |
| snake_abs_exit_conv | -2,648 | -1.25% |
| gold | -9,798 | -5.61% |

Average per day so far: unified Rs +664, benchmark Rs +607, intramonth Rs +374, intraweek Rs +360, oracle Rs +340, snake_abs_exit Rs +310, snake_abs_exit_conv Rs +240, random_hold Rs +240, snake_viper_wild Rs +228, snake_abs_conv Rs +212, snake_abs Rs +210, snake_viper_tick Rs +122, snake_anaconda Rs +49, nifty_calls Rs +48, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -922

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.