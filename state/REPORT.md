# Paper trading report

Updated 2026-11-06 12:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,269 | +7.63% | 0 | - | 237 |
| unified | 214,592 | +7.30% | 0 | - | 236 |
| intraweek | 209,454 | +4.73% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,865 | +4.43% | 1 | 100% | 255 |
| snake_abs_exit | 208,688 | +4.34% | 1 | 100% | 260 |
| intramonth | 206,811 | +3.41% | 0 | - | 235 |
| snake_abs | 205,831 | +2.92% | 1 | 100% | 255 |
| snake_abs_conv | 205,657 | +2.83% | 1 | 100% | 255 |
| oracle | 205,003 | +2.50% | 0 | - | 233 |
| random_hold | 203,271 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,137 | -1.93% | 3 | 33% | 374 |
| snake_viper_wild | 195,414 | -2.29% | 3 | 33% | 702 |
| benchmark_smallcap | 194,731 | -2.63% | 0 | - | 237 |
| snake_viper_tick | 192,107 | -3.95% | 2 | 0% | 532 |
| gold | 189,848 | -5.08% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,984 (-6.51%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,499 | +0.70% |
| oracle | +931 | +0.46% |
| intraweek | +35 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,052 | -0.52% |
| intramonth | -1,137 | -0.55% |
| unified | -1,392 | -0.64% |
| benchmark_smallcap | -3,957 | -1.99% |
| gold | -4,373 | -2.25% |
| snake_abs | -5,858 | -2.77% |
| snake_abs_conv | -5,888 | -2.78% |
| snake_abs_exit_conv | -5,938 | -2.77% |
| snake_abs_exit | -5,971 | -2.78% |
| snake_anaconda | -6,342 | -3.13% |
| snake_viper_tick | -9,031 | -4.49% |
| snake_viper_wild | -9,242 | -4.52% |

Average per day so far: benchmark Rs +527, unified Rs +503, snake_abs_exit_conv Rs +341, snake_abs_exit Rs +334, intraweek Rs +326, intramonth Rs +235, snake_abs_conv Rs +218, snake_abs Rs +216, oracle Rs +173, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -161, benchmark_smallcap Rs -211, snake_viper_wild Rs -218, gold Rs -350, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -438

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.