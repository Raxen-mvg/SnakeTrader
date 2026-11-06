# Paper trading report

Updated 2026-11-06 11:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,616 | +7.31% | 0 | - | 236 |
| benchmark | 214,489 | +7.24% | 0 | - | 237 |
| intraweek | 210,718 | +5.36% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,932 | +4.47% | 1 | 100% | 255 |
| snake_abs_exit | 208,726 | +4.36% | 1 | 100% | 260 |
| intramonth | 206,719 | +3.36% | 0 | - | 235 |
| snake_abs | 205,891 | +2.95% | 1 | 100% | 255 |
| snake_abs_conv | 205,724 | +2.86% | 1 | 100% | 255 |
| oracle | 204,541 | +2.27% | 0 | - | 233 |
| random_hold | 203,265 | +1.63% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,325 | -1.84% | 3 | 33% | 374 |
| snake_viper_wild | 195,461 | -2.27% | 3 | 33% | 702 |
| benchmark_smallcap | 194,540 | -2.73% | 0 | - | 237 |
| snake_viper_tick | 192,151 | -3.92% | 2 | 0% | 532 |
| gold | 190,391 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,104 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,300 | +0.62% |
| benchmark | +719 | +0.34% |
| oracle | +469 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,058 | -0.52% |
| intramonth | -1,229 | -0.59% |
| unified | -1,368 | -0.63% |
| gold | -3,831 | -1.97% |
| benchmark_smallcap | -4,148 | -2.09% |
| snake_abs | -5,797 | -2.74% |
| snake_abs_conv | -5,821 | -2.75% |
| snake_abs_exit_conv | -5,872 | -2.73% |
| snake_abs_exit | -5,933 | -2.76% |
| snake_anaconda | -6,155 | -3.04% |
| snake_viper_tick | -8,987 | -4.47% |
| snake_viper_wild | -9,195 | -4.49% |

Average per day so far: unified Rs +504, benchmark Rs +500, intraweek Rs +370, snake_abs_exit_conv Rs +344, snake_abs_exit Rs +336, intramonth Rs +232, snake_abs_conv Rs +220, snake_abs Rs +218, oracle Rs +157, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -153, snake_viper_wild Rs -216, benchmark_smallcap Rs -218, gold Rs -331, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -436

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.