# Paper trading report

Updated 2026-11-06 09:42 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,362 | +7.18% | 0 | - | 236 |
| benchmark | 214,060 | +7.03% | 0 | - | 237 |
| intraweek | 210,063 | +5.03% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,233 | +4.62% | 1 | 100% | 255 |
| snake_abs_exit | 208,974 | +4.49% | 1 | 100% | 260 |
| snake_abs | 206,199 | +3.10% | 1 | 100% | 255 |
| intramonth | 206,160 | +3.08% | 0 | - | 235 |
| snake_abs_conv | 206,020 | +3.01% | 1 | 100% | 255 |
| oracle | 204,004 | +2.00% | 0 | - | 233 |
| random_hold | 203,662 | +1.83% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,610 | -0.69% | 3 | 33% | 702 |
| snake_anaconda | 196,191 | -1.90% | 3 | 33% | 374 |
| snake_viper_tick | 195,244 | -2.38% | 2 | 0% | 532 |
| benchmark_smallcap | 195,011 | -2.49% | 0 | - | 237 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,102 (-6.45%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +644 | +0.31% |
| benchmark | +291 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -68 | -0.03% |
| random_hold | -661 | -0.32% |
| unified | -1,621 | -0.75% |
| intramonth | -1,788 | -0.86% |
| benchmark_smallcap | -3,677 | -1.85% |
| gold | -4,011 | -2.06% |
| snake_abs | -5,490 | -2.59% |
| snake_abs_conv | -5,525 | -2.61% |
| snake_abs_exit_conv | -5,570 | -2.59% |
| snake_abs_exit | -5,685 | -2.65% |
| snake_viper_tick | -5,894 | -2.93% |
| snake_viper_wild | -6,046 | -2.95% |
| snake_anaconda | -6,288 | -3.11% |

Average per day so far: unified Rs +495, benchmark Rs +485, snake_abs_exit_conv Rs +355, intraweek Rs +347, snake_abs_exit Rs +345, snake_abs_conv Rs +232, snake_abs Rs +230, intramonth Rs +212, oracle Rs +138, random_hold Rs +126, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -66, snake_anaconda Rs -159, benchmark_smallcap Rs -200, snake_viper_tick Rs -264, gold Rs -338, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.