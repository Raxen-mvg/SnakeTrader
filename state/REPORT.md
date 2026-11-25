# Paper trading report

Updated 2026-11-25 09:17 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,597 | +12.80% | 0 | - | 236 |
| benchmark | 224,411 | +12.21% | 0 | - | 237 |
| intramonth | 213,531 | +6.76% | 0 | - | 235 |
| oracle | 213,504 | +6.75% | 0 | - | 233 |
| intraweek | 212,781 | +6.39% | 40 | 55% | 4,400 |
| random_hold | 210,050 | +5.03% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,494 | +4.25% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,715 | +3.86% | 2 | 50% | 345 |
| snake_abs | 206,415 | +3.21% | 1 | 100% | 255 |
| snake_abs_conv | 206,274 | +3.14% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,124 | +0.56% | 16 | 50% | 2,827 |
| benchmark_smallcap | 200,033 | +0.02% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,660 | -0.17% | 3 | 33% | 374 |
| snake_viper_tick | 197,693 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,287 (-4.36%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,938 | +1.33% |
| random_hold | +1,624 | +0.78% |
| unified | +1,312 | +0.58% |
| oracle | +1,162 | +0.55% |
| intraweek | +1,162 | +0.55% |
| benchmark_smallcap | +1,054 | +0.53% |
| snake_abs_exit | +999 | +0.48% |
| snake_abs_conv | +971 | +0.47% |
| snake_anaconda | +956 | +0.48% |
| snake_abs | +955 | +0.47% |
| intramonth | +779 | +0.37% |
| snake_abs_exit_conv | +669 | +0.32% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_viper_wild | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | +0 | +0.00% |
| gold | -2,910 | -1.72% |

Average per day so far: unified Rs +640, benchmark Rs +610, intramonth Rs +338, oracle Rs +338, intraweek Rs +320, random_hold Rs +251, snake_abs_exit Rs +230, snake_abs_exit_conv Rs +209, snake_abs_conv Rs +170, snake_abs Rs +169, nifty_calls Rs +46, snake_viper_wild Rs +35, benchmark_smallcap Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -10, snake_viper_tick Rs -80, snake_nonews Rs -292, snake Rs -311, gold Rs -837

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.