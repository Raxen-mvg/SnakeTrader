# Paper trading report

Updated 2026-11-25 13:43 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,626 | +12.31% | 0 | - | 236 |
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| oracle | 212,459 | +6.23% | 0 | - | 233 |
| intramonth | 212,260 | +6.13% | 0 | - | 235 |
| random_hold | 209,492 | +4.75% | 12 | 75% | 1,009 |
| intraweek | 207,451 | +3.73% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,344 | +0.67% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,031 | +0.52% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,534 | -0.23% | 1 | 100% | 255 |
| snake_abs_conv | 199,334 | -0.33% | 1 | 100% | 255 |
| benchmark_smallcap | 198,822 | -0.59% | 0 | - | 237 |
| snake_viper_wild | 197,006 | -1.50% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,650 | -3.17% | 15 | 47% | 2,625 |
| snake_anaconda | 193,055 | -3.47% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,596 | -17.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,921 (-5.54%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,876 | +1.30% |
| random_hold | +1,066 | +0.51% |
| unified | +340 | +0.15% |
| oracle | +117 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -157 | -0.08% |
| intramonth | -492 | -0.23% |
| snake_viper_tick | -4,042 | -2.04% |
| snake_viper_wild | -4,119 | -2.05% |
| intraweek | -4,168 | -1.97% |
| gold | -4,833 | -2.85% |
| snake_anaconda | -5,648 | -2.84% |
| snake_abs | -5,927 | -2.88% |
| snake_abs_conv | -5,968 | -2.91% |
| snake_abs_exit_conv | -6,015 | -2.90% |
| snake_abs_exit | -6,151 | -2.96% |

Average per day so far: unified Rs +616, benchmark Rs +609, oracle Rs +311, intramonth Rs +306, random_hold Rs +237, intraweek Rs +186, nifty_calls Rs +46, snake_abs_exit Rs +36, snake_abs_exit_conv Rs +28, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -12, snake_abs_conv Rs -18, benchmark_smallcap Rs -33, snake_viper_wild Rs -94, snake_anaconda Rs -198, snake_viper_tick Rs -219, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.