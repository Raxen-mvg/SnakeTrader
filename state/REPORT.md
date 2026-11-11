# Paper trading report

Updated 2026-11-11 10:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,991 | +10.50% | 0 | - | 237 |
| unified | 219,981 | +9.99% | 0 | - | 236 |
| snake_abs_exit_conv | 216,591 | +8.30% | 2 | 50% | 345 |
| intraweek | 215,140 | +7.57% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,973 | +7.49% | 2 | 50% | 345 |
| snake_abs | 213,192 | +6.60% | 1 | 100% | 255 |
| snake_abs_conv | 213,038 | +6.52% | 1 | 100% | 255 |
| oracle | 211,075 | +5.54% | 0 | - | 233 |
| intramonth | 210,630 | +5.32% | 0 | - | 235 |
| random_hold | 206,187 | +3.09% | 9 | 67% | 709 |
| snake_anaconda | 202,993 | +1.50% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,434 | +0.72% | 0 | - | 237 |
| snake_viper_wild | 200,420 | +0.21% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,018 | -1.49% | 9 | 44% | 1,639 |
| gold | 189,191 | -5.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,134 (-4.43%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,683 | +2.21% |
| snake_abs_conv | +3,560 | +1.70% |
| snake_abs | +3,545 | +1.69% |
| snake_anaconda | +3,526 | +1.77% |
| benchmark_smallcap | +3,262 | +1.65% |
| snake_viper_wild | +2,990 | +1.51% |
| snake_abs_exit | +2,989 | +1.41% |
| snake_viper_tick | +2,941 | +1.52% |
| benchmark | +2,899 | +1.33% |
| random_hold | +1,226 | +0.60% |
| oracle | +1,156 | +0.55% |
| intraweek | +598 | +0.28% |
| unified | +234 | +0.11% |
| intramonth | +20 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,943 | -1.53% |

Average per day so far: benchmark Rs +677, unified Rs +645, snake_abs_exit_conv Rs +593, snake_abs_exit Rs +535, intraweek Rs +488, snake_abs_conv Rs +466, snake_abs Rs +455, oracle Rs +357, intramonth Rs +343, random_hold Rs +200, snake_anaconda Rs +115, nifty_calls Rs +59, benchmark_smallcap Rs +53, snake_viper_wild Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -149, gold Rs -349, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.