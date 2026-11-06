# Paper trading report

Updated 2026-11-06 12:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,844 | +7.42% | 0 | - | 236 |
| benchmark | 214,741 | +7.37% | 0 | - | 237 |
| intraweek | 209,125 | +4.56% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,745 | +4.37% | 1 | 100% | 255 |
| snake_abs_exit | 208,568 | +4.28% | 1 | 100% | 260 |
| intramonth | 207,150 | +3.58% | 0 | - | 235 |
| snake_abs | 205,712 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,538 | +2.77% | 1 | 100% | 255 |
| oracle | 204,877 | +2.44% | 0 | - | 233 |
| random_hold | 203,281 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,987 | -2.01% | 3 | 33% | 374 |
| snake_viper_wild | 195,600 | -2.20% | 3 | 33% | 702 |
| benchmark_smallcap | 194,563 | -2.72% | 0 | - | 237 |
| snake_viper_tick | 192,287 | -3.86% | 2 | 0% | 532 |
| gold | 190,358 | -4.82% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,982 (-6.51%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +972 | +0.45% |
| oracle | +805 | +0.40% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -293 | -0.14% |
| intramonth | -799 | -0.38% |
| random_hold | -1,042 | -0.51% |
| unified | -1,139 | -0.53% |
| gold | -3,863 | -1.99% |
| benchmark_smallcap | -4,125 | -2.08% |
| snake_abs | -5,976 | -2.82% |
| snake_abs_conv | -6,006 | -2.84% |
| snake_abs_exit_conv | -6,058 | -2.82% |
| snake_abs_exit | -6,090 | -2.84% |
| snake_anaconda | -6,492 | -3.21% |
| snake_viper_tick | -8,851 | -4.40% |
| snake_viper_wild | -9,056 | -4.42% |

Average per day so far: unified Rs +512, benchmark Rs +508, snake_abs_exit_conv Rs +336, snake_abs_exit Rs +330, intraweek Rs +315, intramonth Rs +247, snake_abs_conv Rs +213, snake_abs Rs +212, oracle Rs +168, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -167, snake_viper_wild Rs -210, benchmark_smallcap Rs -217, gold Rs -332, snake_nonews Rs -411, snake_viper_tick Rs -429, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.