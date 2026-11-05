# Paper trading report

Updated 2026-11-05 14:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,261 | +8.13% | 0 | - | 236 |
| snake_abs_exit_conv | 214,979 | +7.49% | 1 | 100% | 255 |
| snake_abs_exit | 214,765 | +7.38% | 1 | 100% | 260 |
| benchmark | 214,083 | +7.04% | 0 | - | 237 |
| snake_abs | 211,861 | +5.93% | 1 | 100% | 255 |
| snake_abs_conv | 211,717 | +5.86% | 1 | 100% | 255 |
| intraweek | 209,344 | +4.67% | 25 | 48% | 2,757 |
| intramonth | 208,084 | +4.04% | 0 | - | 235 |
| snake_viper_wild | 204,750 | +2.38% | 3 | 33% | 702 |
| random_hold | 204,729 | +2.36% | 8 | 62% | 649 |
| oracle | 204,335 | +2.17% | 0 | - | 233 |
| snake_anaconda | 202,636 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,235 | +0.62% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| gold | 194,336 | -2.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,503 (-5.25%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,324 | +2.55% |
| gold | +2,943 | +1.54% |
| oracle | +2,543 | +1.26% |
| benchmark_smallcap | +2,377 | +1.21% |
| unified | +1,821 | +0.85% |
| random_hold | +1,420 | +0.70% |
| intramonth | +1,069 | +0.52% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -36 | -0.02% |
| snake_abs_conv | -41 | -0.02% |
| snake_abs | -42 | -0.02% |
| snake_abs_exit | -135 | -0.06% |
| intraweek | -354 | -0.17% |
| snake_anaconda | -1,185 | -0.58% |
| snake_viper_tick | -4,166 | -2.03% |
| snake_viper_wild | -4,280 | -2.05% |

Average per day so far: snake_abs_exit_conv Rs +599, snake_abs_exit Rs +591, unified Rs +581, benchmark Rs +503, snake_abs_conv Rs +469, snake_abs Rs +456, intraweek Rs +334, intramonth Rs +289, snake_viper_wild Rs +238, random_hold Rs +169, oracle Rs +155, snake_anaconda Rs +115, snake_viper_tick Rs +73, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -202, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.