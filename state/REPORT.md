# Paper trading report

Updated 2026-11-06 14:26 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,424 | +8.21% | 0 | - | 237 |
| unified | 215,158 | +7.58% | 0 | - | 236 |
| snake_abs_exit_conv | 209,053 | +4.53% | 1 | 100% | 255 |
| snake_abs_exit | 208,959 | +4.48% | 1 | 100% | 260 |
| intraweek | 208,212 | +4.11% | 25 | 48% | 2,757 |
| intramonth | 207,593 | +3.80% | 0 | - | 235 |
| snake_abs | 206,031 | +3.02% | 1 | 100% | 255 |
| snake_abs_conv | 205,846 | +2.92% | 1 | 100% | 255 |
| oracle | 205,678 | +2.84% | 0 | - | 233 |
| random_hold | 203,559 | +1.78% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,174 | -1.91% | 3 | 33% | 374 |
| snake_viper_wild | 195,963 | -2.02% | 4 | 25% | 842 |
| benchmark_smallcap | 195,426 | -2.29% | 0 | - | 237 |
| snake_viper_tick | 192,635 | -3.68% | 3 | 0% | 672 |
| gold | 191,213 | -4.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,171 (-6.41%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,655 | +1.24% |
| oracle | +1,606 | +0.79% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -356 | -0.17% |
| random_hold | -764 | -0.37% |
| unified | -825 | -0.38% |
| intraweek | -1,206 | -0.58% |
| gold | -3,009 | -1.55% |
| benchmark_smallcap | -3,262 | -1.64% |
| snake_abs | -5,657 | -2.67% |
| snake_abs_conv | -5,699 | -2.69% |
| snake_abs_exit | -5,700 | -2.65% |
| snake_abs_exit_conv | -5,751 | -2.68% |
| snake_anaconda | -6,305 | -3.11% |
| snake_viper_tick | -8,503 | -4.23% |
| snake_viper_wild | -8,693 | -4.25% |

Average per day so far: benchmark Rs +566, unified Rs +523, snake_abs_exit_conv Rs +348, snake_abs_exit Rs +345, intraweek Rs +283, intramonth Rs +262, snake_abs_conv Rs +225, snake_abs Rs +223, oracle Rs +196, random_hold Rs +123, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -159, benchmark_smallcap Rs -183, snake_viper_wild Rs -192, gold Rs -303, snake_viper_tick Rs -409, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.