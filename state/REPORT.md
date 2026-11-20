# Paper trading report

Updated 2026-11-20 09:42 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,392 | +12.20% | 0 | - | 236 |
| benchmark | 222,062 | +11.03% | 0 | - | 237 |
| intramonth | 213,883 | +6.94% | 0 | - | 235 |
| intraweek | 213,383 | +6.69% | 35 | 54% | 3,851 |
| oracle | 212,557 | +6.28% | 0 | - | 233 |
| snake_abs_exit | 210,518 | +5.26% | 2 | 50% | 345 |
| random_hold | 208,534 | +4.27% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,356 | +4.18% | 2 | 50% | 345 |
| snake_abs | 206,835 | +3.42% | 1 | 100% | 255 |
| snake_abs_conv | 206,700 | +3.35% | 1 | 100% | 255 |
| snake_viper_wild | 205,617 | +2.81% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,111 | +1.06% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,282 | +0.64% | 3 | 33% | 374 |
| benchmark_smallcap | 200,022 | +0.01% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,356 | -16.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,391 (-4.30%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +494 | +0.23% |
| oracle | +469 | +0.22% |
| random_hold | +81 | +0.04% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intramonth | -125 | -0.06% |
| unified | -223 | -0.10% |
| benchmark | -314 | -0.14% |
| benchmark_smallcap | -1,446 | -0.72% |
| snake_viper_tick | -1,866 | -0.92% |
| snake_viper_wild | -1,906 | -0.92% |
| snake_abs | -2,145 | -1.03% |
| snake_abs_conv | -2,160 | -1.03% |
| snake_anaconda | -2,181 | -1.07% |
| snake_abs_exit_conv | -2,708 | -1.28% |
| snake_abs_exit | -2,833 | -1.33% |
| gold | -8,417 | -4.82% |

Average per day so far: unified Rs +642, benchmark Rs +581, intramonth Rs +365, intraweek Rs +352, oracle Rs +330, snake_abs_exit Rs +301, snake_abs_exit_conv Rs +239, random_hold Rs +225, snake_abs_conv Rs +191, snake_abs Rs +190, snake_viper_wild Rs +187, snake_viper_tick Rs +78, nifty_calls Rs +48, snake_anaconda Rs +39, benchmark_smallcap Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.