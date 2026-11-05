# Paper trading report

Updated 2026-11-05 11:36 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,295 | +9.15% | 0 | - | 236 |
| snake_abs_exit_conv | 214,699 | +7.35% | 1 | 100% | 255 |
| snake_abs_exit | 214,408 | +7.20% | 1 | 100% | 260 |
| benchmark | 212,806 | +6.40% | 0 | - | 237 |
| snake_abs | 211,577 | +5.79% | 1 | 100% | 255 |
| snake_abs_conv | 211,444 | +5.72% | 1 | 100% | 255 |
| intraweek | 210,737 | +5.37% | 25 | 48% | 2,757 |
| intramonth | 210,087 | +5.04% | 0 | - | 235 |
| random_hold | 207,043 | +3.52% | 8 | 62% | 649 |
| snake_viper_wild | 206,675 | +3.34% | 3 | 33% | 702 |
| oracle | 204,220 | +2.11% | 0 | - | 233 |
| snake_viper_tick | 203,126 | +1.56% | 2 | 0% | 532 |
| snake_anaconda | 203,008 | +1.50% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 194,008 | -3.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,336 (-4.83%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,047 | +1.94% |
| unified | +3,855 | +1.80% |
| random_hold | +3,734 | +1.84% |
| intramonth | +3,071 | +1.48% |
| gold | +2,614 | +1.37% |
| benchmark_smallcap | +2,545 | +1.29% |
| oracle | +2,428 | +1.20% |
| intraweek | +1,039 | +0.50% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -314 | -0.15% |
| snake_abs_exit_conv | -316 | -0.15% |
| snake_abs | -326 | -0.15% |
| snake_abs_exit | -492 | -0.23% |
| snake_anaconda | -812 | -0.40% |
| snake_viper_tick | -2,275 | -1.11% |
| snake_viper_wild | -2,355 | -1.13% |

Average per day so far: unified Rs +653, snake_abs_exit_conv Rs +588, snake_abs_exit Rs +576, snake_abs_conv Rs +458, benchmark Rs +457, snake_abs Rs +445, intraweek Rs +383, intramonth Rs +360, snake_viper_wild Rs +334, random_hold Rs +252, snake_viper_tick Rs +184, oracle Rs +151, snake_anaconda Rs +131, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -214, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.