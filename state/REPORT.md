# Paper trading report

Updated 2026-11-06 12:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,246 | +7.62% | 0 | - | 237 |
| unified | 214,527 | +7.26% | 0 | - | 236 |
| intraweek | 209,418 | +4.71% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,008 | +4.50% | 1 | 100% | 255 |
| snake_abs_exit | 208,831 | +4.42% | 1 | 100% | 260 |
| intramonth | 206,745 | +3.37% | 0 | - | 235 |
| snake_abs | 205,977 | +2.99% | 1 | 100% | 255 |
| snake_abs_conv | 205,803 | +2.90% | 1 | 100% | 255 |
| oracle | 205,023 | +2.51% | 0 | - | 233 |
| random_hold | 203,281 | +1.64% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,437 | -1.78% | 3 | 33% | 374 |
| snake_viper_wild | 195,831 | -2.08% | 3 | 33% | 702 |
| benchmark_smallcap | 194,798 | -2.60% | 0 | - | 237 |
| snake_viper_tick | 192,517 | -3.74% | 2 | 0% | 532 |
| gold | 190,062 | -4.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,023 (-6.49%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,476 | +0.69% |
| oracle | +951 | +0.47% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -0 | -0.00% |
| random_hold | -1,042 | -0.51% |
| intramonth | -1,203 | -0.58% |
| unified | -1,457 | -0.67% |
| benchmark_smallcap | -3,890 | -1.96% |
| gold | -4,159 | -2.14% |
| snake_abs | -5,712 | -2.70% |
| snake_abs_conv | -5,741 | -2.71% |
| snake_abs_exit_conv | -5,796 | -2.70% |
| snake_abs_exit | -5,828 | -2.71% |
| snake_anaconda | -6,043 | -2.98% |
| snake_viper_tick | -8,621 | -4.29% |
| snake_viper_wild | -8,825 | -4.31% |

Average per day so far: benchmark Rs +526, unified Rs +501, snake_abs_exit_conv Rs +346, snake_abs_exit Rs +340, intraweek Rs +325, intramonth Rs +233, snake_abs_conv Rs +223, snake_abs Rs +221, oracle Rs +173, random_hold Rs +113, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -148, snake_viper_wild Rs -199, benchmark_smallcap Rs -208, gold Rs -343, snake_nonews Rs -411, snake_viper_tick Rs -416, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.