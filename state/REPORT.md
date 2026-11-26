# Paper trading report

Updated 2026-11-26 10:34 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,948 | +12.97% | 0 | - | 237 |
| unified | 223,510 | +11.76% | 0 | - | 236 |
| oracle | 213,034 | +6.52% | 0 | - | 233 |
| intramonth | 210,828 | +5.41% | 0 | - | 235 |
| random_hold | 209,948 | +4.97% | 13 | 69% | 1,037 |
| intraweek | 208,043 | +4.02% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,946 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,422 | +0.71% | 2 | 50% | 345 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,495 | -0.25% | 1 | 100% | 255 |
| snake_abs_conv | 199,311 | -0.34% | 1 | 100% | 255 |
| snake_anaconda | 193,324 | -3.34% | 3 | 33% | 374 |
| snake_viper_wild | 193,242 | -3.38% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,956 | -5.02% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,786 | -16.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,938 (-5.53%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,189 | +1.94% |
| benchmark_smallcap | +1,805 | +0.91% |
| intraweek | +1,300 | +0.63% |
| benchmark | +926 | +0.41% |
| random_hold | +455 | +0.22% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -309 | -0.15% |
| snake_abs_exit_conv | -554 | -0.27% |
| unified | -590 | -0.26% |
| snake_abs | -655 | -0.33% |
| snake_abs_conv | -661 | -0.33% |
| oracle | -761 | -0.36% |
| intramonth | -865 | -0.41% |
| snake_anaconda | -1,229 | -0.63% |
| snake_viper_tick | -4,221 | -2.17% |
| snake_viper_wild | -4,301 | -2.18% |

Average per day so far: benchmark Rs +633, unified Rs +573, oracle Rs +318, intramonth Rs +264, random_hold Rs +243, intraweek Rs +196, snake_abs_exit Rs +51, nifty_calls Rs +45, snake_abs_exit_conv Rs +37, benchmark_smallcap Rs +17, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -13, snake_abs_conv Rs -18, snake_anaconda Rs -185, snake_viper_wild Rs -205, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -335, gold Rs -786

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.