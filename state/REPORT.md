# Paper trading report

Updated 2026-11-04 10:22 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,080 | +6.54% | 0 | - | 236 |
| snake_abs_exit_conv | 208,893 | +4.45% | 1 | 100% | 255 |
| snake_abs_exit | 208,712 | +4.36% | 1 | 100% | 260 |
| benchmark | 208,086 | +4.04% | 0 | - | 237 |
| intraweek | 207,520 | +3.76% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,623 | +3.31% | 3 | 33% | 702 |
| snake_abs | 205,801 | +2.90% | 1 | 100% | 255 |
| snake_abs_conv | 205,648 | +2.82% | 1 | 100% | 255 |
| intramonth | 205,387 | +2.69% | 0 | - | 235 |
| snake_viper_tick | 203,017 | +1.51% | 2 | 0% | 532 |
| random_hold | 202,446 | +1.22% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,377 | +0.19% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,672 | -1.16% | 3 | 33% | 361 |
| benchmark_smallcap | 194,473 | -2.76% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,645 | -6.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,605 (-5.70%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,697 | +2.30% |
| snake_abs_exit_conv | +4,555 | +2.23% |
| snake_abs_conv | +4,507 | +2.24% |
| snake_abs | +4,492 | +2.23% |
| snake_anaconda | +3,848 | +1.99% |
| intraweek | +2,435 | +1.19% |
| gold | +2,367 | +1.28% |
| random_hold | +1,978 | +0.99% |
| benchmark_smallcap | +1,536 | +0.80% |
| intramonth | +1,416 | +0.69% |
| benchmark | +1,385 | +0.67% |
| unified | +1,079 | +0.51% |
| oracle | +387 | +0.19% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,149 | -2.00% |
| snake_viper_wild | -4,270 | -2.02% |

Average per day so far: unified Rs +484, snake_abs_exit_conv Rs +371, snake_abs_exit Rs +363, snake_viper_wild Rs +349, benchmark Rs +299, intraweek Rs +279, snake_abs_conv Rs +235, snake_abs Rs +232, intramonth Rs +200, snake_viper_tick Rs +189, random_hold Rs +91, nifty_calls Rs +68, oracle Rs +14, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -106, benchmark_smallcap Rs -240, snake_nonews Rs -444, gold Rs -458, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.