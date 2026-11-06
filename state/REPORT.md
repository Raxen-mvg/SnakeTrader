# Paper trading report

Updated 2026-11-06 12:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,659 | +7.33% | 0 | - | 236 |
| benchmark | 214,336 | +7.17% | 0 | - | 237 |
| intraweek | 210,710 | +5.36% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,765 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,576 | +4.29% | 1 | 100% | 260 |
| intramonth | 206,932 | +3.47% | 0 | - | 235 |
| snake_abs | 205,732 | +2.87% | 1 | 100% | 255 |
| snake_abs_conv | 205,558 | +2.78% | 1 | 100% | 255 |
| oracle | 204,589 | +2.29% | 0 | - | 233 |
| random_hold | 203,228 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,014 | -1.99% | 3 | 33% | 374 |
| snake_viper_wild | 195,127 | -2.44% | 3 | 33% | 702 |
| benchmark_smallcap | 194,507 | -2.75% | 0 | - | 237 |
| snake_viper_tick | 191,823 | -4.09% | 2 | 0% | 532 |
| gold | 190,128 | -4.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,077 (-6.46%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,291 | +0.62% |
| benchmark | +566 | +0.27% |
| oracle | +517 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -1,017 | -0.49% |
| random_hold | -1,095 | -0.54% |
| unified | -1,325 | -0.61% |
| gold | -4,094 | -2.11% |
| benchmark_smallcap | -4,181 | -2.10% |
| snake_abs | -5,956 | -2.81% |
| snake_abs_conv | -5,987 | -2.83% |
| snake_abs_exit_conv | -6,038 | -2.81% |
| snake_abs_exit | -6,083 | -2.83% |
| snake_anaconda | -6,466 | -3.19% |
| snake_viper_tick | -9,315 | -4.63% |
| snake_viper_wild | -9,529 | -4.66% |

Average per day so far: unified Rs +505, benchmark Rs +494, intraweek Rs +369, snake_abs_exit_conv Rs +337, snake_abs_exit Rs +330, intramonth Rs +239, snake_abs_conv Rs +214, snake_abs Rs +212, oracle Rs +158, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -166, benchmark_smallcap Rs -220, snake_viper_wild Rs -232, gold Rs -340, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -454

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.