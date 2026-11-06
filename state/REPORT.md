# Paper trading report

Updated 2026-11-06 15:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 217,893 | +8.95% | 0 | - | 237 |
| unified | 215,924 | +7.96% | 0 | - | 236 |
| intraweek | 211,398 | +5.70% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,579 | +4.29% | 1 | 100% | 255 |
| snake_abs_exit | 208,465 | +4.23% | 1 | 100% | 260 |
| intramonth | 207,698 | +3.85% | 0 | - | 235 |
| oracle | 205,720 | +2.86% | 0 | - | 233 |
| snake_abs | 205,569 | +2.78% | 1 | 100% | 255 |
| snake_abs_conv | 205,384 | +2.69% | 1 | 100% | 255 |
| random_hold | 204,290 | +2.15% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 197,085 | -1.46% | 0 | - | 237 |
| snake_anaconda | 196,209 | -1.90% | 3 | 33% | 374 |
| snake_viper_wild | 196,188 | -1.91% | 4 | 25% | 842 |
| snake_viper_tick | 192,860 | -3.57% | 3 | 0% | 672 |
| gold | 191,180 | -4.41% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,638 (-6.18%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,123 | +1.93% |
| intraweek | +1,980 | +0.94% |
| oracle | +1,648 | +0.81% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -34 | -0.02% |
| unified | -59 | -0.03% |
| intramonth | -251 | -0.12% |
| benchmark_smallcap | -1,603 | -0.81% |
| gold | -3,041 | -1.57% |
| snake_abs | -6,120 | -2.89% |
| snake_abs_conv | -6,161 | -2.91% |
| snake_abs_exit | -6,194 | -2.88% |
| snake_abs_exit_conv | -6,225 | -2.90% |
| snake_anaconda | -6,271 | -3.10% |
| snake_viper_tick | -8,278 | -4.12% |
| snake_viper_wild | -8,468 | -4.14% |

Average per day so far: benchmark Rs +617, unified Rs +549, intraweek Rs +393, snake_abs_exit_conv Rs +330, snake_abs_exit Rs +326, intramonth Rs +265, snake_abs_conv Rs +207, snake_abs Rs +206, oracle Rs +197, random_hold Rs +148, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -117, snake_anaconda Rs -158, snake_viper_wild Rs -182, gold Rs -304, snake_viper_tick Rs -397, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.