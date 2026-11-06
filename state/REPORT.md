# Paper trading report

Updated 2026-11-06 15:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,937 | +8.47% | 0 | - | 237 |
| unified | 215,267 | +7.63% | 0 | - | 236 |
| intraweek | 209,558 | +4.78% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,888 | +4.44% | 1 | 100% | 255 |
| snake_abs_exit | 208,768 | +4.38% | 1 | 100% | 260 |
| intramonth | 207,523 | +3.76% | 0 | - | 235 |
| snake_abs | 205,874 | +2.94% | 1 | 100% | 255 |
| oracle | 205,696 | +2.85% | 0 | - | 233 |
| snake_abs_conv | 205,687 | +2.84% | 1 | 100% | 255 |
| random_hold | 203,548 | +1.77% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,636 | -1.68% | 0 | - | 237 |
| snake_anaconda | 196,228 | -1.89% | 3 | 33% | 374 |
| snake_viper_wild | 195,889 | -2.06% | 4 | 25% | 842 |
| snake_viper_tick | 192,565 | -3.72% | 3 | 0% | 672 |
| gold | 191,427 | -4.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,310 (-6.35%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,167 | +1.48% |
| oracle | +1,624 | +0.80% |
| intraweek | +140 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -425 | -0.20% |
| unified | -717 | -0.33% |
| random_hold | -775 | -0.38% |
| benchmark_smallcap | -2,051 | -1.03% |
| gold | -2,795 | -1.44% |
| snake_abs | -5,815 | -2.75% |
| snake_abs_conv | -5,858 | -2.77% |
| snake_abs_exit | -5,891 | -2.74% |
| snake_abs_exit_conv | -5,915 | -2.75% |
| snake_anaconda | -6,251 | -3.09% |
| snake_viper_tick | -8,573 | -4.26% |
| snake_viper_wild | -8,766 | -4.28% |

Average per day so far: benchmark Rs +584, unified Rs +526, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +337, intraweek Rs +330, intramonth Rs +259, snake_abs_conv Rs +219, snake_abs Rs +218, oracle Rs +196, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -135, snake_anaconda Rs -157, snake_viper_wild Rs -196, gold Rs -296, snake_nonews Rs -411, snake_viper_tick Rs -413, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.