# Paper trading report

Updated 2026-11-04 13:31 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,097 | +7.05% | 0 | - | 236 |
| snake_abs_exit_conv | 212,482 | +6.24% | 1 | 100% | 255 |
| snake_abs_exit | 212,351 | +6.17% | 1 | 100% | 260 |
| snake_abs | 209,384 | +4.69% | 1 | 100% | 255 |
| snake_abs_conv | 209,229 | +4.62% | 1 | 100% | 255 |
| intraweek | 209,210 | +4.61% | 25 | 48% | 2,757 |
| benchmark | 208,308 | +4.15% | 0 | - | 237 |
| snake_viper_wild | 207,012 | +3.51% | 3 | 33% | 702 |
| intramonth | 206,287 | +3.14% | 0 | - | 235 |
| snake_viper_tick | 203,405 | +1.70% | 2 | 0% | 532 |
| random_hold | 202,783 | +1.39% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,164 | +0.58% | 0 | - | 233 |
| snake_anaconda | 201,023 | +0.51% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,706 | -2.15% | 0 | - | 237 |
| gold | 190,555 | -4.72% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,294 (-5.35%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,336 | +4.09% |
| snake_abs_exit_conv | +8,143 | +3.98% |
| snake_abs_conv | +8,088 | +4.02% |
| snake_abs | +8,075 | +4.01% |
| snake_anaconda | +7,199 | +3.71% |
| gold | +5,277 | +2.85% |
| intraweek | +4,125 | +2.01% |
| benchmark_smallcap | +2,769 | +1.44% |
| intramonth | +2,316 | +1.14% |
| random_hold | +2,315 | +1.16% |
| unified | +2,096 | +0.99% |
| benchmark | +1,606 | +0.78% |
| oracle | +1,175 | +0.59% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,762 | -1.82% |
| snake_viper_wild | -3,881 | -1.84% |

Average per day so far: unified Rs +522, snake_abs_exit_conv Rs +520, snake_abs_exit Rs +515, snake_abs_conv Rs +385, snake_abs Rs +375, snake_viper_wild Rs +369, intraweek Rs +341, benchmark Rs +308, intramonth Rs +233, snake_viper_tick Rs +213, random_hold Rs +103, nifty_calls Rs +68, snake_anaconda Rs +47, oracle Rs +43, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -187, gold Rs -350, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.