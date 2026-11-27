# Paper trading report

Updated 2026-11-27 11:07 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,549 | +12.27% | 0 | - | 237 |
| unified | 222,480 | +11.24% | 0 | - | 236 |
| oracle | 212,146 | +6.07% | 0 | - | 233 |
| intramonth | 210,190 | +5.09% | 0 | - | 235 |
| random_hold | 209,949 | +4.97% | 13 | 69% | 1,037 |
| intraweek | 207,738 | +3.87% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,283 | +2.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,011 | +2.01% | 2 | 50% | 345 |
| benchmark_smallcap | 202,107 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,946 | +0.47% | 1 | 100% | 255 |
| snake_abs_conv | 200,769 | +0.38% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,515 | -2.74% | 3 | 33% | 374 |
| snake_viper_wild | 193,359 | -3.32% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,071 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,265 | -15.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,527 (-5.74%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,206 | +2.09% |
| snake_abs_exit_conv | +3,614 | +1.80% |
| gold | +3,272 | +1.97% |
| snake_abs_conv | +2,402 | +1.21% |
| snake_abs | +2,393 | +1.21% |
| snake_anaconda | +2,219 | +1.15% |
| random_hold | +1,355 | +0.65% |
| benchmark_smallcap | +1,267 | +0.63% |
| snake_viper_wild | +1,154 | +0.60% |
| snake_viper_tick | +1,130 | +0.60% |
| intraweek | +689 | +0.33% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -90 | -0.04% |
| intramonth | -343 | -0.16% |
| unified | -598 | -0.27% |
| benchmark | -1,438 | -0.64% |

Average per day so far: benchmark Rs +584, unified Rs +535, oracle Rs +289, intramonth Rs +243, random_hold Rs +237, intraweek Rs +184, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +103, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +24, snake_abs_conv Rs +20, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -148, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -320, gold Rs -732

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.