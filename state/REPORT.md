# Paper trading report

Updated 2026-11-17 14:27 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| unified | 221,631 | +10.81% | 0 | - | 236 |
| intraweek | 213,604 | +6.80% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,200 | +6.60% | 2 | 50% | 345 |
| oracle | 212,254 | +6.13% | 0 | - | 233 |
| snake_abs_exit_conv | 211,624 | +5.81% | 2 | 50% | 345 |
| intramonth | 211,570 | +5.79% | 0 | - | 235 |
| snake_viper_wild | 209,444 | +4.72% | 14 | 50% | 2,496 |
| snake_abs | 208,347 | +4.17% | 1 | 100% | 255 |
| snake_abs_conv | 208,208 | +4.10% | 1 | 100% | 255 |
| random_hold | 207,815 | +3.91% | 10 | 70% | 733 |
| snake_viper_tick | 205,865 | +2.93% | 13 | 46% | 2,299 |
| snake_anaconda | 203,749 | +1.87% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,255 | +0.63% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,905 | -9.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,162 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,300 | +1.60% |
| snake_viper_tick | +3,245 | +1.60% |
| intraweek | +2,338 | +1.11% |
| benchmark | +1,943 | +0.88% |
| benchmark_smallcap | +426 | +0.21% |
| oracle | +231 | +0.11% |
| unified | +193 | +0.09% |
| random_hold | +22 | +0.01% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -49 | -0.02% |
| gold | -49 | -0.03% |
| snake_abs_exit | -1,210 | -0.56% |
| snake_anaconda | -1,354 | -0.66% |
| snake_abs_exit_conv | -1,593 | -0.75% |
| snake_abs_conv | -1,781 | -0.85% |
| snake_abs | -1,786 | -0.85% |

Average per day so far: benchmark Rs +629, unified Rs +618, snake_abs_exit Rs +412, intraweek Rs +389, snake_abs_exit_conv Rs +363, oracle Rs +350, snake_viper_wild Rs +350, intramonth Rs +331, snake_abs_conv Rs +257, snake_abs Rs +253, snake_viper_tick Rs +244, random_hold Rs +223, snake_anaconda Rs +125, nifty_calls Rs +52, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.