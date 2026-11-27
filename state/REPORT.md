# Paper trading report

Updated 2026-11-27 14:25 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,051 | +12.03% | 0 | - | 237 |
| unified | 223,618 | +11.81% | 0 | - | 236 |
| oracle | 212,154 | +6.08% | 0 | - | 233 |
| random_hold | 211,107 | +5.55% | 13 | 69% | 1,037 |
| intramonth | 210,979 | +5.49% | 0 | - | 235 |
| intraweek | 208,169 | +4.08% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,538 | +3.27% | 2 | 50% | 345 |
| snake_abs_exit | 204,241 | +2.12% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,758 | -0.12% | 1 | 100% | 255 |
| snake_abs_conv | 199,574 | -0.21% | 1 | 100% | 255 |
| snake_anaconda | 193,195 | -3.40% | 3 | 33% | 374 |
| snake_viper_wild | 192,174 | -3.91% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,910 | -5.54% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,761 | -14.62% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,044 (-5.48%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,141 | +3.06% |
| gold | +4,768 | +2.87% |
| snake_abs_exit | +3,163 | +1.57% |
| random_hold | +2,513 | +1.21% |
| snake_abs_conv | +1,208 | +0.61% |
| snake_abs | +1,205 | +0.61% |
| intraweek | +1,120 | +0.54% |
| snake_anaconda | +899 | +0.47% |
| benchmark_smallcap | +706 | +0.35% |
| unified | +539 | +0.24% |
| intramonth | +446 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -31 | -0.02% |
| snake_viper_wild | -32 | -0.02% |
| oracle | -81 | -0.04% |
| benchmark | -1,935 | -0.86% |

Average per day so far: benchmark Rs +573, unified Rs +562, oracle Rs +289, random_hold Rs +264, intramonth Rs +261, intraweek Rs +194, snake_abs_exit_conv Rs +168, snake_abs_exit Rs +109, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, snake_anaconda Rs -184, snake_viper_wild Rs -230, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -358, gold Rs -696

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.