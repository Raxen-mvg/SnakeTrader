# Paper trading report

Updated 2026-11-12 14:40 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,769 | +10.38% | 0 | - | 236 |
| benchmark | 220,364 | +10.18% | 0 | - | 237 |
| snake_abs_exit_conv | 218,824 | +9.41% | 2 | 50% | 345 |
| snake_abs_exit | 217,770 | +8.88% | 2 | 50% | 345 |
| snake_abs | 215,776 | +7.89% | 1 | 100% | 255 |
| snake_abs_conv | 215,606 | +7.80% | 1 | 100% | 255 |
| intraweek | 214,465 | +7.23% | 30 | 53% | 3,302 |
| oracle | 212,786 | +6.39% | 0 | - | 233 |
| intramonth | 211,518 | +5.76% | 0 | - | 235 |
| random_hold | 207,873 | +3.94% | 10 | 70% | 733 |
| snake_anaconda | 206,535 | +3.27% | 3 | 33% | 374 |
| snake_viper_wild | 205,785 | +2.89% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,802 | +1.40% | 0 | - | 237 |
| snake_viper_tick | 202,267 | +1.13% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,916 | -7.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,911 (-4.04%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,412 | +1.18% |
| snake_abs | +2,151 | +1.01% |
| snake_abs_conv | +2,148 | +1.01% |
| benchmark_smallcap | +1,995 | +0.99% |
| snake_abs_exit_conv | +1,672 | +0.77% |
| snake_abs_exit | +1,608 | +0.74% |
| intraweek | +1,332 | +0.62% |
| benchmark | +1,102 | +0.50% |
| unified | +955 | +0.43% |
| oracle | +783 | +0.37% |
| random_hold | +763 | +0.37% |
| intramonth | +522 | +0.25% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -942 | -0.46% |
| snake_viper_wild | -957 | -0.46% |
| gold | -4,669 | -2.46% |

Average per day so far: snake_abs_exit_conv Rs +649, unified Rs +649, benchmark Rs +636, snake_abs_exit Rs +613, snake_abs_conv Rs +538, snake_abs Rs +526, intraweek Rs +452, oracle Rs +400, intramonth Rs +360, random_hold Rs +246, snake_anaconda Rs +242, snake_viper_wild Rs +241, snake_viper_tick Rs +108, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.