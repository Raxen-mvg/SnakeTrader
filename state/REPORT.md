# Paper trading report

Updated 2026-11-06 13:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 216,317 | +8.16% | 0 | - | 237 |
| unified | 214,783 | +7.39% | 0 | - | 236 |
| snake_abs_exit_conv | 208,485 | +4.24% | 1 | 100% | 255 |
| snake_abs_exit | 208,377 | +4.19% | 1 | 100% | 260 |
| intraweek | 208,317 | +4.16% | 25 | 48% | 2,757 |
| intramonth | 207,084 | +3.54% | 0 | - | 235 |
| snake_abs | 205,481 | +2.74% | 1 | 100% | 255 |
| oracle | 205,296 | +2.65% | 0 | - | 233 |
| snake_abs_conv | 205,288 | +2.64% | 1 | 100% | 255 |
| random_hold | 203,329 | +1.67% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,153 | -1.92% | 3 | 33% | 702 |
| snake_anaconda | 195,730 | -2.13% | 3 | 33% | 374 |
| benchmark_smallcap | 195,168 | -2.42% | 0 | - | 237 |
| snake_viper_tick | 192,826 | -3.59% | 2 | 0% | 532 |
| gold | 190,720 | -4.64% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,874 (-6.56%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,547 | +1.19% |
| oracle | +1,224 | +0.60% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -864 | -0.42% |
| random_hold | -994 | -0.49% |
| intraweek | -1,101 | -0.53% |
| unified | -1,200 | -0.56% |
| gold | -3,502 | -1.80% |
| benchmark_smallcap | -3,520 | -1.77% |
| snake_abs | -6,208 | -2.93% |
| snake_abs_conv | -6,256 | -2.96% |
| snake_abs_exit | -6,282 | -2.93% |
| snake_abs_exit_conv | -6,319 | -2.94% |
| snake_anaconda | -6,749 | -3.33% |
| snake_viper_tick | -8,312 | -4.13% |
| snake_viper_wild | -8,503 | -4.16% |

Average per day so far: benchmark Rs +563, unified Rs +510, snake_abs_exit_conv Rs +326, snake_abs_exit Rs +322, intraweek Rs +287, intramonth Rs +244, snake_abs_conv Rs +203, snake_abs Rs +203, oracle Rs +183, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -178, snake_viper_wild Rs -183, benchmark_smallcap Rs -193, gold Rs -320, snake_viper_tick Rs -399, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.