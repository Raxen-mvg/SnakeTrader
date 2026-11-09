# Paper trading report

Updated 2026-11-09 13:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,136 | +10.07% | 0 | - | 236 |
| benchmark | 217,618 | +8.81% | 0 | - | 237 |
| intraweek | 215,090 | +7.54% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,190 | +6.59% | 2 | 50% | 330 |
| snake_abs_exit | 212,598 | +6.30% | 2 | 50% | 308 |
| intramonth | 210,238 | +5.12% | 0 | - | 235 |
| snake_abs | 210,125 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,955 | +4.98% | 1 | 100% | 255 |
| oracle | 209,649 | +4.82% | 0 | - | 233 |
| random_hold | 204,502 | +2.25% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,017 | +0.01% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,990 | -0.01% | 7 | 57% | 1,332 |
| benchmark_smallcap | 198,755 | -0.62% | 0 | - | 237 |
| snake_viper_tick | 196,593 | -1.70% | 6 | 50% | 1,154 |
| gold | 192,331 | -3.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,511 (-4.74%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,768 | +2.29% |
| snake_abs_conv | +4,728 | +2.30% |
| intraweek | +4,728 | +2.25% |
| snake_abs | +4,706 | +2.29% |
| unified | +4,526 | +2.10% |
| snake_abs_exit | +4,286 | +2.06% |
| snake_anaconda | +4,190 | +2.14% |
| snake_viper_wild | +3,953 | +2.02% |
| snake_viper_tick | +3,883 | +2.02% |
| oracle | +3,822 | +1.86% |
| intramonth | +2,635 | +1.27% |
| benchmark_smallcap | +1,962 | +1.00% |
| gold | +1,282 | +0.67% |
| random_hold | +595 | +0.29% |
| benchmark | +130 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +671, benchmark Rs +587, intraweek Rs +503, snake_abs_exit_conv Rs +489, snake_abs_exit Rs +467, snake_abs_conv Rs +369, snake_abs Rs +362, intramonth Rs +341, oracle Rs +322, random_hold Rs +150, nifty_calls Rs +61, snake_anaconda Rs +1, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -0, benchmark_smallcap Rs -48, snake_viper_tick Rs -179, gold Rs -256, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.