# Paper trading report

Updated 2026-11-09 10:39 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,141 | +10.07% | 0 | - | 236 |
| benchmark | 217,227 | +8.61% | 0 | - | 237 |
| intraweek | 217,176 | +8.59% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 212,305 | +6.15% | 2 | 50% | 330 |
| snake_abs_exit | 212,277 | +6.14% | 2 | 50% | 308 |
| snake_abs | 210,210 | +5.11% | 1 | 100% | 255 |
| intramonth | 210,120 | +5.06% | 0 | - | 235 |
| snake_abs_conv | 210,036 | +5.02% | 1 | 100% | 255 |
| oracle | 209,826 | +4.91% | 0 | - | 233 |
| random_hold | 204,155 | +2.08% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,741 | -0.13% | 3 | 33% | 374 |
| benchmark_smallcap | 198,654 | -0.67% | 0 | - | 237 |
| snake_viper_wild | 197,379 | -1.31% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,026 | -2.99% | 6 | 50% | 1,154 |
| gold | 192,939 | -3.53% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,866 (-4.57%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,814 | +3.24% |
| snake_abs_conv | +4,809 | +2.34% |
| snake_abs | +4,791 | +2.33% |
| unified | +4,532 | +2.10% |
| oracle | +3,999 | +1.94% |
| snake_abs_exit | +3,965 | +1.90% |
| snake_anaconda | +3,914 | +2.00% |
| snake_abs_exit_conv | +3,883 | +1.86% |
| intramonth | +2,517 | +1.21% |
| gold | +1,891 | +0.99% |
| benchmark_smallcap | +1,861 | +0.95% |
| snake_viper_wild | +1,342 | +0.69% |
| snake_viper_tick | +1,316 | +0.68% |
| random_hold | +248 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -260 | -0.12% |

Average per day so far: unified Rs +671, benchmark Rs +574, intraweek Rs +573, snake_abs_exit_conv Rs +456, snake_abs_exit Rs +455, snake_abs_conv Rs +372, snake_abs Rs +365, intramonth Rs +337, oracle Rs +328, random_hold Rs +138, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -10, benchmark_smallcap Rs -52, snake_viper_wild Rs -119, gold Rs -235, snake_viper_tick Rs -314, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.