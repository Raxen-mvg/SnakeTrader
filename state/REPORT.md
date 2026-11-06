# Paper trading report

Updated 2026-11-06 13:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,667 | +7.83% | 0 | - | 237 |
| unified | 214,687 | +7.34% | 0 | - | 236 |
| intraweek | 209,093 | +4.55% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,721 | +4.36% | 1 | 100% | 255 |
| snake_abs_exit | 208,646 | +4.32% | 1 | 100% | 260 |
| intramonth | 207,007 | +3.50% | 0 | - | 235 |
| snake_abs | 205,703 | +2.85% | 1 | 100% | 255 |
| snake_abs_conv | 205,521 | +2.76% | 1 | 100% | 255 |
| oracle | 205,212 | +2.61% | 0 | - | 233 |
| random_hold | 203,342 | +1.67% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,852 | -1.57% | 3 | 33% | 702 |
| snake_anaconda | 196,152 | -1.92% | 3 | 33% | 374 |
| benchmark_smallcap | 194,955 | -2.52% | 0 | - | 237 |
| snake_viper_tick | 193,518 | -3.24% | 2 | 0% | 532 |
| gold | 190,095 | -4.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,031 (-6.48%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,897 | +0.89% |
| oracle | +1,140 | +0.56% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -326 | -0.16% |
| intramonth | -942 | -0.45% |
| random_hold | -981 | -0.48% |
| unified | -1,296 | -0.60% |
| benchmark_smallcap | -3,733 | -1.88% |
| gold | -4,126 | -2.12% |
| snake_abs | -5,986 | -2.83% |
| snake_abs_exit | -6,013 | -2.80% |
| snake_abs_conv | -6,024 | -2.85% |
| snake_abs_exit_conv | -6,083 | -2.83% |
| snake_anaconda | -6,327 | -3.12% |
| snake_viper_tick | -7,620 | -3.79% |
| snake_viper_wild | -7,804 | -3.81% |

Average per day so far: benchmark Rs +540, unified Rs +506, snake_abs_exit_conv Rs +335, snake_abs_exit Rs +333, intraweek Rs +314, intramonth Rs +242, snake_abs_conv Rs +212, snake_abs Rs +211, oracle Rs +180, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -150, snake_anaconda Rs -160, benchmark_smallcap Rs -202, gold Rs -342, snake_viper_tick Rs -360, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.