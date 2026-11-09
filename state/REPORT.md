# Paper trading report

Updated 2026-11-09 12:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,099 | +10.05% | 0 | - | 236 |
| benchmark | 217,143 | +8.57% | 0 | - | 237 |
| intraweek | 214,375 | +7.19% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,330 | +6.17% | 2 | 50% | 330 |
| snake_abs_exit | 211,939 | +5.97% | 2 | 50% | 308 |
| intramonth | 210,296 | +5.15% | 0 | - | 235 |
| snake_abs | 209,737 | +4.87% | 1 | 100% | 255 |
| snake_abs_conv | 209,559 | +4.78% | 1 | 100% | 255 |
| oracle | 209,490 | +4.75% | 0 | - | 233 |
| random_hold | 204,438 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,416 | -0.29% | 3 | 33% | 374 |
| snake_viper_wild | 199,164 | -0.42% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,654 | -0.67% | 0 | - | 237 |
| snake_viper_tick | 195,781 | -2.11% | 6 | 50% | 1,154 |
| gold | 192,660 | -3.67% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,272 (-4.86%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,489 | +2.08% |
| snake_abs_conv | +4,332 | +2.11% |
| snake_abs | +4,318 | +2.10% |
| intraweek | +4,012 | +1.91% |
| snake_abs_exit_conv | +3,909 | +1.88% |
| oracle | +3,663 | +1.78% |
| snake_abs_exit | +3,627 | +1.74% |
| snake_anaconda | +3,589 | +1.83% |
| snake_viper_wild | +3,127 | +1.59% |
| snake_viper_tick | +3,071 | +1.59% |
| intramonth | +2,693 | +1.30% |
| benchmark_smallcap | +1,861 | +0.95% |
| gold | +1,611 | +0.84% |
| random_hold | +532 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -344 | -0.16% |

Average per day so far: unified Rs +670, benchmark Rs +571, intraweek Rs +479, snake_abs_exit_conv Rs +457, snake_abs_exit Rs +442, snake_abs_conv Rs +354, snake_abs Rs +348, intramonth Rs +343, oracle Rs +316, random_hold Rs +148, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -23, snake_viper_wild Rs -38, benchmark_smallcap Rs -52, snake_viper_tick Rs -222, gold Rs -245, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.