# Paper trading report

Updated 2026-11-06 10:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,087 | +7.54% | 0 | - | 236 |
| benchmark | 214,374 | +7.19% | 0 | - | 237 |
| intraweek | 210,748 | +5.37% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,428 | +4.71% | 1 | 100% | 255 |
| snake_abs_exit | 209,215 | +4.61% | 1 | 100% | 260 |
| intramonth | 207,049 | +3.52% | 0 | - | 235 |
| snake_abs | 206,385 | +3.19% | 1 | 100% | 255 |
| snake_abs_conv | 206,215 | +3.11% | 1 | 100% | 255 |
| oracle | 205,024 | +2.51% | 0 | - | 233 |
| random_hold | 203,418 | +1.71% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,681 | -1.16% | 3 | 33% | 702 |
| snake_anaconda | 196,762 | -1.62% | 3 | 33% | 374 |
| benchmark_smallcap | 194,630 | -2.69% | 0 | - | 237 |
| snake_viper_tick | 194,332 | -2.83% | 2 | 0% | 532 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,489 (-6.26%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,329 | +0.64% |
| oracle | +952 | +0.47% |
| benchmark | +604 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -896 | -0.41% |
| intramonth | -899 | -0.43% |
| random_hold | -905 | -0.44% |
| benchmark_smallcap | -4,058 | -2.04% |
| gold | -4,324 | -2.23% |
| snake_abs | -5,304 | -2.50% |
| snake_abs_conv | -5,329 | -2.52% |
| snake_abs_exit_conv | -5,376 | -2.50% |
| snake_abs_exit | -5,444 | -2.54% |
| snake_anaconda | -5,717 | -2.82% |
| snake_viper_tick | -6,806 | -3.38% |
| snake_viper_wild | -6,975 | -3.41% |

Average per day so far: unified Rs +520, benchmark Rs +496, intraweek Rs +371, snake_abs_exit_conv Rs +363, snake_abs_exit Rs +354, intramonth Rs +243, snake_abs_conv Rs +239, snake_abs Rs +236, oracle Rs +173, random_hold Rs +118, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -110, snake_anaconda Rs -135, benchmark_smallcap Rs -215, snake_viper_tick Rs -315, gold Rs -348, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.