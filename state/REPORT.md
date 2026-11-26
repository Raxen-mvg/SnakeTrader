# Paper trading report

Updated 2026-11-26 14:15 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,069 | +12.53% | 0 | - | 237 |
| unified | 223,195 | +11.60% | 0 | - | 236 |
| oracle | 213,015 | +6.51% | 0 | - | 233 |
| intramonth | 210,446 | +5.22% | 0 | - | 235 |
| random_hold | 209,276 | +4.64% | 13 | 69% | 1,037 |
| intraweek | 207,802 | +3.90% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,403 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,870 | -0.07% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,274 | -0.36% | 2 | 50% | 345 |
| snake_abs | 197,648 | -1.18% | 1 | 100% | 255 |
| snake_abs_conv | 197,440 | -1.28% | 1 | 100% | 255 |
| snake_viper_wild | 192,359 | -3.82% | 16 | 50% | 2,827 |
| snake_anaconda | 191,402 | -4.30% | 3 | 33% | 374 |
| snake_viper_tick | 189,092 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,421 | -16.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,523 (-5.74%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,825 | +1.11% |
| benchmark_smallcap | +1,592 | +0.80% |
| intraweek | +1,059 | +0.51% |
| benchmark | +46 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -217 | -0.10% |
| oracle | -781 | -0.36% |
| unified | -905 | -0.40% |
| intramonth | -1,247 | -0.59% |
| snake_abs_exit | -2,385 | -1.18% |
| snake_abs | -2,502 | -1.25% |
| snake_abs_conv | -2,532 | -1.27% |
| snake_abs_exit_conv | -2,702 | -1.34% |
| snake_anaconda | -3,151 | -1.62% |
| snake_viper_tick | -5,085 | -2.62% |
| snake_viper_wild | -5,184 | -2.62% |

Average per day so far: benchmark Rs +611, unified Rs +566, oracle Rs +317, intramonth Rs +255, random_hold Rs +226, intraweek Rs +190, nifty_calls Rs +45, benchmark_smallcap Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -3, snake_abs_exit_conv Rs -19, snake_abs Rs -60, snake_abs_conv Rs -67, snake_viper_wild Rs -232, snake_anaconda Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -819

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.