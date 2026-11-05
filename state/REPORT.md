# Paper trading report

Updated 2026-11-05 12:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,312 | +8.66% | 0 | - | 236 |
| snake_abs_exit_conv | 213,540 | +6.77% | 1 | 100% | 255 |
| snake_abs_exit | 213,248 | +6.62% | 1 | 100% | 260 |
| benchmark | 212,982 | +6.49% | 0 | - | 237 |
| intraweek | 210,809 | +5.41% | 25 | 48% | 2,757 |
| snake_abs | 210,432 | +5.22% | 1 | 100% | 255 |
| snake_abs_conv | 210,292 | +5.15% | 1 | 100% | 255 |
| intramonth | 209,383 | +4.69% | 0 | - | 235 |
| snake_viper_wild | 206,484 | +3.24% | 3 | 33% | 702 |
| random_hold | 205,835 | +2.92% | 8 | 62% | 649 |
| oracle | 204,003 | +2.00% | 0 | - | 233 |
| snake_viper_tick | 202,932 | +1.47% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,612 | +0.81% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,069 | -0.47% | 0 | - | 237 |
| gold | 194,172 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,796 (-5.10%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,223 | +2.02% |
| unified | +2,872 | +1.34% |
| gold | +2,778 | +1.45% |
| random_hold | +2,526 | +1.24% |
| benchmark_smallcap | +2,399 | +1.22% |
| intramonth | +2,367 | +1.14% |
| oracle | +2,211 | +1.10% |
| intraweek | +1,111 | +0.53% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,467 | -0.69% |
| snake_abs | -1,471 | -0.69% |
| snake_abs_exit_conv | -1,475 | -0.69% |
| snake_abs_exit | -1,652 | -0.77% |
| snake_anaconda | -2,208 | -1.08% |
| snake_viper_tick | -2,468 | -1.20% |
| snake_viper_wild | -2,546 | -1.22% |

Average per day so far: unified Rs +618, snake_abs_exit_conv Rs +542, snake_abs_exit Rs +530, benchmark Rs +464, snake_abs_conv Rs +412, snake_abs Rs +401, intraweek Rs +386, intramonth Rs +335, snake_viper_wild Rs +324, random_hold Rs +208, snake_viper_tick Rs +172, oracle Rs +143, snake_anaconda Rs +70, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -39, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.