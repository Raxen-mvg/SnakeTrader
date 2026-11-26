# Paper trading report

Updated 2026-11-26 12:28 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,262 | +13.13% | 0 | - | 237 |
| unified | 223,490 | +11.74% | 0 | - | 236 |
| oracle | 213,264 | +6.63% | 0 | - | 233 |
| intramonth | 210,679 | +5.34% | 0 | - | 235 |
| random_hold | 209,751 | +4.88% | 13 | 69% | 1,037 |
| intraweek | 208,370 | +4.18% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,627 | +0.31% | 0 | - | 237 |
| snake_abs_exit | 200,579 | +0.29% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,006 | +0.00% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,315 | -0.84% | 1 | 100% | 255 |
| snake_abs_conv | 198,119 | -0.94% | 1 | 100% | 255 |
| snake_anaconda | 192,179 | -3.91% | 3 | 33% | 374 |
| snake_viper_wild | 191,846 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,589 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,158 | -16.92% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,854 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,816 | +0.91% |
| intraweek | +1,627 | +0.79% |
| gold | +1,562 | +0.95% |
| benchmark | +1,239 | +0.55% |
| random_hold | +258 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -532 | -0.25% |
| unified | -610 | -0.27% |
| intramonth | -1,014 | -0.48% |
| snake_abs_exit | -1,677 | -0.83% |
| snake_abs | -1,835 | -0.92% |
| snake_abs_conv | -1,854 | -0.93% |
| snake_abs_exit_conv | -1,969 | -0.97% |
| snake_anaconda | -2,374 | -1.22% |
| snake_viper_tick | -5,588 | -2.88% |
| snake_viper_wild | -5,698 | -2.88% |

Average per day so far: benchmark Rs +641, unified Rs +573, oracle Rs +324, intramonth Rs +260, random_hold Rs +238, intraweek Rs +204, nifty_calls Rs +45, benchmark_smallcap Rs +17, snake_abs_exit Rs +15, snake_abs_exit_conv Rs +0, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -43, snake_abs_conv Rs -50, snake_anaconda Rs -217, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -380, gold Rs -825

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.