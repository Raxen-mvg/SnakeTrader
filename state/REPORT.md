# Paper trading report

Updated 2026-11-11 13:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,154 | +10.08% | 0 | - | 236 |
| benchmark | 219,997 | +10.00% | 0 | - | 237 |
| snake_abs_exit_conv | 217,402 | +8.70% | 2 | 50% | 345 |
| snake_abs_exit | 216,284 | +8.14% | 2 | 50% | 345 |
| snake_abs | 214,065 | +7.03% | 1 | 100% | 255 |
| snake_abs_conv | 213,905 | +6.95% | 1 | 100% | 255 |
| intraweek | 213,398 | +6.70% | 30 | 53% | 3,302 |
| oracle | 211,615 | +5.81% | 0 | - | 233 |
| intramonth | 211,175 | +5.59% | 0 | - | 235 |
| random_hold | 206,842 | +3.42% | 9 | 67% | 709 |
| snake_viper_wild | 204,523 | +2.26% | 10 | 50% | 1,825 |
| snake_anaconda | 204,324 | +2.16% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,036 | +0.52% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,975 | +0.49% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,733 | -5.13% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,119 (-4.44%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,093 | +3.59% |
| snake_viper_tick | +6,959 | +3.59% |
| snake_abs_exit_conv | +5,493 | +2.59% |
| snake_anaconda | +4,858 | +2.44% |
| snake_abs_conv | +4,428 | +2.11% |
| snake_abs | +4,418 | +2.11% |
| snake_abs_exit | +4,300 | +2.03% |
| benchmark_smallcap | +2,802 | +1.41% |
| benchmark | +1,905 | +0.87% |
| random_hold | +1,881 | +0.92% |
| oracle | +1,697 | +0.81% |
| intramonth | +566 | +0.27% |
| unified | +407 | +0.18% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,144 | -0.53% |
| gold | -2,400 | -1.25% |

Average per day so far: unified Rs +650, benchmark Rs +645, snake_abs_exit_conv Rs +621, snake_abs_exit Rs +582, snake_abs_conv Rs +497, snake_abs Rs +485, intraweek Rs +432, oracle Rs +375, intramonth Rs +360, random_hold Rs +221, snake_viper_wild Rs +197, snake_anaconda Rs +166, nifty_calls Rs +59, snake_viper_tick Rs +52, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -331, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.