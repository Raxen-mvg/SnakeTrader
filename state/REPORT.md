# Paper trading report

Updated 2026-11-27 10:17 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,581 | +12.79% | 0 | - | 237 |
| unified | 223,005 | +11.50% | 0 | - | 236 |
| oracle | 212,512 | +6.26% | 0 | - | 233 |
| intramonth | 210,565 | +5.28% | 0 | - | 235 |
| random_hold | 210,169 | +5.08% | 13 | 69% | 1,037 |
| intraweek | 208,413 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,787 | +2.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,735 | +2.37% | 2 | 50% | 345 |
| benchmark_smallcap | 202,219 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,761 | +0.88% | 1 | 100% | 255 |
| snake_abs_conv | 201,590 | +0.80% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,167 | -2.42% | 3 | 33% | 374 |
| snake_viper_wild | 193,465 | -3.27% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,175 | -4.91% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,739 | -15.63% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,865 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,709 | +2.34% |
| snake_abs_exit_conv | +4,338 | +2.17% |
| snake_abs_conv | +3,224 | +1.62% |
| snake_abs | +3,209 | +1.62% |
| snake_anaconda | +2,871 | +1.49% |
| gold | +2,745 | +1.65% |
| random_hold | +1,575 | +0.76% |
| benchmark_smallcap | +1,379 | +0.69% |
| intraweek | +1,364 | +0.66% |
| snake_viper_wild | +1,259 | +0.66% |
| snake_viper_tick | +1,234 | +0.65% |
| oracle | +276 | +0.13% |
| intramonth | +31 | +0.01% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -73 | -0.03% |
| benchmark | -405 | -0.18% |

Average per day so far: benchmark Rs +609, unified Rs +548, oracle Rs +298, intramonth Rs +252, random_hold Rs +242, intraweek Rs +200, snake_abs_exit Rs +148, snake_abs_exit_conv Rs +121, benchmark_smallcap Rs +58, snake_abs Rs +44, nifty_calls Rs +44, snake_abs_conv Rs +41, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -131, snake_viper_wild Rs -192, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -317, gold Rs -744

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.