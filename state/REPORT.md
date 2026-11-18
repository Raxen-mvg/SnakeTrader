# Paper trading report

Updated 2026-11-18 11:37 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,121 | +11.56% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| intraweek | 214,381 | +7.19% | 35 | 54% | 3,851 |
| intramonth | 213,008 | +6.50% | 0 | - | 235 |
| oracle | 212,766 | +6.38% | 0 | - | 233 |
| snake_abs_exit | 212,614 | +6.31% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,035 | +5.52% | 2 | 50% | 345 |
| snake_abs | 208,002 | +4.00% | 1 | 100% | 255 |
| snake_abs_conv | 207,864 | +3.93% | 1 | 100% | 255 |
| random_hold | 207,561 | +3.78% | 10 | 70% | 733 |
| snake_viper_wild | 206,881 | +3.44% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,348 | +1.67% | 15 | 47% | 2,625 |
| snake_anaconda | 203,076 | +1.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,641 | -0.18% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,321 | -11.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,727 (-4.14%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,682 | +0.76% |
| intramonth | +1,466 | +0.69% |
| intraweek | +1,058 | +0.50% |
| oracle | +280 | +0.13% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -528 | -0.25% |
| snake_abs_exit_conv | -539 | -0.26% |
| snake_abs_conv | -556 | -0.27% |
| snake_abs | -557 | -0.27% |
| random_hold | -872 | -0.42% |
| benchmark_smallcap | -930 | -0.46% |
| snake_anaconda | -979 | -0.48% |
| benchmark | -1,224 | -0.55% |
| snake_viper_tick | -2,488 | -1.21% |
| snake_viper_wild | -2,534 | -1.21% |
| gold | -3,403 | -1.88% |

Average per day so far: unified Rs +642, benchmark Rs +566, intraweek Rs +399, snake_abs_exit Rs +382, intramonth Rs +361, oracle Rs +355, snake_abs_exit_conv Rs +334, snake_viper_wild Rs +246, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +210, snake_viper_tick Rs +134, snake_anaconda Rs +99, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.