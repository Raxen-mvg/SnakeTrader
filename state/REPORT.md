# Paper trading report

Updated 2026-11-05 15:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,177 | +8.09% | 0 | - | 236 |
| snake_abs_exit_conv | 214,936 | +7.47% | 1 | 100% | 255 |
| snake_abs_exit | 214,818 | +7.41% | 1 | 100% | 260 |
| benchmark | 213,969 | +6.98% | 0 | - | 237 |
| snake_abs | 211,811 | +5.91% | 1 | 100% | 255 |
| snake_abs_conv | 211,674 | +5.84% | 1 | 100% | 255 |
| intraweek | 208,761 | +4.38% | 25 | 48% | 2,757 |
| intramonth | 208,000 | +4.00% | 0 | - | 235 |
| snake_viper_wild | 204,609 | +2.31% | 3 | 33% | 702 |
| random_hold | 204,271 | +2.14% | 8 | 62% | 649 |
| oracle | 204,185 | +2.09% | 0 | - | 233 |
| snake_anaconda | 202,699 | +1.35% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,093 | +0.55% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,621 | -0.69% | 0 | - | 237 |
| gold | 194,205 | -2.90% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,359 (-5.32%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,210 | +2.50% |
| gold | +2,811 | +1.47% |
| oracle | +2,393 | +1.19% |
| benchmark_smallcap | +1,951 | +0.99% |
| unified | +1,737 | +0.81% |
| intramonth | +984 | +0.47% |
| random_hold | +962 | +0.47% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -79 | -0.04% |
| snake_abs_exit | -82 | -0.04% |
| snake_abs_conv | -84 | -0.04% |
| snake_abs | -93 | -0.04% |
| intraweek | -937 | -0.45% |
| snake_anaconda | -1,121 | -0.55% |
| snake_viper_tick | -4,307 | -2.10% |
| snake_viper_wild | -4,421 | -2.12% |

Average per day so far: snake_abs_exit_conv Rs +597, snake_abs_exit Rs +593, unified Rs +578, benchmark Rs +499, snake_abs_conv Rs +467, snake_abs Rs +454, intraweek Rs +313, intramonth Rs +286, snake_viper_wild Rs +230, random_hold Rs +153, oracle Rs +149, snake_anaconda Rs +117, nifty_calls Rs +66, snake_viper_tick Rs +64, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -57, gold Rs -207, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.