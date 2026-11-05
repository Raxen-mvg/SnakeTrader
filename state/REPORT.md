# Paper trading report

Updated 2026-11-05 09:28 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,900 | +8.95% | 0 | - | 236 |
| snake_abs_exit_conv | 216,785 | +8.39% | 1 | 100% | 255 |
| snake_abs_exit | 216,547 | +8.27% | 1 | 100% | 260 |
| snake_abs | 213,648 | +6.82% | 1 | 100% | 255 |
| snake_abs_conv | 213,504 | +6.75% | 1 | 100% | 255 |
| benchmark | 212,217 | +6.11% | 0 | - | 237 |
| intramonth | 210,512 | +5.26% | 0 | - | 235 |
| intraweek | 210,325 | +5.16% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,996 | +3.50% | 3 | 33% | 702 |
| random_hold | 205,135 | +2.57% | 8 | 62% | 649 |
| oracle | 204,048 | +2.02% | 0 | - | 233 |
| snake_anaconda | 203,897 | +1.95% | 3 | 33% | 361 |
| snake_viper_tick | 203,463 | +1.73% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| gold | 195,569 | -2.21% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,941 (-4.53%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +4,176 | +2.18% |
| intramonth | +3,497 | +1.69% |
| unified | +3,461 | +1.61% |
| benchmark | +3,458 | +1.66% |
| benchmark_smallcap | +2,377 | +1.21% |
| oracle | +2,256 | +1.12% |
| random_hold | +1,826 | +0.90% |
| snake_abs_exit_conv | +1,770 | +0.82% |
| snake_abs_conv | +1,746 | +0.82% |
| snake_abs | +1,745 | +0.82% |
| snake_abs_exit | +1,646 | +0.77% |
| intraweek | +627 | +0.30% |
| snake_anaconda | +77 | +0.04% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,938 | -0.94% |
| snake_viper_wild | -2,034 | -0.97% |

Average per day so far: snake_abs_exit_conv Rs +671, snake_abs_exit Rs +662, unified Rs +639, snake_abs_conv Rs +540, snake_abs Rs +525, benchmark Rs +436, intramonth Rs +375, intraweek Rs +369, snake_viper_wild Rs +350, snake_viper_tick Rs +204, random_hold Rs +183, snake_anaconda Rs +169, oracle Rs +145, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -158, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.