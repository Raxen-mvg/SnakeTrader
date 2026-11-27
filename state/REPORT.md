# Paper trading report

Updated 2026-11-27 12:43 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| unified | 223,462 | +11.73% | 0 | - | 236 |
| oracle | 212,179 | +6.09% | 0 | - | 233 |
| intramonth | 210,952 | +5.48% | 0 | - | 235 |
| random_hold | 210,484 | +5.24% | 13 | 69% | 1,037 |
| intraweek | 208,195 | +4.10% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,981 | +2.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,702 | +1.85% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,681 | +0.84% | 0 | - | 237 |
| snake_abs | 200,495 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,316 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,914 | -3.04% | 3 | 33% | 374 |
| snake_viper_wild | 192,394 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,127 | -5.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,775 | -15.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,921 (-5.54%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,903 | +1.94% |
| gold | +3,781 | +2.28% |
| snake_abs_exit_conv | +3,305 | +1.65% |
| snake_abs_conv | +1,949 | +0.98% |
| snake_abs | +1,943 | +0.98% |
| random_hold | +1,890 | +0.91% |
| snake_anaconda | +1,618 | +0.84% |
| intraweek | +1,147 | +0.55% |
| benchmark_smallcap | +841 | +0.42% |
| intramonth | +419 | +0.20% |
| unified | +383 | +0.17% |
| snake_viper_wild | +189 | +0.10% |
| snake_viper_tick | +185 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -56 | -0.03% |
| benchmark | -1,637 | -0.72% |

Average per day so far: benchmark Rs +580, unified Rs +559, oracle Rs +290, intramonth Rs +261, random_hold Rs +250, intraweek Rs +195, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +95, benchmark_smallcap Rs +44, nifty_calls Rs +44, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -164, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -720

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.