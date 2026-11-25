# Paper trading report

Updated 2026-11-25 15:26 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,923 | +12.46% | 0 | - | 237 |
| unified | 223,952 | +11.98% | 0 | - | 236 |
| oracle | 213,960 | +6.98% | 0 | - | 233 |
| intramonth | 211,674 | +5.84% | 0 | - | 235 |
| random_hold | 209,449 | +4.72% | 12 | 75% | 1,009 |
| intraweek | 206,583 | +3.29% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,214 | +1.11% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,890 | +0.94% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,060 | +0.03% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,886 | -0.06% | 1 | 100% | 255 |
| benchmark_smallcap | 198,105 | -0.95% | 0 | - | 237 |
| snake_viper_wild | 197,452 | -1.27% | 16 | 50% | 2,827 |
| snake_anaconda | 194,596 | -2.70% | 3 | 33% | 374 |
| snake_viper_tick | 194,088 | -2.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,564 | -17.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,972 (-5.51%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,450 | +1.56% |
| oracle | +1,618 | +0.76% |
| random_hold | +1,022 | +0.49% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -333 | -0.15% |
| benchmark_smallcap | -874 | -0.44% |
| intramonth | -1,077 | -0.51% |
| snake_viper_tick | -3,605 | -1.82% |
| snake_viper_wild | -3,672 | -1.83% |
| snake_anaconda | -4,107 | -2.07% |
| gold | -4,866 | -2.87% |
| intraweek | -5,036 | -2.38% |
| snake_abs_exit_conv | -5,155 | -2.49% |
| snake_abs_exit | -5,281 | -2.54% |
| snake_abs | -5,401 | -2.63% |
| snake_abs_conv | -5,417 | -2.64% |

Average per day so far: benchmark Rs +623, unified Rs +599, oracle Rs +349, intramonth Rs +292, random_hold Rs +236, intraweek Rs +165, snake_abs_exit Rs +60, snake_abs_exit_conv Rs +51, nifty_calls Rs +46, snake_abs Rs +2, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -3, benchmark_smallcap Rs -53, snake_viper_wild Rs -80, snake_anaconda Rs -154, snake_viper_tick Rs -204, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.