# Paper trading report

Updated 2026-11-04 10:25 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,279 | +6.64% | 0 | - | 236 |
| snake_abs_exit_conv | 208,852 | +4.43% | 1 | 100% | 255 |
| snake_abs_exit | 208,693 | +4.35% | 1 | 100% | 260 |
| benchmark | 207,864 | +3.93% | 0 | - | 237 |
| intraweek | 207,003 | +3.50% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,647 | +3.32% | 3 | 33% | 702 |
| snake_abs | 205,759 | +2.88% | 1 | 100% | 255 |
| snake_abs_conv | 205,606 | +2.80% | 1 | 100% | 255 |
| intramonth | 205,351 | +2.68% | 0 | - | 235 |
| snake_viper_tick | 203,041 | +1.52% | 2 | 0% | 532 |
| random_hold | 202,290 | +1.15% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,319 | +0.16% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,519 | -1.24% | 3 | 33% | 361 |
| benchmark_smallcap | 194,394 | -2.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,415 | -6.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,579 (-5.71%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,678 | +2.29% |
| snake_abs_exit_conv | +4,514 | +2.21% |
| snake_abs_conv | +4,465 | +2.22% |
| snake_abs | +4,450 | +2.21% |
| snake_anaconda | +3,694 | +1.91% |
| gold | +2,137 | +1.15% |
| intraweek | +1,918 | +0.94% |
| random_hold | +1,822 | +0.91% |
| benchmark_smallcap | +1,457 | +0.76% |
| intramonth | +1,380 | +0.68% |
| unified | +1,278 | +0.60% |
| benchmark | +1,163 | +0.56% |
| oracle | +330 | +0.17% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,125 | -1.99% |
| snake_viper_wild | -4,245 | -2.01% |

Average per day so far: unified Rs +492, snake_abs_exit_conv Rs +369, snake_abs_exit Rs +362, snake_viper_wild Rs +350, benchmark Rs +291, intraweek Rs +259, snake_abs_conv Rs +234, snake_abs Rs +230, intramonth Rs +198, snake_viper_tick Rs +190, random_hold Rs +85, nifty_calls Rs +68, oracle Rs +12, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -113, benchmark_smallcap Rs -244, snake_nonews Rs -444, gold Rs -466, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.