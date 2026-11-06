# Paper trading report

Updated 2026-11-06 14:46 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,700 | +8.35% | 0 | - | 237 |
| unified | 215,043 | +7.52% | 0 | - | 236 |
| intraweek | 209,152 | +4.58% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,720 | +4.36% | 1 | 100% | 255 |
| snake_abs_exit | 208,639 | +4.32% | 1 | 100% | 260 |
| intramonth | 207,288 | +3.64% | 0 | - | 235 |
| snake_abs | 205,704 | +2.85% | 1 | 100% | 255 |
| snake_abs_conv | 205,519 | +2.76% | 1 | 100% | 255 |
| oracle | 205,364 | +2.68% | 0 | - | 233 |
| random_hold | 203,402 | +1.70% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,108 | -1.95% | 4 | 25% | 842 |
| snake_anaconda | 196,078 | -1.96% | 3 | 33% | 374 |
| benchmark_smallcap | 195,785 | -2.11% | 0 | - | 237 |
| snake_viper_tick | 192,781 | -3.61% | 3 | 0% | 672 |
| gold | 191,640 | -4.18% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,118 (-6.44%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,930 | +1.37% |
| oracle | +1,292 | +0.63% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -267 | -0.13% |
| intramonth | -661 | -0.32% |
| random_hold | -921 | -0.45% |
| unified | -940 | -0.43% |
| gold | -2,581 | -1.33% |
| benchmark_smallcap | -2,903 | -1.46% |
| snake_abs | -5,984 | -2.83% |
| snake_abs_exit | -6,020 | -2.80% |
| snake_abs_conv | -6,025 | -2.85% |
| snake_abs_exit_conv | -6,084 | -2.83% |
| snake_anaconda | -6,402 | -3.16% |
| snake_viper_tick | -8,357 | -4.16% |
| snake_viper_wild | -8,547 | -4.18% |

Average per day so far: benchmark Rs +576, unified Rs +519, snake_abs_exit_conv Rs +335, snake_abs_exit Rs +332, intraweek Rs +316, intramonth Rs +251, snake_abs_conv Rs +212, snake_abs Rs +211, oracle Rs +185, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -163, benchmark_smallcap Rs -169, snake_viper_wild Rs -185, gold Rs -288, snake_viper_tick Rs -401, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.