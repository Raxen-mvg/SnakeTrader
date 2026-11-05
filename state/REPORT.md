# Paper trading report

Updated 2026-11-05 15:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,885 | +7.94% | 0 | - | 236 |
| snake_abs_exit_conv | 214,866 | +7.43% | 1 | 100% | 255 |
| snake_abs_exit | 214,682 | +7.34% | 1 | 100% | 260 |
| benchmark | 214,022 | +7.01% | 0 | - | 237 |
| snake_abs | 211,744 | +5.87% | 1 | 100% | 255 |
| snake_abs_conv | 211,605 | +5.80% | 1 | 100% | 255 |
| intraweek | 208,710 | +4.36% | 25 | 48% | 2,757 |
| intramonth | 207,820 | +3.91% | 0 | - | 235 |
| snake_viper_wild | 204,600 | +2.30% | 3 | 33% | 702 |
| random_hold | 204,154 | +2.08% | 8 | 62% | 649 |
| oracle | 204,142 | +2.07% | 0 | - | 233 |
| snake_anaconda | 202,642 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,085 | +0.54% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,408 | -0.80% | 0 | - | 237 |
| gold | 194,336 | -2.83% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,277 (-5.36%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,263 | +2.52% |
| gold | +2,943 | +1.54% |
| oracle | +2,349 | +1.16% |
| benchmark_smallcap | +1,738 | +0.88% |
| unified | +1,446 | +0.67% |
| random_hold | +845 | +0.42% |
| intramonth | +804 | +0.39% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -149 | -0.07% |
| snake_abs_conv | -153 | -0.07% |
| snake_abs | -159 | -0.07% |
| snake_abs_exit | -218 | -0.10% |
| intraweek | -988 | -0.47% |
| snake_anaconda | -1,178 | -0.58% |
| snake_viper_tick | -4,316 | -2.10% |
| snake_viper_wild | -4,430 | -2.12% |

Average per day so far: snake_abs_exit_conv Rs +595, snake_abs_exit Rs +587, unified Rs +567, benchmark Rs +501, snake_abs_conv Rs +464, snake_abs Rs +452, intraweek Rs +311, intramonth Rs +279, snake_viper_wild Rs +230, random_hold Rs +148, oracle Rs +148, snake_anaconda Rs +115, nifty_calls Rs +66, snake_viper_tick Rs +64, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -66, gold Rs -202, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.