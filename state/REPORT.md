# Paper trading report

Updated 2026-11-06 11:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,779 | +7.39% | 0 | - | 236 |
| benchmark | 214,604 | +7.30% | 0 | - | 237 |
| intraweek | 211,299 | +5.65% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,547 | +4.77% | 1 | 100% | 255 |
| snake_abs_exit | 209,334 | +4.67% | 1 | 100% | 260 |
| intramonth | 206,869 | +3.44% | 0 | - | 235 |
| snake_abs | 206,503 | +3.25% | 1 | 100% | 255 |
| snake_abs_conv | 206,335 | +3.17% | 1 | 100% | 255 |
| oracle | 204,914 | +2.46% | 0 | - | 233 |
| random_hold | 203,324 | +1.66% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,892 | -1.55% | 3 | 33% | 374 |
| snake_viper_wild | 195,180 | -2.41% | 3 | 33% | 702 |
| benchmark_smallcap | 194,764 | -2.62% | 0 | - | 237 |
| snake_viper_tick | 191,877 | -4.06% | 2 | 0% | 532 |
| gold | 190,111 | -4.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,409 (-6.30%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,881 | +0.90% |
| oracle | +842 | +0.41% |
| benchmark | +834 | +0.39% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -999 | -0.49% |
| intramonth | -1,079 | -0.52% |
| unified | -1,204 | -0.56% |
| benchmark_smallcap | -3,924 | -1.98% |
| gold | -4,110 | -2.12% |
| snake_abs | -5,186 | -2.45% |
| snake_abs_conv | -5,210 | -2.46% |
| snake_abs_exit_conv | -5,256 | -2.45% |
| snake_abs_exit | -5,325 | -2.48% |
| snake_anaconda | -5,587 | -2.76% |
| snake_viper_tick | -9,261 | -4.60% |
| snake_viper_wild | -9,476 | -4.63% |

Average per day so far: unified Rs +510, benchmark Rs +504, intraweek Rs +390, snake_abs_exit_conv Rs +367, snake_abs_exit Rs +359, snake_abs_conv Rs +244, snake_abs Rs +241, intramonth Rs +237, oracle Rs +169, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -129, benchmark_smallcap Rs -209, snake_viper_wild Rs -230, gold Rs -341, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -451

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.