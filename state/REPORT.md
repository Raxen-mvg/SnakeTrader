# Paper trading report

Updated 2026-11-25 10:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,905 | +12.45% | 0 | - | 236 |
| benchmark | 224,449 | +12.22% | 0 | - | 237 |
| oracle | 212,623 | +6.31% | 0 | - | 233 |
| intramonth | 212,425 | +6.21% | 0 | - | 235 |
| random_hold | 209,442 | +4.72% | 12 | 75% | 1,009 |
| intraweek | 208,495 | +4.25% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,023 | +1.01% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,368 | +0.68% | 2 | 50% | 345 |
| snake_abs | 201,034 | +0.52% | 1 | 100% | 255 |
| snake_abs_conv | 200,847 | +0.42% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,192 | -0.40% | 0 | - | 237 |
| snake_viper_wild | 197,817 | -1.09% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,454 | -2.77% | 15 | 47% | 2,625 |
| snake_anaconda | 193,792 | -3.10% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,501 | -17.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,309 (-5.35%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,976 | +1.34% |
| random_hold | +1,016 | +0.49% |
| unified | +619 | +0.28% |
| oracle | +280 | +0.13% |
| benchmark_smallcap | +213 | +0.11% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -326 | -0.15% |
| intraweek | -3,124 | -1.48% |
| snake_viper_tick | -3,238 | -1.64% |
| snake_viper_wild | -3,307 | -1.64% |
| gold | -3,929 | -2.32% |
| snake_abs | -4,427 | -2.15% |
| snake_abs_conv | -4,455 | -2.17% |
| snake_anaconda | -4,911 | -2.47% |
| snake_abs_exit | -5,472 | -2.64% |
| snake_abs_exit_conv | -5,678 | -2.74% |

Average per day so far: unified Rs +623, benchmark Rs +611, oracle Rs +316, intramonth Rs +311, random_hold Rs +236, intraweek Rs +212, snake_abs_exit Rs +55, nifty_calls Rs +46, snake_abs_exit_conv Rs +37, snake_abs Rs +27, snake_abs_conv Rs +23, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_viper_wild Rs -68, snake_anaconda Rs -177, snake_viper_tick Rs -191, snake_nonews Rs -292, snake Rs -311, gold Rs -862

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.