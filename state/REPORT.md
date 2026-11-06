# Paper trading report

Updated 2026-11-06 12:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,177 | +7.59% | 0 | - | 237 |
| unified | 214,731 | +7.37% | 0 | - | 236 |
| intraweek | 209,548 | +4.77% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,882 | +4.44% | 1 | 100% | 255 |
| snake_abs_exit | 208,700 | +4.35% | 1 | 100% | 260 |
| intramonth | 206,877 | +3.44% | 0 | - | 235 |
| snake_abs | 205,849 | +2.92% | 1 | 100% | 255 |
| snake_abs_conv | 205,675 | +2.84% | 1 | 100% | 255 |
| oracle | 204,859 | +2.43% | 0 | - | 233 |
| random_hold | 203,159 | +1.58% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,148 | -1.93% | 3 | 33% | 374 |
| snake_viper_wild | 195,620 | -2.19% | 3 | 33% | 702 |
| benchmark_smallcap | 194,899 | -2.55% | 0 | - | 237 |
| snake_viper_tick | 192,308 | -3.85% | 2 | 0% | 532 |
| gold | 190,177 | -4.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,015 (-6.49%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,408 | +0.66% |
| oracle | +787 | +0.39% |
| intraweek | +129 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -1,072 | -0.52% |
| random_hold | -1,164 | -0.57% |
| unified | -1,253 | -0.58% |
| benchmark_smallcap | -3,789 | -1.91% |
| gold | -4,044 | -2.08% |
| snake_abs | -5,840 | -2.76% |
| snake_abs_conv | -5,870 | -2.77% |
| snake_abs_exit_conv | -5,922 | -2.76% |
| snake_abs_exit | -5,959 | -2.78% |
| snake_anaconda | -6,331 | -3.13% |
| snake_viper_tick | -8,830 | -4.39% |
| snake_viper_wild | -9,036 | -4.42% |

Average per day so far: benchmark Rs +523, unified Rs +508, snake_abs_exit_conv Rs +342, snake_abs_exit Rs +335, intraweek Rs +329, intramonth Rs +237, snake_abs_conv Rs +218, snake_abs Rs +217, oracle Rs +168, random_hold Rs +109, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -161, benchmark_smallcap Rs -204, snake_viper_wild Rs -209, gold Rs -339, snake_nonews Rs -411, snake_viper_tick Rs -427, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.