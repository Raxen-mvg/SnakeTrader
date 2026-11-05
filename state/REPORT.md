# Paper trading report

Updated 2026-11-05 12:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,153 | +8.58% | 0 | - | 236 |
| snake_abs_exit_conv | 213,467 | +6.73% | 1 | 100% | 255 |
| snake_abs_exit | 213,178 | +6.59% | 1 | 100% | 260 |
| benchmark | 213,020 | +6.51% | 0 | - | 237 |
| intraweek | 210,871 | +5.43% | 25 | 48% | 2,757 |
| snake_abs | 210,360 | +5.18% | 1 | 100% | 255 |
| snake_abs_conv | 210,220 | +5.11% | 1 | 100% | 255 |
| intramonth | 209,168 | +4.58% | 0 | - | 235 |
| snake_viper_wild | 206,442 | +3.22% | 3 | 33% | 702 |
| random_hold | 205,698 | +2.85% | 8 | 62% | 649 |
| oracle | 203,854 | +1.93% | 0 | - | 233 |
| snake_viper_tick | 202,891 | +1.45% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,538 | +0.77% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,968 | -0.52% | 0 | - | 237 |
| gold | 194,172 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,744 (-5.13%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,261 | +2.04% |
| gold | +2,778 | +1.45% |
| unified | +2,713 | +1.26% |
| random_hold | +2,389 | +1.18% |
| benchmark_smallcap | +2,298 | +1.17% |
| intramonth | +2,153 | +1.04% |
| oracle | +2,062 | +1.02% |
| intraweek | +1,173 | +0.56% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,539 | -0.73% |
| snake_abs | -1,543 | -0.73% |
| snake_abs_exit_conv | -1,548 | -0.72% |
| snake_abs_exit | -1,722 | -0.80% |
| snake_anaconda | -2,282 | -1.12% |
| snake_viper_tick | -2,509 | -1.22% |
| snake_viper_wild | -2,588 | -1.24% |

Average per day so far: unified Rs +613, snake_abs_exit_conv Rs +539, snake_abs_exit Rs +527, benchmark Rs +465, snake_abs_conv Rs +409, snake_abs Rs +398, intraweek Rs +388, intramonth Rs +327, snake_viper_wild Rs +322, random_hold Rs +203, snake_viper_tick Rs +170, oracle Rs +138, snake_anaconda Rs +67, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.