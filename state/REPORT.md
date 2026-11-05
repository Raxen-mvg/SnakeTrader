# Paper trading report

Updated 2026-11-05 14:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,386 | +8.19% | 0 | - | 236 |
| snake_abs_exit_conv | 214,121 | +7.06% | 1 | 100% | 255 |
| benchmark | 213,946 | +6.97% | 0 | - | 237 |
| snake_abs_exit | 213,873 | +6.94% | 1 | 100% | 260 |
| snake_abs | 211,009 | +5.50% | 1 | 100% | 255 |
| snake_abs_conv | 210,870 | +5.43% | 1 | 100% | 255 |
| intraweek | 210,263 | +5.13% | 25 | 48% | 2,757 |
| intramonth | 208,150 | +4.08% | 0 | - | 235 |
| snake_viper_wild | 206,369 | +3.19% | 3 | 33% | 702 |
| random_hold | 205,161 | +2.58% | 8 | 62% | 649 |
| oracle | 203,599 | +1.80% | 0 | - | 233 |
| snake_viper_tick | 202,821 | +1.41% | 2 | 0% | 532 |
| snake_anaconda | 202,302 | +1.15% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| gold | 194,172 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,674 (-5.16%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,187 | +2.48% |
| gold | +2,778 | +1.45% |
| benchmark_smallcap | +2,477 | +1.26% |
| unified | +1,947 | +0.91% |
| random_hold | +1,852 | +0.91% |
| oracle | +1,807 | +0.90% |
| intramonth | +1,134 | +0.55% |
| intraweek | +565 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -888 | -0.42% |
| snake_abs_exit_conv | -894 | -0.42% |
| snake_abs | -895 | -0.42% |
| snake_abs_exit | -1,027 | -0.48% |
| snake_anaconda | -1,518 | -0.74% |
| snake_viper_tick | -2,580 | -1.26% |
| snake_viper_wild | -2,661 | -1.27% |

Average per day so far: unified Rs +585, snake_abs_exit_conv Rs +565, snake_abs_exit Rs +555, benchmark Rs +498, snake_abs_conv Rs +435, snake_abs Rs +423, intraweek Rs +367, snake_viper_wild Rs +318, intramonth Rs +291, random_hold Rs +184, snake_viper_tick Rs +166, oracle Rs +129, snake_anaconda Rs +100, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.