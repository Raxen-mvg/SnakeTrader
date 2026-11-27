# Paper trading report

Updated 2026-11-27 12:22 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| unified | 223,301 | +11.65% | 0 | - | 236 |
| oracle | 211,936 | +5.97% | 0 | - | 233 |
| intramonth | 210,894 | +5.45% | 0 | - | 235 |
| random_hold | 210,129 | +5.06% | 13 | 69% | 1,037 |
| intraweek | 208,029 | +4.01% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,960 | +2.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,774 | +1.89% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,625 | +0.81% | 0 | - | 237 |
| snake_abs | 200,661 | +0.33% | 1 | 100% | 255 |
| snake_abs_conv | 200,486 | +0.24% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,084 | -2.96% | 3 | 33% | 374 |
| snake_viper_wild | 192,476 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,206 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,315 | -15.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,750 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,883 | +1.93% |
| snake_abs_exit_conv | +3,377 | +1.69% |
| gold | +3,321 | +2.00% |
| snake_abs_conv | +2,119 | +1.07% |
| snake_abs | +2,109 | +1.06% |
| snake_anaconda | +1,788 | +0.93% |
| random_hold | +1,535 | +0.74% |
| intraweek | +981 | +0.47% |
| benchmark_smallcap | +785 | +0.39% |
| intramonth | +360 | +0.17% |
| snake_viper_wild | +270 | +0.14% |
| snake_viper_tick | +265 | +0.14% |
| unified | +222 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -300 | -0.14% |
| benchmark | -1,637 | -0.72% |

Average per day so far: benchmark Rs +580, unified Rs +555, oracle Rs +284, intramonth Rs +259, random_hold Rs +241, intraweek Rs +191, snake_abs_exit Rs +127, snake_abs_exit_conv Rs +97, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +17, snake_abs_conv Rs +12, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -160, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -731

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.