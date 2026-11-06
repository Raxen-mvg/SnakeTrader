# Paper trading report

Updated 2026-11-06 14:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,684 | +8.34% | 0 | - | 237 |
| unified | 215,231 | +7.62% | 0 | - | 236 |
| intraweek | 209,226 | +4.61% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,100 | +4.55% | 1 | 100% | 255 |
| snake_abs_exit | 209,001 | +4.50% | 1 | 100% | 260 |
| intramonth | 207,519 | +3.76% | 0 | - | 235 |
| snake_abs | 206,082 | +3.04% | 1 | 100% | 255 |
| snake_abs_conv | 205,897 | +2.95% | 1 | 100% | 255 |
| oracle | 205,419 | +2.71% | 0 | - | 233 |
| random_hold | 203,528 | +1.76% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,449 | -1.77% | 3 | 33% | 374 |
| snake_viper_wild | 196,338 | -1.83% | 4 | 25% | 842 |
| benchmark_smallcap | 195,908 | -2.05% | 0 | - | 237 |
| snake_viper_tick | 193,009 | -3.50% | 3 | 0% | 672 |
| gold | 191,558 | -4.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,305 (-6.35%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,915 | +1.36% |
| oracle | +1,347 | +0.66% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -192 | -0.09% |
| intramonth | -430 | -0.21% |
| unified | -752 | -0.35% |
| random_hold | -795 | -0.39% |
| gold | -2,663 | -1.37% |
| benchmark_smallcap | -2,780 | -1.40% |
| snake_abs | -5,606 | -2.65% |
| snake_abs_conv | -5,648 | -2.67% |
| snake_abs_exit | -5,658 | -2.64% |
| snake_abs_exit_conv | -5,704 | -2.65% |
| snake_anaconda | -6,030 | -2.98% |
| snake_viper_tick | -8,129 | -4.04% |
| snake_viper_wild | -8,318 | -4.06% |

Average per day so far: benchmark Rs +575, unified Rs +525, snake_abs_exit_conv Rs +350, snake_abs_exit Rs +346, intraweek Rs +318, intramonth Rs +259, snake_abs_conv Rs +227, snake_abs Rs +225, oracle Rs +187, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -148, benchmark_smallcap Rs -164, snake_viper_wild Rs -174, gold Rs -291, snake_viper_tick Rs -388, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.