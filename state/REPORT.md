# Paper trading report

Updated 2026-11-11 13:59 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,358 | +10.18% | 0 | - | 236 |
| benchmark | 219,806 | +9.90% | 0 | - | 237 |
| snake_abs_exit_conv | 217,202 | +8.60% | 2 | 50% | 345 |
| snake_abs_exit | 216,270 | +8.13% | 2 | 50% | 345 |
| snake_abs | 214,139 | +7.07% | 1 | 100% | 255 |
| snake_abs_conv | 213,975 | +6.99% | 1 | 100% | 255 |
| intraweek | 213,354 | +6.68% | 30 | 53% | 3,302 |
| oracle | 211,823 | +5.91% | 0 | - | 233 |
| intramonth | 211,259 | +5.63% | 0 | - | 235 |
| random_hold | 207,024 | +3.51% | 9 | 67% | 709 |
| snake_viper_wild | 205,390 | +2.69% | 10 | 50% | 1,825 |
| snake_anaconda | 203,977 | +1.99% | 3 | 33% | 374 |
| snake_viper_tick | 201,885 | +0.94% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,829 | +0.41% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,198 (-4.40%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,960 | +4.03% |
| snake_viper_tick | +7,808 | +4.02% |
| snake_abs_exit_conv | +5,294 | +2.50% |
| snake_anaconda | +4,511 | +2.26% |
| snake_abs_conv | +4,498 | +2.15% |
| snake_abs | +4,492 | +2.14% |
| snake_abs_exit | +4,286 | +2.02% |
| benchmark_smallcap | +2,657 | +1.34% |
| random_hold | +2,063 | +1.01% |
| oracle | +1,904 | +0.91% |
| benchmark | +1,714 | +0.79% |
| intramonth | +649 | +0.31% |
| unified | +611 | +0.28% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,188 | -0.55% |
| gold | -2,367 | -1.23% |

Average per day so far: unified Rs +657, benchmark Rs +639, snake_abs_exit_conv Rs +614, snake_abs_exit Rs +581, snake_abs_conv Rs +499, snake_abs Rs +488, intraweek Rs +431, oracle Rs +381, intramonth Rs +363, snake_viper_wild Rs +234, random_hold Rs +227, snake_anaconda Rs +153, snake_viper_tick Rs +94, nifty_calls Rs +59, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.