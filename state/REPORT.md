# Paper trading report

Updated 2026-11-27 14:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,166 | +12.08% | 0 | - | 237 |
| unified | 223,536 | +11.77% | 0 | - | 236 |
| oracle | 212,240 | +6.12% | 0 | - | 233 |
| random_hold | 211,218 | +5.61% | 13 | 69% | 1,037 |
| intramonth | 210,922 | +5.46% | 0 | - | 235 |
| intraweek | 208,548 | +4.27% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,440 | +3.22% | 2 | 50% | 345 |
| snake_abs_exit | 204,155 | +2.08% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,591 | +0.80% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,673 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,484 | -0.26% | 1 | 100% | 255 |
| snake_anaconda | 193,107 | -3.45% | 3 | 33% | 374 |
| snake_viper_wild | 192,337 | -3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,070 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,548 | -14.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,099 (-5.45%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,043 | +3.02% |
| gold | +4,554 | +2.74% |
| snake_abs_exit | +3,078 | +1.53% |
| random_hold | +2,624 | +1.26% |
| intraweek | +1,499 | +0.72% |
| snake_abs | +1,121 | +0.56% |
| snake_abs_conv | +1,117 | +0.56% |
| snake_anaconda | +810 | +0.42% |
| benchmark_smallcap | +751 | +0.37% |
| unified | +457 | +0.20% |
| intramonth | +389 | +0.18% |
| snake_viper_wild | +131 | +0.07% |
| snake_viper_tick | +129 | +0.07% |
| oracle | +5 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -1,821 | -0.81% |

Average per day so far: benchmark Rs +575, unified Rs +560, oracle Rs +291, random_hold Rs +267, intramonth Rs +260, intraweek Rs +204, snake_abs_exit_conv Rs +165, snake_abs_exit Rs +107, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, snake_anaconda Rs -186, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -353, gold Rs -701

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.