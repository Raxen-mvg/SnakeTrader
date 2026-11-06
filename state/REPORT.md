# Paper trading report

Updated 2026-11-06 10:52 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,831 | +7.42% | 0 | - | 236 |
| benchmark | 214,642 | +7.32% | 0 | - | 237 |
| intraweek | 210,436 | +5.22% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,596 | +4.80% | 1 | 100% | 255 |
| snake_abs_exit | 209,380 | +4.69% | 1 | 100% | 260 |
| intramonth | 206,852 | +3.43% | 0 | - | 235 |
| snake_abs | 206,544 | +3.27% | 1 | 100% | 255 |
| snake_abs_conv | 206,378 | +3.19% | 1 | 100% | 255 |
| oracle | 205,014 | +2.51% | 0 | - | 233 |
| random_hold | 203,226 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,069 | -0.97% | 3 | 33% | 702 |
| snake_anaconda | 196,974 | -1.51% | 3 | 33% | 374 |
| benchmark_smallcap | 194,776 | -2.61% | 0 | - | 237 |
| snake_viper_tick | 194,719 | -2.64% | 2 | 0% | 532 |
| gold | 189,914 | -5.04% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,439 (-6.28%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,018 | +0.49% |
| oracle | +942 | +0.46% |
| benchmark | +872 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -1,096 | -0.53% |
| random_hold | -1,097 | -0.54% |
| unified | -1,152 | -0.53% |
| benchmark_smallcap | -3,912 | -1.97% |
| gold | -4,307 | -2.22% |
| snake_abs | -5,145 | -2.43% |
| snake_abs_conv | -5,167 | -2.44% |
| snake_abs_exit_conv | -5,208 | -2.42% |
| snake_abs_exit | -5,278 | -2.46% |
| snake_anaconda | -5,506 | -2.72% |
| snake_viper_tick | -6,419 | -3.19% |
| snake_viper_wild | -6,587 | -3.22% |

Average per day so far: unified Rs +511, benchmark Rs +505, snake_abs_exit_conv Rs +369, snake_abs_exit Rs +361, intraweek Rs +360, snake_abs_conv Rs +245, snake_abs Rs +242, intramonth Rs +236, oracle Rs +173, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -92, snake_anaconda Rs -126, benchmark_smallcap Rs -209, snake_viper_tick Rs -293, gold Rs -348, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.