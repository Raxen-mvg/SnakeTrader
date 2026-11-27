# Paper trading report

Updated 2026-11-27 09:52 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,367 | +12.68% | 0 | - | 237 |
| unified | 223,353 | +11.68% | 0 | - | 236 |
| oracle | 212,392 | +6.20% | 0 | - | 233 |
| intramonth | 210,974 | +5.49% | 0 | - | 235 |
| random_hold | 209,650 | +4.83% | 13 | 69% | 1,037 |
| intraweek | 207,746 | +3.87% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,605 | +2.80% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,402 | +2.20% | 2 | 50% | 345 |
| benchmark_smallcap | 202,141 | +1.07% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,353 | +0.68% | 1 | 100% | 255 |
| snake_abs_conv | 201,174 | +0.59% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,957 | -2.52% | 3 | 33% | 374 |
| snake_viper_wild | 192,935 | -3.53% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,656 | -5.17% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,476 | -15.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,798 (-5.60%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,528 | +2.25% |
| snake_abs_exit_conv | +4,005 | +2.00% |
| snake_abs_conv | +2,808 | +1.42% |
| snake_abs | +2,801 | +1.41% |
| snake_anaconda | +2,661 | +1.38% |
| gold | +2,482 | +1.50% |
| benchmark_smallcap | +1,300 | +0.65% |
| random_hold | +1,056 | +0.51% |
| snake_viper_wild | +730 | +0.38% |
| snake_viper_tick | +714 | +0.38% |
| intraweek | +698 | +0.34% |
| intramonth | +441 | +0.21% |
| unified | +275 | +0.12% |
| oracle | +156 | +0.07% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -620 | -0.27% |

Average per day so far: benchmark Rs +604, unified Rs +556, oracle Rs +295, intramonth Rs +261, random_hold Rs +230, intraweek Rs +184, snake_abs_exit Rs +144, snake_abs_exit_conv Rs +113, benchmark_smallcap Rs +56, nifty_calls Rs +44, snake_abs Rs +34, snake_abs_conv Rs +30, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -136, snake_viper_wild Rs -208, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -334, gold Rs -751

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.