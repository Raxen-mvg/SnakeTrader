# Paper trading report

Updated 2026-11-06 10:27 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,057 | +7.53% | 0 | - | 236 |
| benchmark | 214,910 | +7.46% | 0 | - | 237 |
| intraweek | 210,755 | +5.38% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,809 | +4.91% | 1 | 100% | 255 |
| snake_abs_exit | 209,595 | +4.80% | 1 | 100% | 260 |
| intramonth | 207,065 | +3.53% | 0 | - | 235 |
| snake_abs | 206,760 | +3.38% | 1 | 100% | 255 |
| snake_abs_conv | 206,591 | +3.29% | 1 | 100% | 255 |
| oracle | 204,762 | +2.38% | 0 | - | 233 |
| random_hold | 203,473 | +1.74% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,068 | -0.97% | 3 | 33% | 702 |
| snake_anaconda | 196,959 | -1.52% | 3 | 33% | 374 |
| benchmark_smallcap | 195,258 | -2.37% | 0 | - | 237 |
| snake_viper_tick | 194,704 | -2.65% | 2 | 0% | 532 |
| gold | 190,292 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,588 (-6.21%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,337 | +0.64% |
| benchmark | +1,140 | +0.53% |
| oracle | +690 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -850 | -0.42% |
| intramonth | -883 | -0.42% |
| unified | -927 | -0.43% |
| benchmark_smallcap | -3,430 | -1.73% |
| gold | -3,929 | -2.02% |
| snake_abs | -4,929 | -2.33% |
| snake_abs_conv | -4,954 | -2.34% |
| snake_abs_exit_conv | -4,994 | -2.33% |
| snake_abs_exit | -5,064 | -2.36% |
| snake_anaconda | -5,520 | -2.73% |
| snake_viper_tick | -6,434 | -3.20% |
| snake_viper_wild | -6,588 | -3.22% |

Average per day so far: unified Rs +519, benchmark Rs +514, snake_abs_exit_conv Rs +377, intraweek Rs +371, snake_abs_exit Rs +369, snake_abs_conv Rs +253, snake_abs Rs +250, intramonth Rs +244, oracle Rs +164, random_hold Rs +120, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -92, snake_anaconda Rs -127, benchmark_smallcap Rs -190, snake_viper_tick Rs -294, gold Rs -335, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.