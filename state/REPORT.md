# Paper trading report

Updated 2026-11-06 11:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,801 | +7.40% | 0 | - | 236 |
| benchmark | 214,642 | +7.32% | 0 | - | 237 |
| intraweek | 211,481 | +5.74% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,300 | +4.65% | 1 | 100% | 255 |
| snake_abs_exit | 209,087 | +4.54% | 1 | 100% | 260 |
| intramonth | 206,840 | +3.42% | 0 | - | 235 |
| snake_abs | 206,255 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,088 | +3.04% | 1 | 100% | 255 |
| oracle | 204,760 | +2.38% | 0 | - | 233 |
| random_hold | 203,401 | +1.70% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,680 | -1.66% | 3 | 33% | 374 |
| snake_viper_wild | 195,323 | -2.34% | 3 | 33% | 702 |
| benchmark_smallcap | 194,888 | -2.56% | 0 | - | 237 |
| snake_viper_tick | 192,015 | -3.99% | 2 | 0% | 532 |
| gold | 190,194 | -4.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,363 (-6.32%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,062 | +0.98% |
| benchmark | +872 | +0.41% |
| oracle | +688 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -922 | -0.45% |
| intramonth | -1,108 | -0.53% |
| unified | -1,182 | -0.55% |
| benchmark_smallcap | -3,800 | -1.91% |
| gold | -4,028 | -2.07% |
| snake_abs | -5,433 | -2.57% |
| snake_abs_conv | -5,457 | -2.58% |
| snake_abs_exit_conv | -5,504 | -2.56% |
| snake_abs_exit | -5,572 | -2.60% |
| snake_anaconda | -5,800 | -2.86% |
| snake_viper_tick | -9,123 | -4.54% |
| snake_viper_wild | -9,333 | -4.56% |

Average per day so far: unified Rs +510, benchmark Rs +505, intraweek Rs +396, snake_abs_exit_conv Rs +358, snake_abs_exit Rs +349, intramonth Rs +236, snake_abs_conv Rs +234, snake_abs Rs +232, oracle Rs +164, random_hold Rs +117, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -138, benchmark_smallcap Rs -204, snake_viper_wild Rs -223, gold Rs -338, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -444

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.