# Paper trading report

Updated 2026-11-09 12:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,161 | +10.08% | 0 | - | 236 |
| benchmark | 217,189 | +8.60% | 0 | - | 237 |
| intraweek | 214,833 | +7.42% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,486 | +6.24% | 2 | 50% | 330 |
| snake_abs_exit | 212,180 | +6.09% | 2 | 50% | 308 |
| intramonth | 210,369 | +5.18% | 0 | - | 235 |
| snake_abs | 209,969 | +4.99% | 1 | 100% | 255 |
| snake_abs_conv | 209,792 | +4.90% | 1 | 100% | 255 |
| oracle | 209,582 | +4.79% | 0 | - | 233 |
| random_hold | 204,435 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,643 | -0.18% | 3 | 33% | 374 |
| snake_viper_wild | 199,019 | -0.49% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,621 | -0.69% | 0 | - | 237 |
| snake_viper_tick | 195,639 | -2.18% | 6 | 50% | 1,154 |
| gold | 192,479 | -3.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,423 (-4.79%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,565 | +2.22% |
| unified | +4,552 | +2.11% |
| snake_abs | +4,550 | +2.21% |
| intraweek | +4,471 | +2.12% |
| snake_abs_exit_conv | +4,064 | +1.95% |
| snake_abs_exit | +3,868 | +1.86% |
| snake_anaconda | +3,816 | +1.95% |
| oracle | +3,755 | +1.82% |
| snake_viper_wild | +2,982 | +1.52% |
| snake_viper_tick | +2,929 | +1.52% |
| intramonth | +2,766 | +1.33% |
| benchmark_smallcap | +1,827 | +0.93% |
| gold | +1,430 | +0.75% |
| random_hold | +529 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -298 | -0.14% |

Average per day so far: unified Rs +672, benchmark Rs +573, intraweek Rs +494, snake_abs_exit_conv Rs +462, snake_abs_exit Rs +451, snake_abs_conv Rs +363, snake_abs Rs +356, intramonth Rs +346, oracle Rs +319, random_hold Rs +148, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -14, snake_viper_wild Rs -45, benchmark_smallcap Rs -53, snake_viper_tick Rs -230, gold Rs -251, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.