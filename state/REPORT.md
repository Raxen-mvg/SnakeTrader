# Paper trading report

Updated 2026-11-11 10:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,183 | +10.59% | 0 | - | 237 |
| unified | 220,831 | +10.41% | 0 | - | 236 |
| snake_abs_exit_conv | 216,031 | +8.02% | 2 | 50% | 345 |
| intraweek | 215,030 | +7.51% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,492 | +7.25% | 2 | 50% | 345 |
| snake_abs | 212,760 | +6.38% | 1 | 100% | 255 |
| snake_abs_conv | 212,603 | +6.30% | 1 | 100% | 255 |
| oracle | 212,106 | +6.05% | 0 | - | 233 |
| intramonth | 211,556 | +5.78% | 0 | - | 235 |
| random_hold | 206,991 | +3.50% | 9 | 67% | 709 |
| snake_anaconda | 202,520 | +1.26% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,771 | +0.89% | 0 | - | 237 |
| snake_viper_wild | 200,360 | +0.18% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,959 | -1.52% | 9 | 44% | 1,639 |
| gold | 189,667 | -5.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,547 (-4.23%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,122 | +1.95% |
| benchmark_smallcap | +3,598 | +1.82% |
| snake_abs_conv | +3,125 | +1.49% |
| snake_abs | +3,113 | +1.49% |
| benchmark | +3,091 | +1.42% |
| snake_anaconda | +3,054 | +1.53% |
| snake_viper_wild | +2,930 | +1.48% |
| snake_viper_tick | +2,882 | +1.49% |
| snake_abs_exit | +2,508 | +1.18% |
| oracle | +2,188 | +1.04% |
| random_hold | +2,031 | +0.99% |
| unified | +1,084 | +0.49% |
| intramonth | +947 | +0.45% |
| intraweek | +489 | +0.23% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,466 | -1.28% |

Average per day so far: benchmark Rs +683, unified Rs +672, snake_abs_exit_conv Rs +573, snake_abs_exit Rs +518, intraweek Rs +485, snake_abs_conv Rs +450, snake_abs Rs +440, oracle Rs +391, intramonth Rs +373, random_hold Rs +226, snake_anaconda Rs +97, benchmark_smallcap Rs +66, nifty_calls Rs +59, snake_viper_wild Rs +16, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -152, gold Rs -333, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.