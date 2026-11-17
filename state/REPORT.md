# Paper trading report

Updated 2026-11-17 12:59 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,009 | +11.00% | 0 | - | 237 |
| unified | 221,705 | +10.85% | 0 | - | 236 |
| snake_abs_exit | 214,308 | +7.15% | 2 | 50% | 345 |
| intraweek | 214,181 | +7.09% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,616 | +6.31% | 2 | 50% | 345 |
| oracle | 212,184 | +6.09% | 0 | - | 233 |
| intramonth | 211,584 | +5.79% | 0 | - | 235 |
| snake_abs | 209,434 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,286 | +4.64% | 1 | 100% | 255 |
| random_hold | 207,593 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 207,482 | +3.74% | 14 | 50% | 2,496 |
| snake_anaconda | 204,887 | +2.44% | 3 | 33% | 374 |
| snake_viper_tick | 203,935 | +1.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,345 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,349 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,247 (-4.38%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,915 | +1.38% |
| benchmark | +1,928 | +0.88% |
| snake_viper_wild | +1,337 | +0.65% |
| snake_viper_tick | +1,315 | +0.65% |
| benchmark_smallcap | +516 | +0.26% |
| gold | +395 | +0.22% |
| unified | +267 | +0.12% |
| oracle | +161 | +0.08% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -35 | -0.02% |
| snake_abs_exit | -102 | -0.05% |
| random_hold | -200 | -0.10% |
| snake_anaconda | -216 | -0.10% |
| snake_abs_exit_conv | -601 | -0.28% |
| snake_abs | -700 | -0.33% |
| snake_abs_conv | -704 | -0.34% |

Average per day so far: benchmark Rs +629, unified Rs +620, snake_abs_exit Rs +447, intraweek Rs +405, snake_abs_exit_conv Rs +394, oracle Rs +348, intramonth Rs +331, snake_abs_conv Rs +290, snake_abs Rs +286, snake_viper_wild Rs +277, random_hold Rs +217, snake_viper_tick Rs +164, snake_anaconda Rs +163, nifty_calls Rs +52, benchmark_smallcap Rs +43, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.