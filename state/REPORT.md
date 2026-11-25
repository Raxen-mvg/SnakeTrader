# Paper trading report

Updated 2026-11-25 09:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,485 | +12.74% | 0 | - | 236 |
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| intramonth | 213,017 | +6.51% | 0 | - | 235 |
| oracle | 212,736 | +6.37% | 0 | - | 233 |
| intraweek | 212,251 | +6.13% | 40 | 55% | 4,400 |
| random_hold | 209,354 | +4.68% | 12 | 75% | 1,009 |
| snake_abs_exit | 204,530 | +2.27% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,899 | +1.95% | 2 | 50% | 345 |
| snake_abs | 203,367 | +1.68% | 1 | 100% | 255 |
| snake_abs_conv | 203,187 | +1.59% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,164 | +0.08% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,786 | -0.11% | 0 | - | 237 |
| snake_viper_tick | 196,753 | -1.62% | 15 | 47% | 2,625 |
| snake_anaconda | 196,169 | -1.92% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,912 | -17.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,343 (-4.83%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,876 | +1.30% |
| unified | +1,200 | +0.54% |
| random_hold | +928 | +0.45% |
| benchmark_smallcap | +807 | +0.41% |
| intraweek | +632 | +0.30% |
| oracle | +394 | +0.19% |
| intramonth | +265 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -940 | -0.47% |
| snake_viper_wild | -960 | -0.48% |
| snake_abs | -2,094 | -1.02% |
| snake_abs_conv | -2,115 | -1.03% |
| snake_anaconda | -2,535 | -1.28% |
| snake_abs_exit | -2,965 | -1.43% |
| snake_abs_exit_conv | -3,147 | -1.52% |
| gold | -3,518 | -2.08% |

Average per day so far: unified Rs +637, benchmark Rs +609, intramonth Rs +325, oracle Rs +318, intraweek Rs +306, random_hold Rs +234, snake_abs_exit Rs +122, snake_abs_exit_conv Rs +105, snake_abs Rs +89, snake_abs_conv Rs +86, nifty_calls Rs +46, snake_viper_wild Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -109, snake_viper_tick Rs -112, snake_nonews Rs -292, snake Rs -311, gold Rs -852

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.