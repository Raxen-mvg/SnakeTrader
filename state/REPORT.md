# Paper trading report

Updated 2026-11-18 14:35 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,394 | +11.20% | 0 | - | 236 |
| benchmark | 220,479 | +10.24% | 0 | - | 237 |
| snake_abs_exit | 214,449 | +7.22% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,657 | +6.33% | 2 | 50% | 345 |
| intraweek | 212,214 | +6.11% | 35 | 54% | 3,851 |
| intramonth | 212,076 | +6.04% | 0 | - | 235 |
| oracle | 211,680 | +5.84% | 0 | - | 233 |
| snake_abs | 209,722 | +4.86% | 1 | 100% | 255 |
| snake_abs_conv | 209,616 | +4.81% | 1 | 100% | 255 |
| random_hold | 207,090 | +3.54% | 10 | 70% | 733 |
| snake_viper_wild | 206,934 | +3.47% | 16 | 50% | 2,827 |
| snake_anaconda | 204,545 | +2.27% | 3 | 33% | 374 |
| snake_viper_tick | 203,400 | +1.70% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,674 | -0.16% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,239 | -11.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,894 (-4.55%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +1,307 | +0.61% |
| snake_abs_conv | +1,196 | +0.57% |
| snake_abs | +1,163 | +0.56% |
| snake_abs_exit_conv | +1,083 | +0.51% |
| unified | +955 | +0.43% |
| intramonth | +534 | +0.25% |
| snake_anaconda | +490 | +0.24% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -806 | -0.38% |
| benchmark_smallcap | -897 | -0.45% |
| intraweek | -1,109 | -0.52% |
| benchmark | -1,125 | -0.51% |
| random_hold | -1,342 | -0.64% |
| snake_viper_tick | -2,437 | -1.18% |
| snake_viper_wild | -2,481 | -1.19% |
| gold | -3,485 | -1.93% |

Average per day so far: unified Rs +622, benchmark Rs +569, snake_abs_exit Rs +438, snake_abs_exit_conv Rs +384, intraweek Rs +339, intramonth Rs +335, oracle Rs +324, snake_abs_conv Rs +291, snake_abs Rs +286, snake_viper_wild Rs +248, random_hold Rs +197, snake_anaconda Rs +147, snake_viper_tick Rs +136, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -10, snake_nonews Rs -326, snake Rs -347, gold Rs -632

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.