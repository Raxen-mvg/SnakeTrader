# Paper trading report

Updated 2026-11-23 11:24 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,221 | +12.11% | 0 | - | 236 |
| benchmark | 223,378 | +11.69% | 0 | - | 237 |
| intraweek | 213,036 | +6.52% | 40 | 55% | 4,400 |
| intramonth | 212,444 | +6.22% | 0 | - | 235 |
| oracle | 211,608 | +5.80% | 0 | - | 233 |
| random_hold | 210,189 | +5.09% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,969 | +3.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,993 | +3.00% | 2 | 50% | 345 |
| snake_abs | 204,294 | +2.15% | 1 | 100% | 255 |
| snake_abs_conv | 204,130 | +2.06% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,129 | +0.56% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,630 | -0.18% | 0 | - | 237 |
| snake_anaconda | 198,090 | -0.95% | 3 | 33% | 374 |
| snake_viper_tick | 197,697 | -1.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,022 | -14.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,458 (-4.77%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,973 | +1.17% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -570 | -0.27% |
| snake_abs_exit_conv | -623 | -0.30% |
| oracle | -870 | -0.41% |
| benchmark_smallcap | -1,278 | -0.64% |
| snake_abs_exit | -1,593 | -0.76% |
| snake_abs | -1,626 | -0.79% |
| snake_abs_conv | -1,653 | -0.80% |
| snake_viper_tick | -1,674 | -0.84% |
| snake_viper_wild | -1,700 | -0.84% |
| benchmark | -1,760 | -0.78% |
| snake_anaconda | -1,816 | -0.91% |
| unified | -1,961 | -0.87% |
| intramonth | -2,561 | -1.19% |
| intraweek | -2,676 | -1.24% |

Average per day so far: unified Rs +621, benchmark Rs +599, intraweek Rs +334, intramonth Rs +319, oracle Rs +298, random_hold Rs +261, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +166, snake_abs Rs +116, snake_abs_conv Rs +115, nifty_calls Rs +47, snake_viper_wild Rs +36, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_anaconda Rs -56, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -769

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.