# Paper trading report

Updated 2026-11-18 12:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,087 | +11.54% | 0 | - | 236 |
| benchmark | 220,157 | +10.08% | 0 | - | 237 |
| intraweek | 213,854 | +6.93% | 35 | 54% | 3,851 |
| intramonth | 213,040 | +6.52% | 0 | - | 235 |
| snake_abs_exit | 212,879 | +6.44% | 2 | 50% | 345 |
| oracle | 212,338 | +6.17% | 0 | - | 233 |
| snake_abs_exit_conv | 211,092 | +5.55% | 2 | 50% | 345 |
| snake_abs | 208,058 | +4.03% | 1 | 100% | 255 |
| snake_abs_conv | 207,926 | +3.96% | 1 | 100% | 255 |
| random_hold | 207,417 | +3.71% | 10 | 70% | 733 |
| snake_viper_wild | 207,294 | +3.65% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,752 | +1.88% | 15 | 47% | 2,625 |
| snake_anaconda | 203,169 | +1.58% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,495 | -0.25% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,140 | -11.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,548 (-4.23%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,648 | +0.74% |
| intramonth | +1,498 | +0.71% |
| intraweek | +531 | +0.25% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -148 | -0.07% |
| snake_abs_exit | -263 | -0.12% |
| snake_abs_exit_conv | -482 | -0.23% |
| snake_abs_conv | -494 | -0.24% |
| snake_abs | -501 | -0.24% |
| snake_anaconda | -886 | -0.43% |
| random_hold | -1,015 | -0.49% |
| benchmark_smallcap | -1,076 | -0.54% |
| benchmark | -1,446 | -0.65% |
| snake_viper_tick | -2,084 | -1.01% |
| snake_viper_wild | -2,121 | -1.01% |
| gold | -3,584 | -1.98% |

Average per day so far: unified Rs +641, benchmark Rs +560, snake_abs_exit Rs +390, intraweek Rs +385, intramonth Rs +362, oracle Rs +343, snake_abs_exit_conv Rs +336, snake_viper_wild Rs +260, snake_abs_conv Rs +240, snake_abs Rs +237, random_hold Rs +206, snake_viper_tick Rs +150, snake_anaconda Rs +102, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -16, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.