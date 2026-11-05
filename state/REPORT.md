# Paper trading report

Updated 2026-11-05 10:00 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,969 | +9.48% | 0 | - | 236 |
| snake_abs_exit_conv | 215,891 | +7.95% | 1 | 100% | 255 |
| snake_abs_exit | 215,656 | +7.83% | 1 | 100% | 260 |
| snake_abs | 212,770 | +6.38% | 1 | 100% | 255 |
| benchmark | 212,729 | +6.37% | 0 | - | 237 |
| snake_abs_conv | 212,617 | +6.31% | 1 | 100% | 255 |
| intramonth | 210,757 | +5.38% | 0 | - | 235 |
| intraweek | 209,896 | +4.95% | 25 | 48% | 2,757 |
| random_hold | 206,479 | +3.24% | 8 | 62% | 649 |
| snake_viper_wild | 205,892 | +2.95% | 3 | 33% | 702 |
| oracle | 204,614 | +2.31% | 0 | - | 233 |
| snake_anaconda | 202,994 | +1.50% | 3 | 33% | 374 |
| snake_viper_tick | 202,365 | +1.18% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,697 | -0.15% | 0 | - | 237 |
| gold | 194,978 | -2.51% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,560 (-4.72%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,529 | +2.11% |
| benchmark | +3,970 | +1.90% |
| intramonth | +3,742 | +1.81% |
| gold | +3,584 | +1.87% |
| random_hold | +3,170 | +1.56% |
| benchmark_smallcap | +3,027 | +1.54% |
| oracle | +2,821 | +1.40% |
| snake_abs_exit_conv | +876 | +0.41% |
| snake_abs | +867 | +0.41% |
| snake_abs_conv | +859 | +0.41% |
| snake_abs_exit | +755 | +0.35% |
| intraweek | +198 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -827 | -0.41% |
| snake_viper_tick | -3,036 | -1.48% |
| snake_viper_wild | -3,138 | -1.50% |

Average per day so far: unified Rs +677, snake_abs_exit_conv Rs +636, snake_abs_exit Rs +626, snake_abs_conv Rs +505, snake_abs Rs +491, benchmark Rs +455, intramonth Rs +384, intraweek Rs +353, snake_viper_wild Rs +295, random_hold Rs +231, oracle Rs +165, snake_viper_tick Rs +139, snake_anaconda Rs +130, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -13, gold Rs -179, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.