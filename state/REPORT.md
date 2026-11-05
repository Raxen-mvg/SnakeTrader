# Paper trading report

Updated 2026-11-05 13:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,417 | +8.71% | 0 | - | 236 |
| snake_abs_exit_conv | 214,537 | +7.27% | 1 | 100% | 255 |
| snake_abs_exit | 214,230 | +7.12% | 1 | 100% | 260 |
| benchmark | 213,433 | +6.72% | 0 | - | 237 |
| snake_abs | 211,414 | +5.71% | 1 | 100% | 255 |
| intraweek | 211,287 | +5.64% | 25 | 48% | 2,757 |
| snake_abs_conv | 211,278 | +5.64% | 1 | 100% | 255 |
| intramonth | 209,385 | +4.69% | 0 | - | 235 |
| snake_viper_wild | 206,515 | +3.26% | 3 | 33% | 702 |
| random_hold | 206,026 | +3.01% | 8 | 62% | 649 |
| oracle | 203,930 | +1.97% | 0 | - | 233 |
| snake_viper_tick | 202,968 | +1.48% | 2 | 0% | 532 |
| snake_anaconda | 202,545 | +1.27% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,013 | -0.49% | 0 | - | 237 |
| gold | 194,106 | -2.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,197 (-4.90%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,674 | +2.24% |
| unified | +2,977 | +1.39% |
| random_hold | +2,717 | +1.34% |
| gold | +2,713 | +1.42% |
| intramonth | +2,369 | +1.14% |
| benchmark_smallcap | +2,343 | +1.19% |
| oracle | +2,137 | +1.06% |
| intraweek | +1,590 | +0.76% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -478 | -0.22% |
| snake_abs_conv | -480 | -0.23% |
| snake_abs | -489 | -0.23% |
| snake_abs_exit | -671 | -0.31% |
| snake_anaconda | -1,275 | -0.63% |
| snake_viper_tick | -2,433 | -1.18% |
| snake_viper_wild | -2,514 | -1.20% |

Average per day so far: unified Rs +622, snake_abs_exit_conv Rs +581, snake_abs_exit Rs +569, benchmark Rs +480, snake_abs_conv Rs +451, snake_abs Rs +439, intraweek Rs +403, intramonth Rs +335, snake_viper_wild Rs +326, random_hold Rs +215, snake_viper_tick Rs +175, oracle Rs +140, snake_anaconda Rs +111, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -41, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.