# Paper trading report

Updated 2026-11-20 09:17 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,709 | +12.86% | 0 | - | 236 |
| benchmark | 221,825 | +10.91% | 0 | - | 237 |
| intramonth | 214,901 | +7.45% | 0 | - | 235 |
| intraweek | 213,672 | +6.84% | 35 | 54% | 3,851 |
| oracle | 212,588 | +6.29% | 0 | - | 233 |
| snake_abs_exit | 212,051 | +6.03% | 2 | 50% | 345 |
| snake_abs_exit_conv | 209,970 | +4.99% | 2 | 50% | 345 |
| random_hold | 209,274 | +4.64% | 10 | 70% | 733 |
| snake_abs | 208,071 | +4.04% | 1 | 100% | 255 |
| snake_abs_conv | 207,945 | +3.97% | 1 | 100% | 255 |
| snake_viper_wild | 206,716 | +3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,187 | +1.59% | 15 | 47% | 2,625 |
| snake_anaconda | 202,410 | +1.21% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,750 | -16.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,138 (-3.93%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,094 | +0.49% |
| intramonth | +893 | +0.42% |
| random_hold | +821 | +0.39% |
| intraweek | +783 | +0.37% |
| oracle | +499 | +0.24% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -551 | -0.25% |
| snake_viper_tick | -790 | -0.39% |
| snake_viper_wild | -806 | -0.39% |
| snake_abs | -909 | -0.43% |
| snake_abs_conv | -915 | -0.44% |
| snake_anaconda | -1,054 | -0.52% |
| snake_abs_exit_conv | -1,094 | -0.52% |
| benchmark_smallcap | -1,244 | -0.62% |
| snake_abs_exit | -1,300 | -0.61% |
| gold | -8,023 | -4.59% |

Average per day so far: unified Rs +677, benchmark Rs +574, intramonth Rs +392, intraweek Rs +360, snake_abs_exit Rs +344, oracle Rs +331, snake_abs_exit_conv Rs +285, random_hold Rs +244, snake_abs_conv Rs +227, snake_abs Rs +224, snake_viper_wild Rs +224, snake_viper_tick Rs +118, snake_anaconda Rs +73, nifty_calls Rs +48, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -875

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.