# Paper trading report

Updated 2026-11-05 13:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,409 | +8.21% | 0 | - | 236 |
| snake_abs_exit_conv | 214,458 | +7.23% | 1 | 100% | 255 |
| snake_abs_exit | 214,209 | +7.10% | 1 | 100% | 260 |
| benchmark | 213,946 | +6.97% | 0 | - | 237 |
| snake_abs | 211,330 | +5.67% | 1 | 100% | 255 |
| intraweek | 211,239 | +5.62% | 25 | 48% | 2,757 |
| snake_abs_conv | 211,199 | +5.60% | 1 | 100% | 255 |
| intramonth | 208,394 | +4.20% | 0 | - | 235 |
| snake_viper_wild | 206,740 | +3.37% | 3 | 33% | 702 |
| random_hold | 205,169 | +2.58% | 8 | 62% | 649 |
| oracle | 203,647 | +1.82% | 0 | - | 233 |
| snake_viper_tick | 203,188 | +1.59% | 2 | 0% | 532 |
| snake_anaconda | 202,588 | +1.29% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| gold | 194,057 | -2.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,019 (-4.99%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,187 | +2.48% |
| gold | +2,663 | +1.39% |
| benchmark_smallcap | +2,433 | +1.24% |
| unified | +1,970 | +0.92% |
| random_hold | +1,860 | +0.92% |
| oracle | +1,855 | +0.92% |
| intraweek | +1,541 | +0.73% |
| intramonth | +1,379 | +0.67% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -557 | -0.26% |
| snake_abs_conv | -559 | -0.26% |
| snake_abs | -573 | -0.27% |
| snake_abs_exit | -692 | -0.32% |
| snake_anaconda | -1,232 | -0.60% |
| snake_viper_tick | -2,213 | -1.08% |
| snake_viper_wild | -2,289 | -1.09% |

Average per day so far: unified Rs +586, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +568, benchmark Rs +498, snake_abs_conv Rs +448, snake_abs Rs +436, intraweek Rs +401, snake_viper_wild Rs +337, intramonth Rs +300, snake_viper_tick Rs +188, random_hold Rs +185, oracle Rs +130, snake_anaconda Rs +113, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -37, gold Rs -212, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.