# Paper trading report

Updated 2026-11-27 12:34 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,503 | +12.25% | 0 | - | 237 |
| unified | 223,542 | +11.77% | 0 | - | 236 |
| oracle | 212,138 | +6.07% | 0 | - | 233 |
| intramonth | 211,108 | +5.55% | 0 | - | 235 |
| random_hold | 210,455 | +5.23% | 13 | 69% | 1,037 |
| intraweek | 208,208 | +4.10% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,968 | +2.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,635 | +1.82% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,670 | +0.83% | 0 | - | 237 |
| snake_abs | 200,498 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,319 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,913 | -3.04% | 3 | 33% | 374 |
| snake_viper_wild | 192,394 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,127 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,808 | -15.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,944 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,890 | +1.94% |
| gold | +3,814 | +2.30% |
| snake_abs_exit_conv | +3,238 | +1.62% |
| snake_abs_conv | +1,952 | +0.98% |
| snake_abs | +1,946 | +0.98% |
| random_hold | +1,861 | +0.89% |
| snake_anaconda | +1,617 | +0.84% |
| intraweek | +1,159 | +0.56% |
| benchmark_smallcap | +830 | +0.41% |
| intramonth | +575 | +0.27% |
| unified | +463 | +0.21% |
| snake_viper_wild | +189 | +0.10% |
| snake_viper_tick | +185 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -98 | -0.05% |
| benchmark | -1,484 | -0.66% |

Average per day so far: benchmark Rs +583, unified Rs +561, oracle Rs +289, intramonth Rs +264, random_hold Rs +249, intraweek Rs +195, snake_abs_exit Rs +127, snake_abs_exit_conv Rs +93, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -719

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.