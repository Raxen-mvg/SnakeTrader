# Paper trading report

Updated 2026-11-06 12:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,101 | +7.55% | 0 | - | 237 |
| unified | 214,807 | +7.40% | 0 | - | 236 |
| intraweek | 209,227 | +4.61% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,583 | +4.29% | 1 | 100% | 255 |
| snake_abs_exit | 208,416 | +4.21% | 1 | 100% | 260 |
| intramonth | 207,096 | +3.55% | 0 | - | 235 |
| snake_abs | 205,555 | +2.78% | 1 | 100% | 255 |
| snake_abs_conv | 205,379 | +2.69% | 1 | 100% | 255 |
| oracle | 204,931 | +2.47% | 0 | - | 233 |
| random_hold | 203,123 | +1.56% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,846 | -2.08% | 3 | 33% | 374 |
| snake_viper_wild | 195,571 | -2.21% | 3 | 33% | 702 |
| benchmark_smallcap | 194,697 | -2.65% | 0 | - | 237 |
| snake_viper_tick | 192,260 | -3.87% | 2 | 0% | 532 |
| gold | 190,259 | -4.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,934 (-6.53%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,331 | +0.62% |
| oracle | +859 | +0.42% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -192 | -0.09% |
| intramonth | -852 | -0.41% |
| unified | -1,176 | -0.54% |
| random_hold | -1,200 | -0.59% |
| gold | -3,962 | -2.04% |
| benchmark_smallcap | -3,991 | -2.01% |
| snake_abs | -6,134 | -2.90% |
| snake_abs_conv | -6,166 | -2.92% |
| snake_abs_exit_conv | -6,220 | -2.90% |
| snake_abs_exit | -6,243 | -2.91% |
| snake_anaconda | -6,633 | -3.28% |
| snake_viper_tick | -8,878 | -4.41% |
| snake_viper_wild | -9,084 | -4.44% |

Average per day so far: benchmark Rs +521, unified Rs +511, snake_abs_exit_conv Rs +330, snake_abs_exit Rs +324, intraweek Rs +318, intramonth Rs +245, snake_abs_conv Rs +207, snake_abs Rs +206, oracle Rs +170, random_hold Rs +108, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -173, snake_viper_wild Rs -211, benchmark_smallcap Rs -212, gold Rs -336, snake_nonews Rs -411, snake_viper_tick Rs -430, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.