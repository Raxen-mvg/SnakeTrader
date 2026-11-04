# Paper trading report

Updated 2026-11-04 12:37 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,906 | +6.95% | 0 | - | 236 |
| snake_abs_exit_conv | 212,136 | +6.07% | 1 | 100% | 255 |
| snake_abs_exit | 211,976 | +5.99% | 1 | 100% | 260 |
| snake_abs | 209,037 | +4.52% | 1 | 100% | 255 |
| intraweek | 208,991 | +4.50% | 25 | 48% | 2,757 |
| snake_abs_conv | 208,881 | +4.44% | 1 | 100% | 255 |
| benchmark | 207,734 | +3.87% | 0 | - | 237 |
| snake_viper_wild | 206,995 | +3.50% | 3 | 33% | 702 |
| intramonth | 206,269 | +3.13% | 0 | - | 235 |
| snake_viper_tick | 203,388 | +1.69% | 2 | 0% | 532 |
| random_hold | 202,891 | +1.45% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,151 | +0.58% | 0 | - | 233 |
| snake_anaconda | 200,491 | +0.24% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,921 | -2.54% | 0 | - | 237 |
| gold | 190,424 | -4.79% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,215 (-5.39%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +7,962 | +3.90% |
| snake_abs_exit_conv | +7,797 | +3.82% |
| snake_abs_conv | +7,740 | +3.85% |
| snake_abs | +7,728 | +3.84% |
| snake_anaconda | +6,666 | +3.44% |
| gold | +5,146 | +2.78% |
| intraweek | +3,906 | +1.90% |
| random_hold | +2,423 | +1.21% |
| intramonth | +2,298 | +1.13% |
| benchmark_smallcap | +1,984 | +1.03% |
| unified | +1,905 | +0.90% |
| oracle | +1,162 | +0.58% |
| benchmark | +1,033 | +0.50% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,779 | -1.82% |
| snake_viper_wild | -3,898 | -1.85% |

Average per day so far: unified Rs +515, snake_abs_exit_conv Rs +506, snake_abs_exit Rs +499, snake_abs_conv Rs +370, snake_viper_wild Rs +368, snake_abs Rs +361, intraweek Rs +333, benchmark Rs +286, intramonth Rs +232, snake_viper_tick Rs +212, random_hold Rs +107, nifty_calls Rs +68, oracle Rs +43, snake_anaconda Rs +22, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -221, gold Rs -355, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.