# Paper trading report

Updated 2026-11-19 09:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,481 | +12.24% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| intramonth | 214,221 | +7.11% | 0 | - | 235 |
| snake_abs_exit | 214,185 | +7.09% | 2 | 50% | 345 |
| intraweek | 212,367 | +6.18% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,232 | +6.12% | 2 | 50% | 345 |
| oracle | 211,832 | +5.92% | 0 | - | 233 |
| snake_abs | 209,465 | +4.73% | 1 | 100% | 255 |
| snake_abs_conv | 209,345 | +4.67% | 1 | 100% | 255 |
| random_hold | 208,188 | +4.09% | 10 | 70% | 733 |
| snake_viper_wild | 207,591 | +3.80% | 16 | 50% | 2,827 |
| snake_anaconda | 204,164 | +2.08% | 3 | 33% | 374 |
| snake_viper_tick | 204,044 | +2.02% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,851 (-4.07%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,947 | +0.92% |
| unified | +1,869 | +0.84% |
| benchmark_smallcap | +1,289 | +0.65% |
| random_hold | +1,256 | +0.61% |
| oracle | +1,036 | +0.49% |
| snake_viper_wild | +552 | +0.27% |
| snake_viper_tick | +540 | +0.27% |
| intraweek | +527 | +0.25% |
| snake_abs_exit | +154 | +0.07% |
| snake_abs | +28 | +0.01% |
| snake_abs_conv | +20 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| benchmark | -31 | -0.01% |
| snake_abs_exit_conv | -152 | -0.07% |
| snake_anaconda | -237 | -0.12% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +662, benchmark Rs +548, snake_abs_exit Rs +417, intramonth Rs +384, snake_abs_exit_conv Rs +360, intraweek Rs +334, oracle Rs +320, snake_abs_conv Rs +275, snake_abs Rs +270, snake_viper_wild Rs +262, random_hold Rs +221, snake_viper_tick Rs +156, snake_anaconda Rs +130, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.