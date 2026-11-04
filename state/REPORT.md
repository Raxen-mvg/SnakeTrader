# Paper trading report

Updated 2026-11-04 11:37 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,822 | +6.41% | 0 | - | 236 |
| intraweek | 208,588 | +4.29% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,484 | +4.24% | 1 | 100% | 255 |
| snake_abs_exit | 208,345 | +4.17% | 1 | 100% | 260 |
| benchmark | 207,328 | +3.66% | 0 | - | 237 |
| snake_viper_wild | 206,766 | +3.38% | 3 | 33% | 702 |
| intramonth | 205,414 | +2.71% | 0 | - | 235 |
| snake_abs | 205,398 | +2.70% | 1 | 100% | 255 |
| snake_abs_conv | 205,243 | +2.62% | 1 | 100% | 255 |
| snake_viper_tick | 203,164 | +1.58% | 2 | 0% | 532 |
| random_hold | 202,379 | +1.19% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,625 | +0.31% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,277 | -1.36% | 3 | 33% | 361 |
| benchmark_smallcap | 194,809 | -2.60% | 0 | - | 237 |
| gold | 190,210 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,741 (-5.63%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,932 | +2.66% |
| snake_abs_exit | +4,331 | +2.12% |
| snake_abs_exit_conv | +4,145 | +2.03% |
| snake_abs_conv | +4,102 | +2.04% |
| snake_abs | +4,089 | +2.03% |
| intraweek | +3,502 | +1.71% |
| snake_anaconda | +3,452 | +1.78% |
| random_hold | +1,911 | +0.95% |
| benchmark_smallcap | +1,872 | +0.97% |
| intramonth | +1,443 | +0.71% |
| unified | +821 | +0.39% |
| oracle | +635 | +0.32% |
| benchmark | +627 | +0.30% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,002 | -1.93% |
| snake_viper_wild | -4,127 | -1.96% |

Average per day so far: unified Rs +475, snake_viper_wild Rs +356, snake_abs_exit_conv Rs +353, snake_abs_exit Rs +348, intraweek Rs +318, benchmark Rs +271, snake_abs_conv Rs +218, snake_abs Rs +216, intramonth Rs +201, snake_viper_tick Rs +198, random_hold Rs +88, nifty_calls Rs +68, oracle Rs +23, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -124, benchmark_smallcap Rs -226, gold Rs -363, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.