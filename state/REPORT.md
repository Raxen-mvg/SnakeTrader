# Paper trading report

Updated 2026-11-09 13:58 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,055 | +10.03% | 0 | - | 236 |
| benchmark | 217,472 | +8.74% | 0 | - | 237 |
| intraweek | 214,565 | +7.28% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,324 | +6.66% | 2 | 50% | 330 |
| snake_abs_exit | 212,886 | +6.44% | 2 | 50% | 308 |
| snake_abs | 210,229 | +5.11% | 1 | 100% | 255 |
| intramonth | 210,131 | +5.07% | 0 | - | 235 |
| snake_abs_conv | 210,063 | +5.03% | 1 | 100% | 255 |
| oracle | 209,409 | +4.71% | 0 | - | 233 |
| random_hold | 204,439 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,301 | +0.15% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,495 | -0.25% | 7 | 57% | 1,332 |
| benchmark_smallcap | 197,948 | -1.03% | 0 | - | 237 |
| snake_viper_tick | 196,107 | -1.95% | 6 | 50% | 1,154 |
| gold | 192,183 | -3.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,366 (-4.82%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,902 | +2.35% |
| snake_abs_conv | +4,836 | +2.36% |
| snake_abs | +4,810 | +2.34% |
| snake_abs_exit | +4,574 | +2.20% |
| snake_anaconda | +4,474 | +2.29% |
| unified | +4,446 | +2.06% |
| intraweek | +4,203 | +2.00% |
| oracle | +3,582 | +1.74% |
| snake_viper_wild | +3,458 | +1.76% |
| snake_viper_tick | +3,397 | +1.76% |
| intramonth | +2,528 | +1.22% |
| benchmark_smallcap | +1,155 | +0.59% |
| gold | +1,134 | +0.59% |
| random_hold | +532 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -15 | -0.01% |

Average per day so far: unified Rs +669, benchmark Rs +582, snake_abs_exit_conv Rs +493, intraweek Rs +486, snake_abs_exit Rs +477, snake_abs_conv Rs +373, snake_abs Rs +365, intramonth Rs +338, oracle Rs +314, random_hold Rs +148, nifty_calls Rs +61, snake_anaconda Rs +12, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_viper_wild Rs -23, benchmark_smallcap Rs -79, snake_viper_tick Rs -205, gold Rs -261, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.