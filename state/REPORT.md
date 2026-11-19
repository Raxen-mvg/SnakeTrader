# Paper trading report

Updated 2026-11-19 09:39 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,063 | +12.03% | 0 | - | 236 |
| benchmark | 219,744 | +9.87% | 0 | - | 237 |
| intramonth | 213,936 | +6.97% | 0 | - | 235 |
| snake_abs_exit | 213,347 | +6.67% | 2 | 50% | 345 |
| intraweek | 212,227 | +6.11% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,740 | +5.87% | 2 | 50% | 345 |
| oracle | 211,369 | +5.68% | 0 | - | 233 |
| snake_abs | 208,995 | +4.50% | 1 | 100% | 255 |
| snake_abs_conv | 208,877 | +4.44% | 1 | 100% | 255 |
| random_hold | 207,826 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 207,644 | +3.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,095 | +2.05% | 15 | 47% | 2,625 |
| snake_anaconda | 203,902 | +1.95% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,887 | -0.06% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,921 | -12.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,528 (-4.24%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,663 | +0.78% |
| unified | +1,451 | +0.65% |
| random_hold | +894 | +0.43% |
| snake_viper_wild | +605 | +0.29% |
| snake_viper_tick | +592 | +0.29% |
| oracle | +573 | +0.27% |
| benchmark_smallcap | +560 | +0.28% |
| intraweek | +388 | +0.18% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -441 | -0.21% |
| snake_abs_conv | -448 | -0.21% |
| snake_anaconda | -499 | -0.24% |
| benchmark | -551 | -0.25% |
| snake_abs_exit_conv | -643 | -0.30% |
| snake_abs_exit | -684 | -0.32% |
| gold | -2,400 | -1.35% |

Average per day so far: unified Rs +650, benchmark Rs +534, snake_abs_exit Rs +393, intramonth Rs +377, snake_abs_exit_conv Rs +345, intraweek Rs +330, oracle Rs +307, snake_viper_wild Rs +264, snake_abs_conv Rs +261, snake_abs Rs +257, random_hold Rs +212, snake_viper_tick Rs +158, snake_anaconda Rs +122, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -3, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.