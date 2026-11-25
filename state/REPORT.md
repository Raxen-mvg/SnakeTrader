# Paper trading report

Updated 2026-11-25 09:59 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,286 | +12.64% | 0 | - | 236 |
| benchmark | 224,694 | +12.35% | 0 | - | 237 |
| intramonth | 212,917 | +6.46% | 0 | - | 235 |
| oracle | 212,913 | +6.46% | 0 | - | 233 |
| random_hold | 209,634 | +4.82% | 12 | 75% | 1,009 |
| intraweek | 209,597 | +4.80% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,027 | +1.01% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,369 | +0.69% | 2 | 50% | 345 |
| snake_abs | 200,734 | +0.37% | 1 | 100% | 255 |
| snake_abs_conv | 200,540 | +0.27% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_viper_wild | 198,595 | -0.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,216 | -2.39% | 15 | 47% | 2,625 |
| snake_anaconda | 193,735 | -3.13% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,566 | -17.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,618 (-5.19%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,221 | +1.45% |
| random_hold | +1,208 | +0.58% |
| unified | +1,001 | +0.45% |
| oracle | +571 | +0.27% |
| benchmark_smallcap | +527 | +0.27% |
| intramonth | +166 | +0.08% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -2,022 | -0.95% |
| snake_viper_tick | -2,477 | -1.25% |
| snake_viper_wild | -2,530 | -1.26% |
| gold | -3,863 | -2.28% |
| snake_abs | -4,727 | -2.30% |
| snake_abs_conv | -4,762 | -2.32% |
| snake_anaconda | -4,969 | -2.50% |
| snake_abs_exit | -5,468 | -2.63% |
| snake_abs_exit_conv | -5,676 | -2.74% |

Average per day so far: unified Rs +632, benchmark Rs +617, intramonth Rs +323, oracle Rs +323, random_hold Rs +241, intraweek Rs +240, snake_abs_exit Rs +55, nifty_calls Rs +46, snake_abs_exit_conv Rs +37, snake_abs Rs +19, snake_abs_conv Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -44, snake_viper_tick Rs -165, snake_anaconda Rs -179, snake_nonews Rs -292, snake Rs -311, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.