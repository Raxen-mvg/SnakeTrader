# Paper trading report

Updated 2026-11-19 13:58 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,904 | +11.95% | 0 | - | 236 |
| benchmark | 221,703 | +10.85% | 0 | - | 237 |
| intramonth | 213,453 | +6.73% | 0 | - | 235 |
| snake_abs_exit | 212,690 | +6.34% | 2 | 50% | 345 |
| intraweek | 211,770 | +5.88% | 35 | 54% | 3,851 |
| oracle | 211,566 | +5.78% | 0 | - | 233 |
| snake_abs_exit_conv | 210,360 | +5.18% | 2 | 50% | 345 |
| snake_abs | 208,356 | +4.18% | 1 | 100% | 255 |
| snake_abs_conv | 208,221 | +4.11% | 1 | 100% | 255 |
| random_hold | 207,779 | +3.89% | 10 | 70% | 733 |
| snake_viper_wild | 207,566 | +3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,019 | +2.01% | 15 | 47% | 2,625 |
| snake_anaconda | 202,868 | +1.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,019 | -12.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,354 (-4.32%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,408 | +0.64% |
| unified | +1,293 | +0.58% |
| benchmark_smallcap | +1,278 | +0.64% |
| intramonth | +1,179 | +0.56% |
| random_hold | +847 | +0.41% |
| oracle | +770 | +0.36% |
| snake_viper_wild | +527 | +0.25% |
| snake_viper_tick | +516 | +0.25% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -70 | -0.03% |
| snake_abs | -1,080 | -0.52% |
| snake_abs_conv | -1,104 | -0.53% |
| snake_abs_exit | -1,342 | -0.63% |
| snake_anaconda | -1,533 | -0.75% |
| snake_abs_exit_conv | -2,023 | -0.95% |
| gold | -2,302 | -1.30% |

Average per day so far: unified Rs +646, benchmark Rs +587, snake_abs_exit Rs +373, intramonth Rs +364, intraweek Rs +318, oracle Rs +313, snake_abs_exit_conv Rs +305, snake_viper_wild Rs +261, snake_abs_conv Rs +242, snake_abs Rs +239, random_hold Rs +210, snake_viper_tick Rs +155, snake_anaconda Rs +90, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.