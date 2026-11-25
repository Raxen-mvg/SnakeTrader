# Paper trading report

Updated 2026-11-25 11:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,079 | +13.04% | 0 | - | 237 |
| unified | 225,385 | +12.69% | 0 | - | 236 |
| intramonth | 213,110 | +6.55% | 0 | - | 235 |
| oracle | 212,637 | +6.32% | 0 | - | 233 |
| random_hold | 209,595 | +4.80% | 12 | 75% | 1,009 |
| intraweek | 207,653 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,456 | +1.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,896 | +0.95% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,318 | +0.66% | 1 | 100% | 255 |
| snake_abs_conv | 201,131 | +0.57% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_viper_wild | 196,794 | -1.60% | 16 | 50% | 2,827 |
| snake_anaconda | 194,062 | -2.97% | 3 | 33% | 374 |
| snake_viper_tick | 193,444 | -3.28% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,547 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,472 (-5.26%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,605 | +2.08% |
| random_hold | +1,169 | +0.56% |
| unified | +1,100 | +0.49% |
| benchmark_smallcap | +628 | +0.32% |
| intramonth | +359 | +0.17% |
| oracle | +295 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,966 | -1.87% |
| snake_abs | -4,143 | -2.02% |
| snake_abs_conv | -4,171 | -2.03% |
| snake_viper_tick | -4,249 | -2.15% |
| snake_viper_wild | -4,330 | -2.15% |
| snake_anaconda | -4,641 | -2.34% |
| gold | -4,883 | -2.88% |
| snake_abs_exit | -5,039 | -2.43% |
| snake_abs_exit_conv | -5,150 | -2.49% |

Average per day so far: benchmark Rs +652, unified Rs +635, intramonth Rs +328, oracle Rs +316, random_hold Rs +240, intraweek Rs +191, snake_abs_exit Rs +66, snake_abs_exit_conv Rs +51, nifty_calls Rs +46, snake_abs Rs +35, snake_abs_conv Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_viper_wild Rs -100, snake_anaconda Rs -170, snake_viper_tick Rs -226, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.