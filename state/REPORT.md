# Paper trading report

Updated 2026-11-06 15:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,013 | +8.51% | 0 | - | 237 |
| unified | 215,251 | +7.62% | 0 | - | 236 |
| intraweek | 209,442 | +4.72% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,755 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,636 | +4.32% | 1 | 100% | 260 |
| intramonth | 207,534 | +3.77% | 0 | - | 235 |
| oracle | 205,768 | +2.88% | 0 | - | 233 |
| snake_abs | 205,744 | +2.87% | 1 | 100% | 255 |
| snake_abs_conv | 205,556 | +2.78% | 1 | 100% | 255 |
| random_hold | 203,570 | +1.78% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,726 | -1.64% | 0 | - | 237 |
| snake_anaconda | 196,115 | -1.94% | 3 | 33% | 374 |
| snake_viper_wild | 196,045 | -1.98% | 4 | 25% | 842 |
| snake_viper_tick | 192,718 | -3.64% | 3 | 0% | 672 |
| gold | 191,229 | -4.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,275 (-6.36%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,244 | +1.52% |
| oracle | +1,696 | +0.83% |
| intraweek | +23 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -414 | -0.20% |
| unified | -732 | -0.34% |
| random_hold | -753 | -0.37% |
| benchmark_smallcap | -1,962 | -0.99% |
| gold | -2,992 | -1.54% |
| snake_abs | -5,944 | -2.81% |
| snake_abs_conv | -5,989 | -2.83% |
| snake_abs_exit | -6,023 | -2.81% |
| snake_abs_exit_conv | -6,048 | -2.82% |
| snake_anaconda | -6,364 | -3.14% |
| snake_viper_tick | -8,420 | -4.19% |
| snake_viper_wild | -8,610 | -4.21% |

Average per day so far: benchmark Rs +587, unified Rs +526, snake_abs_exit_conv Rs +337, snake_abs_exit Rs +332, intraweek Rs +326, intramonth Rs +260, snake_abs_conv Rs +214, snake_abs Rs +213, oracle Rs +199, random_hold Rs +123, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -131, snake_anaconda Rs -162, snake_viper_wild Rs -188, gold Rs -302, snake_viper_tick Rs -405, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.