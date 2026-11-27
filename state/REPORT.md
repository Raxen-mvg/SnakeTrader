# Paper trading report

Updated 2026-11-27 10:46 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,969 | +12.48% | 0 | - | 237 |
| unified | 222,926 | +11.46% | 0 | - | 236 |
| oracle | 212,285 | +6.14% | 0 | - | 233 |
| intramonth | 210,685 | +5.34% | 0 | - | 235 |
| random_hold | 209,797 | +4.90% | 13 | 69% | 1,037 |
| intraweek | 207,793 | +3.90% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,639 | +2.82% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,401 | +2.20% | 2 | 50% | 345 |
| benchmark_smallcap | 202,174 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,263 | +0.63% | 1 | 100% | 255 |
| snake_abs_conv | 201,087 | +0.54% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,723 | -2.64% | 3 | 33% | 374 |
| snake_viper_wild | 193,772 | -3.11% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,475 | -4.76% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,723 | -15.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,690 (-5.66%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,561 | +2.27% |
| snake_abs_exit_conv | +4,004 | +2.00% |
| gold | +2,729 | +1.64% |
| snake_abs_conv | +2,721 | +1.37% |
| snake_abs | +2,711 | +1.36% |
| snake_anaconda | +2,427 | +1.26% |
| snake_viper_wild | +1,566 | +0.81% |
| snake_viper_tick | +1,534 | +0.81% |
| benchmark_smallcap | +1,334 | +0.66% |
| random_hold | +1,203 | +0.58% |
| intraweek | +744 | +0.36% |
| intramonth | +152 | +0.07% |
| oracle | +49 | +0.02% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -152 | -0.07% |
| benchmark | -1,017 | -0.45% |

Average per day so far: benchmark Rs +595, unified Rs +546, oracle Rs +292, intramonth Rs +254, random_hold Rs +233, intraweek Rs +186, snake_abs_exit Rs +145, snake_abs_exit_conv Rs +113, benchmark_smallcap Rs +57, nifty_calls Rs +44, snake_abs Rs +32, snake_abs_conv Rs +28, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -143, snake_viper_wild Rs -183, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -307, gold Rs -745

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.