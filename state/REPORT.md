# Paper trading report

Updated 2026-11-19 15:15 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,444 | +12.22% | 0 | - | 236 |
| benchmark | 222,636 | +11.32% | 0 | - | 237 |
| intramonth | 213,873 | +6.94% | 0 | - | 235 |
| snake_abs_exit | 213,401 | +6.70% | 2 | 50% | 345 |
| intraweek | 212,802 | +6.40% | 35 | 54% | 3,851 |
| oracle | 211,870 | +5.93% | 0 | - | 233 |
| snake_abs_exit_conv | 211,118 | +5.56% | 2 | 50% | 345 |
| snake_abs | 208,904 | +4.45% | 1 | 100% | 255 |
| snake_abs_conv | 208,785 | +4.39% | 1 | 100% | 255 |
| random_hold | 208,417 | +4.21% | 10 | 70% | 733 |
| snake_viper_wild | 207,547 | +3.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,000 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,458 | +1.73% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,773 | -12.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,871 (-4.06%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,354 | +1.18% |
| benchmark | +2,341 | +1.06% |
| unified | +1,833 | +0.82% |
| intramonth | +1,599 | +0.75% |
| random_hold | +1,485 | +0.72% |
| oracle | +1,074 | +0.51% |
| intraweek | +962 | +0.45% |
| snake_viper_wild | +507 | +0.24% |
| snake_viper_tick | +497 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -532 | -0.25% |
| snake_abs_conv | -539 | -0.26% |
| snake_abs_exit | -631 | -0.29% |
| snake_anaconda | -943 | -0.46% |
| snake_abs_exit_conv | -1,266 | -0.60% |
| gold | -2,548 | -1.44% |

Average per day so far: unified Rs +661, benchmark Rs +612, snake_abs_exit Rs +394, intramonth Rs +375, intraweek Rs +346, snake_abs_exit_conv Rs +327, oracle Rs +321, snake_viper_wild Rs +260, snake_abs_conv Rs +258, snake_abs Rs +254, random_hold Rs +227, snake_viper_tick Rs +154, snake_anaconda Rs +108, benchmark_smallcap Rs +51, nifty_calls Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -682

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.