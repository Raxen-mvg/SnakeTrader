# Paper trading report

Updated 2026-11-06 11:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,752 | +7.38% | 0 | - | 236 |
| benchmark | 214,626 | +7.31% | 0 | - | 237 |
| intraweek | 210,931 | +5.47% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,764 | +4.88% | 1 | 100% | 255 |
| snake_abs_exit | 209,550 | +4.78% | 1 | 100% | 260 |
| intramonth | 206,840 | +3.42% | 0 | - | 235 |
| snake_abs | 206,718 | +3.36% | 1 | 100% | 255 |
| snake_abs_conv | 206,548 | +3.27% | 1 | 100% | 255 |
| oracle | 204,904 | +2.45% | 0 | - | 233 |
| random_hold | 203,496 | +1.75% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,959 | -1.52% | 3 | 33% | 374 |
| snake_viper_wild | 196,586 | -1.71% | 3 | 33% | 702 |
| benchmark_smallcap | 194,720 | -2.64% | 0 | - | 237 |
| snake_viper_tick | 193,258 | -3.37% | 2 | 0% | 532 |
| gold | 189,947 | -5.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,479 (-6.26%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,513 | +0.72% |
| benchmark | +857 | +0.40% |
| oracle | +832 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -827 | -0.41% |
| intramonth | -1,109 | -0.53% |
| unified | -1,232 | -0.57% |
| benchmark_smallcap | -3,968 | -2.00% |
| gold | -4,274 | -2.20% |
| snake_abs | -4,971 | -2.35% |
| snake_abs_conv | -4,997 | -2.36% |
| snake_abs_exit_conv | -5,040 | -2.35% |
| snake_abs_exit | -5,108 | -2.38% |
| snake_anaconda | -5,520 | -2.73% |
| snake_viper_tick | -7,880 | -3.92% |
| snake_viper_wild | -8,070 | -3.94% |

Average per day so far: unified Rs +509, benchmark Rs +504, intraweek Rs +377, snake_abs_exit_conv Rs +376, snake_abs_exit Rs +367, snake_abs_conv Rs +252, snake_abs Rs +249, intramonth Rs +236, oracle Rs +169, random_hold Rs +121, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -127, snake_viper_wild Rs -163, benchmark_smallcap Rs -211, gold Rs -347, snake_viper_tick Rs -375, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.