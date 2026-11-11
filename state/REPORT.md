# Paper trading report

Updated 2026-11-11 15:18 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,883 | +9.94% | 0 | - | 236 |
| benchmark | 219,239 | +9.62% | 0 | - | 237 |
| snake_abs_exit_conv | 217,104 | +8.55% | 2 | 50% | 345 |
| snake_abs_exit | 216,153 | +8.08% | 2 | 50% | 345 |
| snake_abs | 213,245 | +6.62% | 1 | 100% | 255 |
| intraweek | 213,154 | +6.58% | 30 | 53% | 3,302 |
| snake_abs_conv | 213,084 | +6.54% | 1 | 100% | 255 |
| oracle | 212,195 | +6.10% | 0 | - | 233 |
| intramonth | 211,196 | +5.60% | 0 | - | 235 |
| random_hold | 206,979 | +3.49% | 9 | 67% | 709 |
| snake_viper_wild | 206,646 | +3.32% | 10 | 50% | 1,825 |
| snake_anaconda | 204,013 | +2.01% | 3 | 33% | 374 |
| snake_viper_tick | 203,115 | +1.56% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,536 | -5.23% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,058 (-4.47%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +9,216 | +4.67% |
| snake_viper_tick | +9,039 | +4.66% |
| snake_abs_exit_conv | +5,195 | +2.45% |
| snake_anaconda | +4,546 | +2.28% |
| snake_abs_exit | +4,169 | +1.97% |
| snake_abs_conv | +3,606 | +1.72% |
| snake_abs | +3,598 | +1.72% |
| benchmark_smallcap | +2,489 | +1.26% |
| oracle | +2,276 | +1.08% |
| random_hold | +2,018 | +0.98% |
| benchmark | +1,147 | +0.53% |
| intramonth | +587 | +0.28% |
| unified | +136 | +0.06% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,388 | -0.65% |
| gold | -2,598 | -1.35% |

Average per day so far: unified Rs +641, benchmark Rs +621, snake_abs_exit_conv Rs +611, snake_abs_exit Rs +577, snake_abs_conv Rs +467, snake_abs Rs +457, intraweek Rs +424, oracle Rs +393, intramonth Rs +361, snake_viper_wild Rs +289, random_hold Rs +225, snake_viper_tick Rs +156, snake_anaconda Rs +154, nifty_calls Rs +59, benchmark_smallcap Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -338, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.