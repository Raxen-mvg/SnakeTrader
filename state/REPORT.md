# Paper trading report

Updated 2026-11-05 13:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,430 | +8.21% | 0 | - | 236 |
| snake_abs_exit_conv | 214,329 | +7.17% | 1 | 100% | 255 |
| snake_abs_exit | 214,087 | +7.04% | 1 | 100% | 260 |
| benchmark | 214,014 | +7.01% | 0 | - | 237 |
| snake_abs | 211,209 | +5.60% | 1 | 100% | 255 |
| snake_abs_conv | 211,074 | +5.54% | 1 | 100% | 255 |
| intraweek | 210,157 | +5.08% | 25 | 48% | 2,757 |
| intramonth | 208,183 | +4.09% | 0 | - | 235 |
| snake_viper_wild | 206,423 | +3.21% | 3 | 33% | 702 |
| random_hold | 205,171 | +2.58% | 8 | 62% | 649 |
| oracle | 203,496 | +1.75% | 0 | - | 233 |
| snake_viper_tick | 202,875 | +1.44% | 2 | 0% | 532 |
| snake_anaconda | 202,451 | +1.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,058 | -0.47% | 0 | - | 237 |
| gold | 194,271 | -2.87% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,736 (-5.13%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,256 | +2.52% |
| gold | +2,877 | +1.50% |
| benchmark_smallcap | +2,388 | +1.21% |
| unified | +1,990 | +0.93% |
| random_hold | +1,862 | +0.92% |
| oracle | +1,704 | +0.84% |
| intramonth | +1,167 | +0.56% |
| intraweek | +459 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -684 | -0.32% |
| snake_abs_exit_conv | -686 | -0.32% |
| snake_abs | -694 | -0.33% |
| snake_abs_exit | -813 | -0.38% |
| snake_anaconda | -1,369 | -0.67% |
| snake_viper_tick | -2,525 | -1.23% |
| snake_viper_wild | -2,606 | -1.25% |

Average per day so far: unified Rs +587, snake_abs_exit_conv Rs +573, snake_abs_exit Rs +563, benchmark Rs +501, snake_abs_conv Rs +443, snake_abs Rs +431, intraweek Rs +363, snake_viper_wild Rs +321, intramonth Rs +292, random_hold Rs +185, snake_viper_tick Rs +169, oracle Rs +125, snake_anaconda Rs +107, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -39, gold Rs -205, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.