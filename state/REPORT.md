# Paper trading report

Updated 2026-11-04 10:47 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,718 | +6.36% | 0 | - | 236 |
| snake_abs_exit_conv | 208,692 | +4.35% | 1 | 100% | 255 |
| snake_abs_exit | 208,536 | +4.27% | 1 | 100% | 260 |
| benchmark | 207,902 | +3.95% | 0 | - | 237 |
| intraweek | 207,839 | +3.92% | 25 | 48% | 2,757 |
| snake_viper_wild | 207,099 | +3.55% | 3 | 33% | 702 |
| snake_abs | 205,599 | +2.80% | 1 | 100% | 255 |
| intramonth | 205,553 | +2.78% | 0 | - | 235 |
| snake_abs_conv | 205,448 | +2.72% | 1 | 100% | 255 |
| snake_viper_tick | 203,489 | +1.74% | 2 | 0% | 532 |
| random_hold | 202,332 | +1.17% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,408 | +0.20% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,444 | -1.28% | 3 | 33% | 361 |
| benchmark_smallcap | 194,383 | -2.81% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,563 | -6.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,727 (-5.64%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,521 | +2.22% |
| snake_abs_exit_conv | +4,354 | +2.13% |
| snake_abs_conv | +4,307 | +2.14% |
| snake_abs | +4,290 | +2.13% |
| snake_anaconda | +3,620 | +1.87% |
| intraweek | +2,754 | +1.34% |
| gold | +2,285 | +1.23% |
| random_hold | +1,864 | +0.93% |
| intramonth | +1,582 | +0.78% |
| benchmark_smallcap | +1,446 | +0.75% |
| benchmark | +1,201 | +0.58% |
| unified | +717 | +0.34% |
| oracle | +419 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,678 | -1.77% |
| snake_viper_wild | -3,793 | -1.80% |

Average per day so far: unified Rs +471, snake_viper_wild Rs +374, snake_abs_exit_conv Rs +362, snake_abs_exit Rs +356, benchmark Rs +293, intraweek Rs +290, snake_abs_conv Rs +227, snake_abs Rs +224, snake_viper_tick Rs +218, intramonth Rs +206, random_hold Rs +86, nifty_calls Rs +68, oracle Rs +15, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -116, benchmark_smallcap Rs -244, snake_nonews Rs -444, gold Rs -461, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.