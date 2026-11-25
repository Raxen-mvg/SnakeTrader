# Paper trading report

Updated 2026-11-25 12:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 225,382 | +12.69% | 0 | - | 236 |
| intramonth | 213,055 | +6.53% | 0 | - | 235 |
| oracle | 212,778 | +6.39% | 0 | - | 233 |
| random_hold | 210,019 | +5.01% | 12 | 75% | 1,009 |
| intraweek | 207,965 | +3.98% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,417 | +1.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,829 | +0.92% | 2 | 50% | 345 |
| snake_abs | 200,982 | +0.49% | 1 | 100% | 255 |
| snake_abs_conv | 200,797 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_viper_wild | 196,890 | -1.55% | 16 | 50% | 2,827 |
| snake_anaconda | 194,168 | -2.92% | 3 | 33% | 374 |
| snake_viper_tick | 193,538 | -3.23% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,498 | -17.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,546 (-5.23%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,185 | +1.89% |
| random_hold | +1,593 | +0.76% |
| unified | +1,097 | +0.49% |
| benchmark_smallcap | +527 | +0.27% |
| oracle | +436 | +0.20% |
| intramonth | +303 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,654 | -1.73% |
| snake_viper_tick | -4,155 | -2.10% |
| snake_viper_wild | -4,234 | -2.10% |
| snake_abs | -4,479 | -2.18% |
| snake_abs_conv | -4,506 | -2.19% |
| snake_anaconda | -4,535 | -2.28% |
| gold | -4,932 | -2.91% |
| snake_abs_exit | -5,078 | -2.45% |
| snake_abs_exit_conv | -5,216 | -2.52% |

Average per day so far: benchmark Rs +641, unified Rs +635, intramonth Rs +326, oracle Rs +319, random_hold Rs +250, intraweek Rs +199, snake_abs_exit Rs +65, snake_abs_exit_conv Rs +49, nifty_calls Rs +46, snake_abs Rs +26, snake_abs_conv Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -97, snake_anaconda Rs -167, snake_viper_tick Rs -223, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.