# Paper trading report

Updated 2026-11-06 15:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,327 | +8.66% | 0 | - | 237 |
| unified | 215,917 | +7.96% | 0 | - | 236 |
| intraweek | 209,584 | +4.79% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,210 | +4.11% | 1 | 100% | 255 |
| snake_abs_exit | 208,083 | +4.04% | 1 | 100% | 260 |
| intramonth | 207,777 | +3.89% | 0 | - | 235 |
| oracle | 205,877 | +2.94% | 0 | - | 233 |
| snake_abs | 205,206 | +2.60% | 1 | 100% | 255 |
| snake_abs_conv | 205,019 | +2.51% | 1 | 100% | 255 |
| random_hold | 203,597 | +1.80% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,838 | -1.58% | 0 | - | 237 |
| snake_viper_wild | 195,869 | -2.06% | 4 | 25% | 842 |
| snake_anaconda | 195,868 | -2.07% | 3 | 33% | 374 |
| snake_viper_tick | 192,545 | -3.73% | 3 | 0% | 672 |
| gold | 190,999 | -4.50% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,278 (-6.36%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,557 | +1.66% |
| oracle | +1,805 | +0.89% |
| intraweek | +165 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -67 | -0.03% |
| intramonth | -172 | -0.08% |
| random_hold | -726 | -0.35% |
| benchmark_smallcap | -1,850 | -0.93% |
| gold | -3,222 | -1.66% |
| snake_abs | -6,482 | -3.06% |
| snake_abs_conv | -6,526 | -3.08% |
| snake_abs_exit | -6,576 | -3.06% |
| snake_abs_exit_conv | -6,593 | -3.07% |
| snake_anaconda | -6,612 | -3.27% |
| snake_viper_tick | -8,593 | -4.27% |
| snake_viper_wild | -8,786 | -4.29% |

Average per day so far: benchmark Rs +597, unified Rs +549, intraweek Rs +330, snake_abs_exit_conv Rs +316, snake_abs_exit Rs +311, intramonth Rs +268, oracle Rs +203, snake_abs_conv Rs +193, snake_abs Rs +193, random_hold Rs +124, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -126, snake_anaconda Rs -172, snake_viper_wild Rs -197, gold Rs -310, snake_nonews Rs -411, snake_viper_tick Rs -414, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.