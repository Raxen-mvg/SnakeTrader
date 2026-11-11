# Paper trading report

Updated 2026-11-11 14:17 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,299 | +10.15% | 0 | - | 236 |
| benchmark | 220,004 | +10.00% | 0 | - | 237 |
| snake_abs_exit_conv | 216,850 | +8.43% | 2 | 50% | 345 |
| snake_abs_exit | 216,042 | +8.02% | 2 | 50% | 345 |
| snake_abs | 213,896 | +6.95% | 1 | 100% | 255 |
| snake_abs_conv | 213,731 | +6.87% | 1 | 100% | 255 |
| intraweek | 213,035 | +6.52% | 30 | 53% | 3,302 |
| oracle | 211,772 | +5.89% | 0 | - | 233 |
| intramonth | 211,300 | +5.65% | 0 | - | 235 |
| random_hold | 207,049 | +3.52% | 9 | 67% | 709 |
| snake_viper_wild | 205,054 | +2.53% | 10 | 50% | 1,825 |
| snake_anaconda | 203,879 | +1.94% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,555 | +0.78% | 9 | 44% | 1,639 |
| benchmark_smallcap | 200,874 | +0.44% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,766 | -5.12% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,098 (-4.45%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,624 | +3.86% |
| snake_viper_tick | +7,479 | +3.85% |
| snake_abs_exit_conv | +4,942 | +2.33% |
| snake_anaconda | +4,413 | +2.21% |
| snake_abs_conv | +4,254 | +2.03% |
| snake_abs | +4,249 | +2.03% |
| snake_abs_exit | +4,058 | +1.91% |
| benchmark_smallcap | +2,702 | +1.36% |
| random_hold | +2,088 | +1.02% |
| benchmark | +1,912 | +0.88% |
| oracle | +1,853 | +0.88% |
| intramonth | +691 | +0.33% |
| unified | +552 | +0.25% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -1,507 | -0.70% |
| gold | -2,367 | -1.23% |

Average per day so far: unified Rs +655, benchmark Rs +645, snake_abs_exit_conv Rs +602, snake_abs_exit Rs +573, snake_abs_conv Rs +490, snake_abs Rs +479, intraweek Rs +420, oracle Rs +380, intramonth Rs +365, random_hold Rs +227, snake_viper_wild Rs +220, snake_anaconda Rs +149, snake_viper_tick Rs +78, nifty_calls Rs +59, benchmark_smallcap Rs +32, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -330, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.