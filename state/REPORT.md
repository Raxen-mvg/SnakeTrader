# Paper trading report

Updated 2026-11-05 14:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,985 | +7.99% | 0 | - | 236 |
| snake_abs_exit_conv | 214,538 | +7.27% | 1 | 100% | 255 |
| snake_abs_exit | 214,298 | +7.15% | 1 | 100% | 260 |
| benchmark | 214,083 | +7.04% | 0 | - | 237 |
| snake_abs | 211,424 | +5.71% | 1 | 100% | 255 |
| snake_abs_conv | 211,286 | +5.64% | 1 | 100% | 255 |
| intraweek | 210,455 | +5.23% | 25 | 48% | 2,757 |
| intramonth | 207,445 | +3.72% | 0 | - | 235 |
| snake_viper_wild | 205,571 | +2.79% | 3 | 33% | 702 |
| random_hold | 205,001 | +2.50% | 8 | 62% | 649 |
| oracle | 203,842 | +1.92% | 0 | - | 233 |
| snake_anaconda | 202,713 | +1.36% | 3 | 33% | 374 |
| snake_viper_tick | 202,036 | +1.02% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| gold | 194,271 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,609 (-5.20%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,324 | +2.55% |
| gold | +2,877 | +1.50% |
| benchmark_smallcap | +2,477 | +1.26% |
| oracle | +2,049 | +1.02% |
| random_hold | +1,693 | +0.83% |
| unified | +1,546 | +0.72% |
| intraweek | +757 | +0.36% |
| intramonth | +429 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -472 | -0.22% |
| snake_abs_exit_conv | -477 | -0.22% |
| snake_abs | -479 | -0.23% |
| snake_abs_exit | -602 | -0.28% |
| snake_anaconda | -1,107 | -0.54% |
| snake_viper_tick | -3,364 | -1.64% |
| snake_viper_wild | -3,459 | -1.66% |

Average per day so far: snake_abs_exit_conv Rs +582, snake_abs_exit Rs +572, unified Rs +571, benchmark Rs +503, snake_abs_conv Rs +451, snake_abs Rs +439, intraweek Rs +373, snake_viper_wild Rs +279, intramonth Rs +266, random_hold Rs +179, oracle Rs +137, snake_viper_tick Rs +120, snake_anaconda Rs +118, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.