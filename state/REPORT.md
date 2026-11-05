# Paper trading report

Updated 2026-11-05 14:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,131 | +8.07% | 0 | - | 236 |
| snake_abs_exit_conv | 214,533 | +7.27% | 1 | 100% | 255 |
| snake_abs_exit | 214,248 | +7.12% | 1 | 100% | 260 |
| benchmark | 213,999 | +7.00% | 0 | - | 237 |
| snake_abs | 211,422 | +5.71% | 1 | 100% | 255 |
| snake_abs_conv | 211,275 | +5.64% | 1 | 100% | 255 |
| intraweek | 209,865 | +4.93% | 25 | 48% | 2,757 |
| intramonth | 208,000 | +4.00% | 0 | - | 235 |
| snake_viper_wild | 205,362 | +2.68% | 3 | 33% | 702 |
| random_hold | 204,601 | +2.30% | 8 | 62% | 649 |
| oracle | 204,293 | +2.15% | 0 | - | 233 |
| snake_anaconda | 202,066 | +1.03% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,832 | +0.92% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,114 | -0.44% | 0 | - | 237 |
| gold | 194,238 | -2.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,526 (-5.24%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,240 | +2.51% |
| gold | +2,844 | +1.49% |
| oracle | +2,501 | +1.24% |
| benchmark_smallcap | +2,444 | +1.24% |
| unified | +1,692 | +0.79% |
| random_hold | +1,292 | +0.64% |
| intramonth | +984 | +0.48% |
| intraweek | +168 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -481 | -0.23% |
| snake_abs_exit_conv | -482 | -0.22% |
| snake_abs_conv | -483 | -0.23% |
| snake_abs_exit | -652 | -0.30% |
| snake_anaconda | -1,755 | -0.86% |
| snake_viper_tick | -3,568 | -1.74% |
| snake_viper_wild | -3,668 | -1.75% |

Average per day so far: snake_abs_exit_conv Rs +581, unified Rs +576, snake_abs_exit Rs +570, benchmark Rs +500, snake_abs_conv Rs +451, snake_abs Rs +439, intraweek Rs +352, intramonth Rs +286, snake_viper_wild Rs +268, random_hold Rs +164, oracle Rs +153, snake_viper_tick Rs +108, snake_anaconda Rs +90, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.