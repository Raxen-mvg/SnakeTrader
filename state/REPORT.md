# Paper trading report

Updated 2026-11-04 10:11 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 212,612 | +6.31% | 0 | - | 236 |
| snake_abs_exit_conv | 209,574 | +4.79% | 1 | 100% | 255 |
| snake_abs_exit | 209,424 | +4.71% | 1 | 100% | 260 |
| benchmark | 208,598 | +4.30% | 0 | - | 237 |
| intraweek | 207,899 | +3.95% | 25 | 48% | 2,757 |
| snake_viper_wild | 206,547 | +3.27% | 3 | 33% | 702 |
| snake_abs | 206,467 | +3.23% | 1 | 100% | 255 |
| snake_abs_conv | 206,319 | +3.16% | 1 | 100% | 255 |
| intramonth | 205,156 | +2.58% | 0 | - | 235 |
| snake_viper_tick | 202,946 | +1.47% | 2 | 0% | 532 |
| random_hold | 202,531 | +1.26% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,267 | +0.13% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,156 | -0.92% | 3 | 33% | 361 |
| benchmark_smallcap | 194,619 | -2.69% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,070 | -6.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,504 (-5.75%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +5,409 | +2.65% |
| snake_abs_exit_conv | +5,236 | +2.56% |
| snake_abs_conv | +5,178 | +2.57% |
| snake_abs | +5,157 | +2.56% |
| snake_anaconda | +4,331 | +2.23% |
| intraweek | +2,813 | +1.37% |
| random_hold | +2,062 | +1.03% |
| benchmark | +1,897 | +0.92% |
| gold | +1,792 | +0.97% |
| benchmark_smallcap | +1,682 | +0.87% |
| intramonth | +1,185 | +0.58% |
| unified | +611 | +0.29% |
| oracle | +278 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,221 | -2.04% |
| snake_viper_wild | -4,346 | -2.06% |

Average per day so far: unified Rs +467, snake_abs_exit_conv Rs +399, snake_abs_exit Rs +393, snake_viper_wild Rs +345, benchmark Rs +318, intraweek Rs +293, snake_abs_conv Rs +263, snake_abs Rs +259, intramonth Rs +191, snake_viper_tick Rs +184, random_hold Rs +94, nifty_calls Rs +68, oracle Rs +10, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -84, benchmark_smallcap Rs -234, snake_nonews Rs -444, snake Rs -467, gold Rs -479

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.