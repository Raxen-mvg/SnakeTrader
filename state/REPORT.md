# Paper trading report

Updated 2026-11-11 10:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,144 | +10.57% | 0 | - | 237 |
| unified | 220,607 | +10.30% | 0 | - | 236 |
| snake_abs_exit_conv | 216,620 | +8.31% | 2 | 50% | 345 |
| intraweek | 215,304 | +7.65% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,738 | +7.37% | 2 | 50% | 345 |
| snake_abs | 213,157 | +6.58% | 1 | 100% | 255 |
| snake_abs_conv | 212,997 | +6.50% | 1 | 100% | 255 |
| oracle | 211,737 | +5.87% | 0 | - | 233 |
| intramonth | 211,200 | +5.60% | 0 | - | 235 |
| random_hold | 206,401 | +3.20% | 9 | 67% | 709 |
| snake_anaconda | 202,832 | +1.42% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_viper_wild | 200,420 | +0.21% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,018 | -1.49% | 9 | 44% | 1,639 |
| gold | 189,224 | -5.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,460 (-4.27%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,711 | +2.22% |
| snake_abs_conv | +3,520 | +1.68% |
| snake_abs | +3,511 | +1.68% |
| snake_anaconda | +3,365 | +1.69% |
| benchmark_smallcap | +3,341 | +1.69% |
| benchmark | +3,052 | +1.40% |
| snake_viper_wild | +2,990 | +1.51% |
| snake_viper_tick | +2,941 | +1.51% |
| snake_abs_exit | +2,754 | +1.30% |
| oracle | +1,819 | +0.87% |
| random_hold | +1,440 | +0.70% |
| unified | +860 | +0.39% |
| intraweek | +762 | +0.35% |
| intramonth | +591 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,910 | -1.51% |

Average per day so far: benchmark Rs +682, unified Rs +665, snake_abs_exit_conv Rs +594, snake_abs_exit Rs +526, intraweek Rs +494, snake_abs_conv Rs +464, snake_abs Rs +454, oracle Rs +379, intramonth Rs +361, random_hold Rs +206, snake_anaconda Rs +109, nifty_calls Rs +59, benchmark_smallcap Rs +56, snake_viper_wild Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -149, gold Rs -348, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.