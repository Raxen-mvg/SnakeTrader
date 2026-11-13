# Paper trading report

Updated 2026-11-13 11:13 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,478 | +10.24% | 0 | - | 236 |
| benchmark | 219,729 | +9.87% | 0 | - | 237 |
| snake_abs_exit_conv | 216,545 | +8.27% | 2 | 50% | 345 |
| snake_abs_exit | 216,412 | +8.21% | 2 | 50% | 345 |
| intraweek | 215,952 | +7.98% | 30 | 53% | 3,302 |
| oracle | 213,487 | +6.74% | 0 | - | 233 |
| snake_abs | 212,604 | +6.30% | 1 | 100% | 255 |
| snake_abs_conv | 212,434 | +6.22% | 1 | 100% | 255 |
| intramonth | 211,307 | +5.65% | 0 | - | 235 |
| random_hold | 207,111 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 206,010 | +3.00% | 14 | 50% | 2,496 |
| snake_anaconda | 204,734 | +2.37% | 3 | 33% | 374 |
| benchmark_smallcap | 203,295 | +1.65% | 0 | - | 237 |
| snake_viper_tick | 202,486 | +1.24% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,111 | -7.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,001 (-4.00%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,294 | +0.60% |
| snake_viper_wild | +717 | +0.35% |
| snake_viper_tick | +704 | +0.35% |
| oracle | +371 | +0.17% |
| benchmark_smallcap | +90 | +0.04% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -219 | -0.10% |
| intramonth | -286 | -0.14% |
| benchmark | -819 | -0.37% |
| random_hold | -943 | -0.45% |
| snake_abs_exit | -1,031 | -0.47% |
| snake_anaconda | -1,193 | -0.58% |
| gold | -1,200 | -0.65% |
| snake_abs_exit_conv | -2,129 | -0.97% |
| snake_abs_conv | -3,101 | -1.44% |
| snake_abs | -3,107 | -1.44% |

Average per day so far: unified Rs +621, benchmark Rs +598, snake_abs_exit_conv Rs +552, snake_abs_exit Rs +547, intraweek Rs +483, snake_abs_conv Rs +414, oracle Rs +409, snake_abs Rs +407, intramonth Rs +343, snake_viper_wild Rs +240, random_hold Rs +215, snake_anaconda Rs +169, benchmark_smallcap Rs +114, snake_viper_tick Rs +113, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -481

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.