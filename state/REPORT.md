# Paper trading report

Updated 2026-11-06 10:02 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,897 | +7.45% | 0 | - | 236 |
| benchmark | 214,542 | +7.27% | 0 | - | 237 |
| intraweek | 211,553 | +5.78% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,202 | +5.10% | 1 | 100% | 255 |
| snake_abs_exit | 209,984 | +4.99% | 1 | 100% | 260 |
| snake_abs | 207,145 | +3.57% | 1 | 100% | 255 |
| intramonth | 206,981 | +3.49% | 0 | - | 235 |
| snake_abs_conv | 206,975 | +3.49% | 1 | 100% | 255 |
| oracle | 204,723 | +2.36% | 0 | - | 233 |
| random_hold | 204,132 | +2.07% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,247 | -0.88% | 3 | 33% | 702 |
| snake_anaconda | 197,120 | -1.44% | 3 | 33% | 374 |
| benchmark_smallcap | 194,977 | -2.51% | 0 | - | 237 |
| snake_viper_tick | 194,886 | -2.56% | 2 | 0% | 532 |
| gold | 190,391 | -4.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,800 (-6.10%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,135 | +1.02% |
| benchmark | +773 | +0.36% |
| oracle | +651 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -191 | -0.09% |
| intramonth | -968 | -0.47% |
| unified | -1,086 | -0.50% |
| benchmark_smallcap | -3,711 | -1.87% |
| gold | -3,831 | -1.97% |
| snake_abs | -4,543 | -2.15% |
| snake_abs_conv | -4,570 | -2.16% |
| snake_abs_exit_conv | -4,602 | -2.14% |
| snake_abs_exit | -4,675 | -2.18% |
| snake_anaconda | -5,359 | -2.65% |
| snake_viper_tick | -6,252 | -3.11% |
| snake_viper_wild | -6,409 | -3.13% |

Average per day so far: unified Rs +514, benchmark Rs +501, intraweek Rs +398, snake_abs_exit_conv Rs +392, snake_abs_exit Rs +384, snake_abs_conv Rs +268, snake_abs Rs +265, intramonth Rs +241, oracle Rs +163, random_hold Rs +142, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -83, snake_anaconda Rs -120, benchmark_smallcap Rs -201, snake_viper_tick Rs -284, gold Rs -331, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.