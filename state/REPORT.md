# Paper trading report

Updated 2026-11-05 14:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,088 | +8.04% | 0 | - | 236 |
| snake_abs_exit_conv | 214,384 | +7.19% | 1 | 100% | 255 |
| snake_abs_exit | 214,143 | +7.07% | 1 | 100% | 260 |
| benchmark | 214,030 | +7.01% | 0 | - | 237 |
| snake_abs | 211,269 | +5.63% | 1 | 100% | 255 |
| snake_abs_conv | 211,131 | +5.57% | 1 | 100% | 255 |
| intraweek | 210,272 | +5.14% | 25 | 48% | 2,757 |
| intramonth | 207,595 | +3.80% | 0 | - | 235 |
| snake_viper_wild | 205,593 | +2.80% | 3 | 33% | 702 |
| random_hold | 205,050 | +2.52% | 8 | 62% | 649 |
| oracle | 203,619 | +1.81% | 0 | - | 233 |
| snake_anaconda | 202,551 | +1.27% | 3 | 33% | 374 |
| snake_viper_tick | 202,058 | +1.03% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| gold | 194,139 | -2.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,557 (-5.22%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,271 | +2.52% |
| gold | +2,745 | +1.43% |
| benchmark_smallcap | +2,489 | +1.26% |
| oracle | +1,827 | +0.91% |
| random_hold | +1,741 | +0.86% |
| unified | +1,649 | +0.77% |
| intramonth | +579 | +0.28% |
| intraweek | +574 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -627 | -0.30% |
| snake_abs_exit_conv | -631 | -0.29% |
| snake_abs | -634 | -0.30% |
| snake_abs_exit | -757 | -0.35% |
| snake_anaconda | -1,269 | -0.62% |
| snake_viper_tick | -3,342 | -1.63% |
| snake_viper_wild | -3,437 | -1.64% |

Average per day so far: snake_abs_exit_conv Rs +575, unified Rs +575, snake_abs_exit Rs +566, benchmark Rs +501, snake_abs_conv Rs +445, snake_abs Rs +433, intraweek Rs +367, snake_viper_wild Rs +280, intramonth Rs +271, random_hold Rs +180, oracle Rs +129, snake_viper_tick Rs +121, snake_anaconda Rs +111, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -35, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.