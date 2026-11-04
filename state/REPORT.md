# Paper trading report

Updated 2026-11-04 12:22 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,739 | +6.87% | 0 | - | 236 |
| snake_abs_exit_conv | 210,764 | +5.38% | 1 | 100% | 255 |
| snake_abs_exit | 210,607 | +5.30% | 1 | 100% | 260 |
| intraweek | 208,422 | +4.21% | 25 | 48% | 2,757 |
| snake_abs | 207,673 | +3.84% | 1 | 100% | 255 |
| snake_abs_conv | 207,514 | +3.76% | 1 | 100% | 255 |
| benchmark | 207,260 | +3.63% | 0 | - | 237 |
| snake_viper_wild | 207,157 | +3.58% | 3 | 33% | 702 |
| intramonth | 206,070 | +3.04% | 0 | - | 235 |
| snake_viper_tick | 203,548 | +1.77% | 2 | 0% | 532 |
| random_hold | 202,757 | +1.38% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,089 | +0.55% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,160 | -0.42% | 3 | 33% | 361 |
| benchmark_smallcap | 194,619 | -2.69% | 0 | - | 237 |
| gold | 190,736 | -4.63% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,122 (-5.44%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +6,593 | +3.23% |
| snake_abs_exit_conv | +6,425 | +3.15% |
| snake_abs_conv | +6,373 | +3.17% |
| snake_abs | +6,364 | +3.16% |
| gold | +5,458 | +2.95% |
| snake_anaconda | +5,336 | +2.75% |
| intraweek | +3,336 | +1.63% |
| random_hold | +2,289 | +1.14% |
| intramonth | +2,099 | +1.03% |
| unified | +1,738 | +0.82% |
| benchmark_smallcap | +1,682 | +0.87% |
| oracle | +1,100 | +0.55% |
| benchmark | +558 | +0.27% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,618 | -1.75% |
| snake_viper_wild | -3,735 | -1.77% |

Average per day so far: unified Rs +509, snake_abs_exit_conv Rs +448, snake_abs_exit Rs +442, snake_viper_wild Rs +377, snake_abs_conv Rs +313, intraweek Rs +312, snake_abs Rs +307, benchmark Rs +269, intramonth Rs +225, snake_viper_tick Rs +222, random_hold Rs +102, nifty_calls Rs +68, oracle Rs +40, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -38, benchmark_smallcap Rs -234, gold Rs -343, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.