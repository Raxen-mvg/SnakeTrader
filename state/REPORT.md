# Paper trading report

Updated 2026-11-06 15:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,411 | +8.71% | 0 | - | 237 |
| unified | 215,962 | +7.98% | 0 | - | 236 |
| intraweek | 209,380 | +4.69% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,292 | +4.15% | 1 | 100% | 255 |
| snake_abs_exit | 208,164 | +4.08% | 1 | 100% | 260 |
| intramonth | 207,885 | +3.94% | 0 | - | 235 |
| oracle | 205,979 | +2.99% | 0 | - | 233 |
| snake_abs | 205,284 | +2.64% | 1 | 100% | 255 |
| snake_abs_conv | 205,099 | +2.55% | 1 | 100% | 255 |
| random_hold | 203,536 | +1.77% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,704 | -1.65% | 0 | - | 237 |
| snake_anaconda | 195,943 | -2.03% | 3 | 33% | 374 |
| snake_viper_wild | 195,869 | -2.06% | 4 | 25% | 842 |
| snake_viper_tick | 192,545 | -3.73% | 3 | 0% | 672 |
| gold | 190,785 | -4.61% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,298 (-6.35%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,641 | +1.70% |
| oracle | +1,907 | +0.94% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -21 | -0.01% |
| intraweek | -39 | -0.02% |
| intramonth | -63 | -0.03% |
| random_hold | -787 | -0.39% |
| benchmark_smallcap | -1,984 | -1.00% |
| gold | -3,436 | -1.77% |
| snake_abs | -6,405 | -3.02% |
| snake_abs_conv | -6,446 | -3.05% |
| snake_abs_exit | -6,495 | -3.03% |
| snake_abs_exit_conv | -6,511 | -3.03% |
| snake_anaconda | -6,536 | -3.23% |
| snake_viper_tick | -8,593 | -4.27% |
| snake_viper_wild | -8,786 | -4.29% |

Average per day so far: benchmark Rs +600, unified Rs +550, intraweek Rs +323, snake_abs_exit_conv Rs +319, snake_abs_exit Rs +314, intramonth Rs +272, oracle Rs +206, snake_abs_conv Rs +196, snake_abs Rs +196, random_hold Rs +122, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -132, snake_anaconda Rs -169, snake_viper_wild Rs -197, gold Rs -318, snake_nonews Rs -411, snake_viper_tick Rs -414, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.