# Paper trading report

Updated 2026-11-04 14:52 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,136 | +7.07% | 0 | - | 236 |
| snake_abs_exit_conv | 213,665 | +6.83% | 1 | 100% | 255 |
| snake_abs_exit | 213,535 | +6.77% | 1 | 100% | 260 |
| snake_abs | 210,549 | +5.27% | 1 | 100% | 255 |
| snake_abs_conv | 210,405 | +5.20% | 1 | 100% | 255 |
| intraweek | 209,355 | +4.68% | 25 | 48% | 2,757 |
| benchmark | 208,652 | +4.33% | 0 | - | 237 |
| snake_viper_wild | 208,421 | +4.21% | 3 | 33% | 702 |
| intramonth | 206,651 | +3.33% | 0 | - | 235 |
| snake_viper_tick | 204,795 | +2.40% | 2 | 0% | 532 |
| random_hold | 202,678 | +1.34% | 8 | 62% | 649 |
| snake_anaconda | 202,358 | +1.18% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,128 | +0.56% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,423 | -1.79% | 0 | - | 237 |
| gold | 191,509 | -4.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,783 (-5.11%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,521 | +4.67% |
| snake_abs_exit_conv | +9,326 | +4.56% |
| snake_abs_conv | +9,264 | +4.61% |
| snake_abs | +9,240 | +4.59% |
| snake_anaconda | +8,534 | +4.40% |
| gold | +6,231 | +3.36% |
| intraweek | +4,270 | +2.08% |
| benchmark_smallcap | +3,486 | +1.81% |
| intramonth | +2,680 | +1.31% |
| random_hold | +2,209 | +1.10% |
| unified | +2,135 | +1.01% |
| benchmark | +1,951 | +0.94% |
| oracle | +1,139 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,372 | -1.15% |
| snake_viper_wild | -2,471 | -1.17% |

Average per day so far: snake_abs_exit_conv Rs +569, snake_abs_exit Rs +564, unified Rs +524, snake_viper_wild Rs +443, snake_abs_conv Rs +434, snake_abs Rs +422, intraweek Rs +346, benchmark Rs +320, snake_viper_tick Rs +300, intramonth Rs +246, snake_anaconda Rs +107, random_hold Rs +99, nifty_calls Rs +68, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -156, gold Rs -314, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.