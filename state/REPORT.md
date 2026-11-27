# Paper trading report

Updated 2026-11-27 15:19 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,424 | +11.71% | 0 | - | 237 |
| unified | 222,991 | +11.50% | 0 | - | 236 |
| oracle | 211,476 | +5.74% | 0 | - | 233 |
| random_hold | 211,278 | +5.64% | 13 | 69% | 1,037 |
| intramonth | 210,824 | +5.41% | 0 | - | 235 |
| intraweek | 207,768 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,415 | +3.21% | 2 | 50% | 345 |
| snake_abs_exit | 204,193 | +2.10% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,221 | +0.61% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,644 | -0.18% | 1 | 100% | 255 |
| snake_abs_conv | 199,453 | -0.27% | 1 | 100% | 255 |
| snake_anaconda | 192,829 | -3.58% | 3 | 33% | 374 |
| snake_viper_wild | 192,394 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,127 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,646 | -14.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,729 (-5.64%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,018 | +3.00% |
| gold | +4,653 | +2.80% |
| snake_abs_exit | +3,115 | +1.55% |
| random_hold | +2,684 | +1.29% |
| snake_abs | +1,091 | +0.55% |
| snake_abs_conv | +1,087 | +0.55% |
| intraweek | +720 | +0.35% |
| snake_anaconda | +533 | +0.28% |
| benchmark_smallcap | +381 | +0.19% |
| intramonth | +291 | +0.14% |
| snake_viper_wild | +189 | +0.10% |
| snake_viper_tick | +185 | +0.10% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -88 | -0.04% |
| oracle | -759 | -0.36% |
| benchmark | -2,563 | -1.13% |

Average per day so far: benchmark Rs +558, unified Rs +547, oracle Rs +273, random_hold Rs +269, intramonth Rs +258, intraweek Rs +185, snake_abs_exit_conv Rs +164, snake_abs_exit Rs +108, nifty_calls Rs +44, benchmark_smallcap Rs +32, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -9, snake_abs_conv Rs -14, snake_anaconda Rs -194, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -699

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.