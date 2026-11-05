# Paper trading report

Updated 2026-11-05 14:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,081 | +8.04% | 0 | - | 236 |
| snake_abs_exit_conv | 214,553 | +7.28% | 1 | 100% | 255 |
| snake_abs_exit | 214,301 | +7.15% | 1 | 100% | 260 |
| benchmark | 213,670 | +6.83% | 0 | - | 237 |
| snake_abs | 211,440 | +5.72% | 1 | 100% | 255 |
| snake_abs_conv | 211,300 | +5.65% | 1 | 100% | 255 |
| intraweek | 210,692 | +5.35% | 25 | 48% | 2,757 |
| intramonth | 207,639 | +3.82% | 0 | - | 235 |
| snake_viper_wild | 205,295 | +2.65% | 3 | 33% | 702 |
| random_hold | 204,938 | +2.47% | 8 | 62% | 649 |
| oracle | 203,818 | +1.91% | 0 | - | 233 |
| snake_anaconda | 202,662 | +1.33% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,766 | +0.88% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,834 | -0.58% | 0 | - | 237 |
| gold | 194,271 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,632 (-5.18%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,911 | +2.35% |
| gold | +2,877 | +1.50% |
| benchmark_smallcap | +2,164 | +1.10% |
| oracle | +2,026 | +1.00% |
| unified | +1,642 | +0.77% |
| random_hold | +1,630 | +0.80% |
| intraweek | +994 | +0.47% |
| intramonth | +624 | +0.30% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -458 | -0.22% |
| snake_abs_exit_conv | -462 | -0.21% |
| snake_abs | -464 | -0.22% |
| snake_abs_exit | -599 | -0.28% |
| snake_anaconda | -1,158 | -0.57% |
| snake_viper_tick | -3,634 | -1.77% |
| snake_viper_wild | -3,734 | -1.79% |

Average per day so far: snake_abs_exit_conv Rs +582, unified Rs +574, snake_abs_exit Rs +572, benchmark Rs +488, snake_abs_conv Rs +452, snake_abs Rs +440, intraweek Rs +382, intramonth Rs +273, snake_viper_wild Rs +265, random_hold Rs +176, oracle Rs +136, snake_anaconda Rs +116, snake_viper_tick Rs +104, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -49, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.