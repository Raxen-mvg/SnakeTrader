# Paper trading report

Updated 2026-11-09 12:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,672 | +9.84% | 0 | - | 236 |
| benchmark | 217,090 | +8.54% | 0 | - | 237 |
| intraweek | 215,035 | +7.52% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,427 | +6.21% | 2 | 50% | 330 |
| snake_abs_exit | 212,128 | +6.06% | 2 | 50% | 308 |
| intramonth | 209,950 | +4.97% | 0 | - | 235 |
| snake_abs | 209,919 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,745 | +4.87% | 1 | 100% | 255 |
| oracle | 209,512 | +4.76% | 0 | - | 233 |
| random_hold | 204,426 | +2.21% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,574 | -0.21% | 3 | 33% | 374 |
| snake_viper_wild | 199,135 | -0.43% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,542 | -0.73% | 0 | - | 237 |
| snake_viper_tick | 195,753 | -2.12% | 6 | 50% | 1,154 |
| gold | 192,544 | -3.73% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,304 (-4.85%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +4,672 | +2.22% |
| snake_abs_conv | +4,518 | +2.20% |
| snake_abs | +4,500 | +2.19% |
| unified | +4,063 | +1.88% |
| snake_abs_exit_conv | +4,005 | +1.92% |
| snake_abs_exit | +3,816 | +1.83% |
| snake_anaconda | +3,747 | +1.91% |
| oracle | +3,685 | +1.79% |
| snake_viper_wild | +3,097 | +1.58% |
| snake_viper_tick | +3,043 | +1.58% |
| intramonth | +2,347 | +1.13% |
| benchmark_smallcap | +1,749 | +0.89% |
| gold | +1,496 | +0.78% |
| random_hold | +520 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -398 | -0.18% |

Average per day so far: unified Rs +656, benchmark Rs +570, intraweek Rs +501, snake_abs_exit_conv Rs +460, snake_abs_exit Rs +449, snake_abs_conv Rs +361, snake_abs Rs +354, intramonth Rs +332, oracle Rs +317, random_hold Rs +148, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -17, snake_viper_wild Rs -39, benchmark_smallcap Rs -56, snake_viper_tick Rs -224, gold Rs -249, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.