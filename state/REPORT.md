# Paper trading report

Updated 2026-11-06 11:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,558 | +7.28% | 0 | - | 237 |
| unified | 214,495 | +7.25% | 0 | - | 236 |
| intraweek | 210,958 | +5.48% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,084 | +4.54% | 1 | 100% | 255 |
| snake_abs_exit | 208,878 | +4.44% | 1 | 100% | 260 |
| intramonth | 206,702 | +3.35% | 0 | - | 235 |
| snake_abs | 206,042 | +3.02% | 1 | 100% | 255 |
| snake_abs_conv | 205,873 | +2.94% | 1 | 100% | 255 |
| oracle | 204,563 | +2.28% | 0 | - | 233 |
| random_hold | 203,309 | +1.65% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,335 | -1.83% | 3 | 33% | 374 |
| snake_viper_wild | 195,474 | -2.26% | 3 | 33% | 702 |
| benchmark_smallcap | 194,507 | -2.75% | 0 | - | 237 |
| snake_viper_tick | 192,165 | -3.92% | 2 | 0% | 532 |
| gold | 190,276 | -4.86% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,158 (-6.42%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,540 | +0.73% |
| benchmark | +788 | +0.37% |
| oracle | +491 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,014 | -0.50% |
| intramonth | -1,247 | -0.60% |
| unified | -1,488 | -0.69% |
| gold | -3,946 | -2.03% |
| benchmark_smallcap | -4,181 | -2.10% |
| snake_abs | -5,646 | -2.67% |
| snake_abs_conv | -5,672 | -2.68% |
| snake_abs_exit_conv | -5,719 | -2.66% |
| snake_abs_exit | -5,781 | -2.69% |
| snake_anaconda | -6,144 | -3.03% |
| snake_viper_tick | -8,973 | -4.46% |
| snake_viper_wild | -9,182 | -4.49% |

Average per day so far: benchmark Rs +502, unified Rs +500, intraweek Rs +378, snake_abs_exit_conv Rs +349, snake_abs_exit Rs +341, intramonth Rs +231, snake_abs_conv Rs +226, snake_abs Rs +224, oracle Rs +157, random_hold Rs +114, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -153, snake_viper_wild Rs -216, benchmark_smallcap Rs -220, gold Rs -335, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.