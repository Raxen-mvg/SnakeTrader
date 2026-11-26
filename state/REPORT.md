# Paper trading report

Updated 2026-11-26 09:59 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,275 | +12.64% | 0 | - | 237 |
| unified | 224,034 | +12.02% | 0 | - | 236 |
| oracle | 213,698 | +6.85% | 0 | - | 233 |
| intramonth | 211,753 | +5.88% | 0 | - | 235 |
| random_hold | 210,350 | +5.17% | 13 | 69% | 1,037 |
| intraweek | 208,414 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,390 | +1.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,781 | +1.39% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,719 | +0.36% | 1 | 100% | 255 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| snake_abs_conv | 200,544 | +0.27% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,002 | -2.00% | 16 | 50% | 2,827 |
| snake_anaconda | 194,888 | -2.56% | 3 | 33% | 374 |
| snake_viper_tick | 192,668 | -3.67% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,687 | -16.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,482 (-5.26%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,091 | +1.88% |
| benchmark_smallcap | +1,850 | +0.93% |
| intraweek | +1,670 | +0.81% |
| snake_abs_exit | +1,135 | +0.56% |
| random_hold | +858 | +0.41% |
| snake_abs_exit_conv | +805 | +0.40% |
| snake_abs_conv | +572 | +0.29% |
| snake_abs | +569 | +0.28% |
| snake_anaconda | +335 | +0.17% |
| benchmark | +252 | +0.11% |
| intramonth | +60 | +0.03% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -66 | -0.03% |
| oracle | -97 | -0.04% |
| snake_viper_tick | -1,509 | -0.78% |
| snake_viper_wild | -1,541 | -0.78% |

Average per day so far: benchmark Rs +616, unified Rs +586, oracle Rs +334, intramonth Rs +287, random_hold Rs +252, intraweek Rs +205, snake_abs_exit Rs +89, snake_abs_exit_conv Rs +73, nifty_calls Rs +45, snake_abs Rs +18, benchmark_smallcap Rs +18, snake_abs_conv Rs +14, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -121, snake_anaconda Rs -142, snake_viper_tick Rs -244, snake_nonews Rs -284, snake Rs -304, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.