# Paper trading report

Updated 2026-11-04 11:26 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,110 | +6.05% | 0 | - | 236 |
| snake_abs_exit_conv | 208,813 | +4.41% | 1 | 100% | 255 |
| snake_abs_exit | 208,668 | +4.33% | 1 | 100% | 260 |
| intraweek | 208,404 | +4.20% | 25 | 48% | 2,757 |
| benchmark | 207,650 | +3.83% | 0 | - | 237 |
| snake_viper_wild | 206,735 | +3.37% | 3 | 33% | 702 |
| snake_abs | 205,720 | +2.86% | 1 | 100% | 255 |
| snake_abs_conv | 205,567 | +2.78% | 1 | 100% | 255 |
| intramonth | 205,137 | +2.57% | 0 | - | 235 |
| snake_viper_tick | 203,134 | +1.57% | 2 | 0% | 532 |
| random_hold | 202,183 | +1.09% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,444 | +0.22% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,492 | -1.25% | 3 | 33% | 361 |
| benchmark_smallcap | 194,764 | -2.62% | 0 | - | 237 |
| gold | 189,881 | -5.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 188,511 (-5.74%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,653 | +2.28% |
| gold | +4,603 | +2.48% |
| snake_abs_exit_conv | +4,474 | +2.19% |
| snake_abs_conv | +4,426 | +2.20% |
| snake_abs | +4,410 | +2.19% |
| snake_anaconda | +3,668 | +1.89% |
| intraweek | +3,319 | +1.62% |
| benchmark_smallcap | +1,827 | +0.95% |
| random_hold | +1,715 | +0.85% |
| intramonth | +1,166 | +0.57% |
| benchmark | +949 | +0.46% |
| oracle | +455 | +0.23% |
| unified | +109 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,033 | -1.95% |
| snake_viper_wild | -4,158 | -1.97% |

Average per day so far: unified Rs +449, snake_abs_exit_conv Rs +367, snake_abs_exit Rs +361, snake_viper_wild Rs +354, intraweek Rs +311, benchmark Rs +283, snake_abs_conv Rs +232, snake_abs Rs +229, snake_viper_tick Rs +196, intramonth Rs +190, random_hold Rs +81, nifty_calls Rs +68, oracle Rs +16, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -114, benchmark_smallcap Rs -228, gold Rs -375, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.