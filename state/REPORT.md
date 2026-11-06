# Paper trading report

Updated 2026-11-06 09:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,126 | +7.06% | 0 | - | 236 |
| benchmark | 213,800 | +6.90% | 0 | - | 237 |
| snake_abs_exit_conv | 210,115 | +5.06% | 1 | 100% | 255 |
| snake_abs_exit | 209,876 | +4.94% | 1 | 100% | 260 |
| intraweek | 209,536 | +4.77% | 25 | 48% | 2,757 |
| snake_abs | 207,048 | +3.52% | 1 | 100% | 255 |
| snake_abs_conv | 206,890 | +3.44% | 1 | 100% | 255 |
| intramonth | 206,296 | +3.15% | 0 | - | 235 |
| oracle | 203,830 | +1.92% | 0 | - | 233 |
| random_hold | 203,230 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,411 | -1.29% | 3 | 33% | 374 |
| snake_viper_wild | 197,074 | -1.46% | 3 | 33% | 702 |
| benchmark_smallcap | 194,787 | -2.61% | 0 | - | 237 |
| snake_viper_tick | 193,735 | -3.13% | 2 | 0% | 532 |
| gold | 190,407 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,153 (-6.42%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +118 | +0.06% |
| benchmark | +31 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -242 | -0.12% |
| random_hold | -1,093 | -0.54% |
| intramonth | -1,653 | -0.80% |
| unified | -1,857 | -0.86% |
| gold | -3,814 | -1.96% |
| benchmark_smallcap | -3,901 | -1.96% |
| snake_abs | -4,640 | -2.19% |
| snake_abs_conv | -4,655 | -2.20% |
| snake_abs_exit_conv | -4,688 | -2.18% |
| snake_abs_exit | -4,783 | -2.23% |
| snake_anaconda | -5,068 | -2.50% |
| snake_viper_tick | -7,403 | -3.68% |
| snake_viper_wild | -7,582 | -3.71% |

Average per day so far: unified Rs +487, benchmark Rs +476, snake_abs_exit_conv Rs +389, snake_abs_exit Rs +380, intraweek Rs +329, snake_abs_conv Rs +265, snake_abs Rs +261, intramonth Rs +217, oracle Rs +132, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -108, snake_viper_wild Rs -139, benchmark_smallcap Rs -209, gold Rs -331, snake_viper_tick Rs -348, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.