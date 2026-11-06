# Paper trading report

Updated 2026-11-06 11:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,694 | +7.35% | 0 | - | 236 |
| benchmark | 214,443 | +7.22% | 0 | - | 237 |
| intraweek | 211,209 | +5.60% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,291 | +4.65% | 1 | 100% | 255 |
| snake_abs_exit | 209,079 | +4.54% | 1 | 100% | 260 |
| intramonth | 206,691 | +3.35% | 0 | - | 235 |
| snake_abs | 206,245 | +3.12% | 1 | 100% | 255 |
| snake_abs_conv | 206,078 | +3.04% | 1 | 100% | 255 |
| oracle | 204,710 | +2.35% | 0 | - | 233 |
| random_hold | 203,243 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,603 | -1.70% | 3 | 33% | 374 |
| snake_viper_wild | 195,815 | -2.09% | 3 | 33% | 702 |
| benchmark_smallcap | 194,563 | -2.72% | 0 | - | 237 |
| snake_viper_tick | 192,497 | -3.75% | 2 | 0% | 532 |
| gold | 189,963 | -5.02% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,294 (-6.35%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,790 | +0.85% |
| benchmark | +673 | +0.32% |
| oracle | +638 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,080 | -0.53% |
| intramonth | -1,258 | -0.60% |
| unified | -1,289 | -0.60% |
| benchmark_smallcap | -4,125 | -2.08% |
| gold | -4,258 | -2.19% |
| snake_abs | -5,444 | -2.57% |
| snake_abs_conv | -5,467 | -2.58% |
| snake_abs_exit_conv | -5,512 | -2.57% |
| snake_abs_exit | -5,580 | -2.60% |
| snake_anaconda | -5,876 | -2.90% |
| snake_viper_tick | -8,641 | -4.30% |
| snake_viper_wild | -8,841 | -4.32% |

Average per day so far: unified Rs +507, benchmark Rs +498, intraweek Rs +387, snake_abs_exit_conv Rs +357, snake_abs_exit Rs +349, snake_abs_conv Rs +234, snake_abs Rs +231, intramonth Rs +231, oracle Rs +162, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -142, snake_viper_wild Rs -199, benchmark_smallcap Rs -217, gold Rs -346, snake_nonews Rs -411, snake_viper_tick Rs -417, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.