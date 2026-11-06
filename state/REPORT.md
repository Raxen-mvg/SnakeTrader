# Paper trading report

Updated 2026-11-06 10:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,786 | +7.39% | 0 | - | 236 |
| benchmark | 214,779 | +7.39% | 0 | - | 237 |
| intraweek | 211,444 | +5.72% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,709 | +4.86% | 1 | 100% | 255 |
| snake_abs_exit | 209,494 | +4.75% | 1 | 100% | 260 |
| intramonth | 206,830 | +3.42% | 0 | - | 235 |
| snake_abs | 206,660 | +3.33% | 1 | 100% | 255 |
| snake_abs_conv | 206,489 | +3.24% | 1 | 100% | 255 |
| oracle | 204,371 | +2.19% | 0 | - | 233 |
| random_hold | 203,734 | +1.87% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,559 | -1.22% | 3 | 33% | 702 |
| snake_anaconda | 196,630 | -1.69% | 3 | 33% | 374 |
| benchmark_smallcap | 194,865 | -2.57% | 0 | - | 237 |
| snake_viper_tick | 194,202 | -2.90% | 2 | 0% | 532 |
| gold | 190,407 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,533 (-6.23%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,025 | +0.97% |
| benchmark | +1,010 | +0.47% |
| oracle | +299 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -590 | -0.29% |
| intramonth | -1,119 | -0.54% |
| unified | -1,197 | -0.55% |
| gold | -3,814 | -1.96% |
| benchmark_smallcap | -3,823 | -1.92% |
| snake_abs | -5,028 | -2.38% |
| snake_abs_conv | -5,056 | -2.39% |
| snake_abs_exit_conv | -5,094 | -2.37% |
| snake_abs_exit | -5,165 | -2.41% |
| snake_anaconda | -5,850 | -2.89% |
| snake_viper_tick | -6,936 | -3.45% |
| snake_viper_wild | -7,097 | -3.47% |

Average per day so far: unified Rs +510, benchmark Rs +510, intraweek Rs +395, snake_abs_exit_conv Rs +373, snake_abs_exit Rs +365, snake_abs_conv Rs +250, snake_abs Rs +247, intramonth Rs +236, oracle Rs +151, random_hold Rs +129, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -116, snake_anaconda Rs -140, benchmark_smallcap Rs -205, snake_viper_tick Rs -322, gold Rs -331, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.