# Paper trading report

Updated 2026-11-04 13:37 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,936 | +6.97% | 0 | - | 236 |
| snake_abs_exit_conv | 212,616 | +6.31% | 1 | 100% | 255 |
| snake_abs_exit | 212,473 | +6.24% | 1 | 100% | 260 |
| snake_abs | 209,515 | +4.76% | 1 | 100% | 255 |
| snake_abs_conv | 209,361 | +4.68% | 1 | 100% | 255 |
| intraweek | 209,338 | +4.67% | 25 | 48% | 2,757 |
| benchmark | 208,629 | +4.31% | 0 | - | 237 |
| snake_viper_wild | 206,897 | +3.45% | 3 | 33% | 702 |
| intramonth | 206,165 | +3.08% | 0 | - | 235 |
| snake_viper_tick | 203,293 | +1.65% | 2 | 0% | 532 |
| random_hold | 202,622 | +1.31% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,151 | +0.58% | 0 | - | 233 |
| snake_anaconda | 201,151 | +0.58% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,717 | -2.14% | 0 | - | 237 |
| gold | 191,377 | -4.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,226 (-5.39%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,459 | +4.15% |
| snake_abs_exit_conv | +8,277 | +4.05% |
| snake_abs_conv | +8,220 | +4.09% |
| snake_abs | +8,206 | +4.08% |
| snake_anaconda | +7,327 | +3.78% |
| gold | +6,099 | +3.29% |
| intraweek | +4,252 | +2.07% |
| benchmark_smallcap | +2,780 | +1.44% |
| intramonth | +2,194 | +1.08% |
| random_hold | +2,154 | +1.07% |
| unified | +1,935 | +0.91% |
| benchmark | +1,928 | +0.93% |
| oracle | +1,162 | +0.58% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,874 | -1.87% |
| snake_viper_wild | -3,995 | -1.89% |

Average per day so far: snake_abs_exit_conv Rs +526, snake_abs_exit Rs +520, unified Rs +516, snake_abs_conv Rs +390, snake_abs Rs +381, snake_viper_wild Rs +363, intraweek Rs +346, benchmark Rs +320, intramonth Rs +228, snake_viper_tick Rs +206, random_hold Rs +97, nifty_calls Rs +68, snake_anaconda Rs +52, oracle Rs +43, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -186, gold Rs -319, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.