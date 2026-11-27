# Paper trading report

Updated 2026-11-27 13:16 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,028 | +12.01% | 0 | - | 237 |
| unified | 223,353 | +11.68% | 0 | - | 236 |
| oracle | 211,825 | +5.91% | 0 | - | 233 |
| intramonth | 210,960 | +5.48% | 0 | - | 235 |
| random_hold | 210,665 | +5.33% | 13 | 69% | 1,037 |
| intraweek | 208,449 | +4.22% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,016 | +2.51% | 2 | 50% | 345 |
| snake_abs_exit | 204,272 | +2.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,289 | +0.64% | 0 | - | 237 |
| snake_abs | 200,027 | +0.01% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,845 | -0.08% | 1 | 100% | 255 |
| snake_anaconda | 193,391 | -3.31% | 3 | 33% | 374 |
| snake_viper_wild | 191,665 | -4.17% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,412 | -5.79% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,851 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,619 | +2.31% |
| gold | +3,551 | +2.14% |
| snake_abs_exit | +3,194 | +1.59% |
| random_hold | +2,071 | +0.99% |
| snake_abs_conv | +1,478 | +0.74% |
| snake_abs | +1,475 | +0.74% |
| intraweek | +1,400 | +0.68% |
| snake_anaconda | +1,095 | +0.57% |
| benchmark_smallcap | +448 | +0.22% |
| intramonth | +426 | +0.20% |
| unified | +275 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -410 | -0.19% |
| snake_viper_tick | -529 | -0.28% |
| snake_viper_wild | -541 | -0.28% |
| benchmark | -1,958 | -0.87% |

Average per day so far: benchmark Rs +572, unified Rs +556, oracle Rs +282, intramonth Rs +261, random_hold Rs +254, intraweek Rs +201, snake_abs_exit_conv Rs +129, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +34, snake_abs Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_conv Rs -4, snake_anaconda Rs -179, snake_viper_wild Rs -245, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -374, gold Rs -725

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.