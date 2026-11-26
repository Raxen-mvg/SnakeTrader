# Paper trading report

Updated 2026-11-26 13:07 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,933 | +12.97% | 0 | - | 237 |
| unified | 223,440 | +11.72% | 0 | - | 236 |
| oracle | 213,212 | +6.61% | 0 | - | 233 |
| intramonth | 210,527 | +5.26% | 0 | - | 235 |
| random_hold | 210,023 | +5.01% | 13 | 69% | 1,037 |
| intraweek | 208,244 | +4.12% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,694 | +0.35% | 0 | - | 237 |
| snake_abs_exit | 200,327 | +0.16% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,759 | -0.12% | 2 | 50% | 345 |
| snake_abs | 198,124 | -0.94% | 1 | 100% | 255 |
| snake_abs_conv | 197,923 | -1.04% | 1 | 100% | 255 |
| snake_viper_wild | 191,850 | -4.08% | 16 | 50% | 2,827 |
| snake_anaconda | 191,805 | -4.10% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,593 | -5.70% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,454 | -16.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,832 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,883 | +0.95% |
| gold | +1,858 | +1.13% |
| intraweek | +1,501 | +0.73% |
| benchmark | +910 | +0.41% |
| random_hold | +530 | +0.25% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -583 | -0.27% |
| unified | -659 | -0.29% |
| intramonth | -1,167 | -0.55% |
| snake_abs_exit | -1,928 | -0.95% |
| snake_abs | -2,026 | -1.01% |
| snake_abs_conv | -2,049 | -1.02% |
| snake_abs_exit_conv | -2,216 | -1.10% |
| snake_anaconda | -2,748 | -1.41% |
| snake_viper_tick | -5,584 | -2.88% |
| snake_viper_wild | -5,693 | -2.88% |

Average per day so far: benchmark Rs +633, unified Rs +572, oracle Rs +322, intramonth Rs +257, random_hold Rs +244, intraweek Rs +201, nifty_calls Rs +45, benchmark_smallcap Rs +19, snake_abs_exit Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -6, snake_abs Rs -48, snake_abs_conv Rs -55, snake_anaconda Rs -228, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -380, gold Rs -818

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.