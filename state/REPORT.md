# Paper trading report

Updated 2026-11-06 14:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,172 | +8.09% | 0 | - | 237 |
| unified | 215,293 | +7.65% | 0 | - | 236 |
| snake_abs_exit_conv | 208,746 | +4.37% | 1 | 100% | 255 |
| snake_abs_exit | 208,658 | +4.33% | 1 | 100% | 260 |
| intraweek | 208,630 | +4.32% | 25 | 48% | 2,757 |
| intramonth | 207,556 | +3.78% | 0 | - | 235 |
| snake_abs | 205,726 | +2.86% | 1 | 100% | 255 |
| oracle | 205,577 | +2.79% | 0 | - | 233 |
| snake_abs_conv | 205,542 | +2.77% | 1 | 100% | 255 |
| random_hold | 203,519 | +1.76% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,193 | -1.90% | 3 | 33% | 702 |
| snake_anaconda | 195,972 | -2.01% | 3 | 33% | 374 |
| benchmark_smallcap | 195,370 | -2.31% | 0 | - | 237 |
| snake_viper_tick | 192,867 | -3.57% | 2 | 0% | 532 |
| gold | 191,048 | -4.48% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,152 (-6.42%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,402 | +1.12% |
| oracle | +1,506 | +0.74% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -393 | -0.19% |
| unified | -690 | -0.32% |
| intraweek | -789 | -0.38% |
| random_hold | -804 | -0.39% |
| gold | -3,173 | -1.63% |
| benchmark_smallcap | -3,318 | -1.67% |
| snake_abs | -5,962 | -2.82% |
| snake_abs_exit | -6,000 | -2.79% |
| snake_abs_conv | -6,003 | -2.84% |
| snake_abs_exit_conv | -6,057 | -2.82% |
| snake_anaconda | -6,507 | -3.21% |
| snake_viper_tick | -8,271 | -4.11% |
| snake_viper_wild | -8,463 | -4.13% |

Average per day so far: benchmark Rs +558, unified Rs +527, snake_abs_exit_conv Rs +336, snake_abs_exit Rs +333, intraweek Rs +298, intramonth Rs +261, snake_abs_conv Rs +213, snake_abs Rs +212, oracle Rs +192, random_hold Rs +121, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -168, snake_viper_wild Rs -181, benchmark_smallcap Rs -185, gold Rs -309, snake_viper_tick Rs -396, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.