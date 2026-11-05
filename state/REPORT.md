# Paper trading report

Updated 2026-11-05 14:07 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,255 | +8.13% | 0 | - | 236 |
| benchmark | 214,076 | +7.04% | 0 | - | 237 |
| snake_abs_exit_conv | 213,944 | +6.97% | 1 | 100% | 255 |
| snake_abs_exit | 213,698 | +6.85% | 1 | 100% | 260 |
| snake_abs | 210,835 | +5.42% | 1 | 100% | 255 |
| snake_abs_conv | 210,695 | +5.35% | 1 | 100% | 255 |
| intraweek | 209,721 | +4.86% | 25 | 48% | 2,757 |
| intramonth | 207,841 | +3.92% | 0 | - | 235 |
| snake_viper_wild | 205,879 | +2.94% | 3 | 33% | 702 |
| random_hold | 205,151 | +2.58% | 8 | 62% | 649 |
| oracle | 203,664 | +1.83% | 0 | - | 233 |
| snake_viper_tick | 202,338 | +1.17% | 2 | 0% | 532 |
| snake_anaconda | 202,113 | +1.06% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 194,139 | -2.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,414 (-5.29%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,317 | +2.55% |
| gold | +2,745 | +1.43% |
| benchmark_smallcap | +2,545 | +1.29% |
| oracle | +1,872 | +0.93% |
| random_hold | +1,842 | +0.91% |
| unified | +1,815 | +0.85% |
| intramonth | +825 | +0.40% |
| intraweek | +23 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,063 | -0.50% |
| snake_abs | -1,068 | -0.50% |
| snake_abs_exit_conv | -1,071 | -0.50% |
| snake_abs_exit | -1,202 | -0.56% |
| snake_anaconda | -1,707 | -0.84% |
| snake_viper_tick | -3,062 | -1.49% |
| snake_viper_wild | -3,151 | -1.51% |

Average per day so far: unified Rs +581, snake_abs_exit_conv Rs +558, snake_abs_exit Rs +548, benchmark Rs +503, snake_abs_conv Rs +428, snake_abs Rs +417, intraweek Rs +347, snake_viper_wild Rs +294, intramonth Rs +280, random_hold Rs +184, snake_viper_tick Rs +138, oracle Rs +131, snake_anaconda Rs +92, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -209, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.