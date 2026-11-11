# Paper trading report

Updated 2026-11-11 09:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,731 | +10.37% | 0 | - | 237 |
| unified | 220,295 | +10.15% | 0 | - | 236 |
| intraweek | 215,013 | +7.51% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 214,556 | +7.28% | 2 | 50% | 330 |
| snake_abs_exit | 214,160 | +7.08% | 2 | 50% | 308 |
| snake_abs | 211,542 | +5.77% | 1 | 100% | 255 |
| snake_abs_conv | 211,396 | +5.70% | 1 | 100% | 255 |
| oracle | 210,966 | +5.48% | 0 | - | 233 |
| intramonth | 210,861 | +5.43% | 0 | - | 235 |
| random_hold | 205,907 | +2.95% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,164 | +0.58% | 3 | 33% | 374 |
| snake_viper_wild | 200,990 | +0.49% | 7 | 57% | 1,332 |
| benchmark_smallcap | 200,033 | +0.02% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,580 | -1.21% | 6 | 50% | 1,154 |
| gold | 189,289 | -5.36% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,004 (-4.50%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,560 | +1.80% |
| snake_viper_tick | +3,503 | +1.80% |
| snake_abs_exit_conv | +2,647 | +1.25% |
| benchmark | +2,639 | +1.21% |
| snake_abs_exit | +2,176 | +1.03% |
| snake_abs_conv | +1,918 | +0.92% |
| snake_abs | +1,896 | +0.90% |
| benchmark_smallcap | +1,861 | +0.94% |
| snake_anaconda | +1,697 | +0.85% |
| oracle | +1,047 | +0.50% |
| random_hold | +946 | +0.46% |
| unified | +549 | +0.25% |
| intraweek | +471 | +0.22% |
| intramonth | +252 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,844 | -1.48% |

Average per day so far: benchmark Rs +669, unified Rs +655, snake_abs_exit_conv Rs +520, snake_abs_exit Rs +506, intraweek Rs +484, snake_abs_conv Rs +407, snake_abs Rs +398, oracle Rs +354, intramonth Rs +350, random_hold Rs +191, nifty_calls Rs +59, snake_anaconda Rs +45, snake_viper_wild Rs +43, benchmark_smallcap Rs +1, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -121, gold Rs -346, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.