# Paper trading report

Updated 2026-11-06 11:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,742 | +7.37% | 0 | - | 236 |
| benchmark | 214,550 | +7.28% | 0 | - | 237 |
| intraweek | 211,676 | +5.84% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,283 | +4.64% | 1 | 100% | 255 |
| snake_abs_exit | 209,071 | +4.54% | 1 | 100% | 260 |
| intramonth | 206,791 | +3.40% | 0 | - | 235 |
| snake_abs | 206,240 | +3.12% | 1 | 100% | 255 |
| snake_abs_conv | 206,072 | +3.04% | 1 | 100% | 255 |
| oracle | 204,780 | +2.39% | 0 | - | 233 |
| random_hold | 203,371 | +1.69% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,663 | -1.67% | 3 | 33% | 374 |
| snake_viper_wild | 195,365 | -2.32% | 3 | 33% | 702 |
| benchmark_smallcap | 194,798 | -2.60% | 0 | - | 237 |
| snake_viper_tick | 192,056 | -3.97% | 2 | 0% | 532 |
| gold | 190,128 | -4.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,368 (-6.32%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,258 | +1.08% |
| benchmark | +780 | +0.36% |
| oracle | +708 | +0.35% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -953 | -0.47% |
| intramonth | -1,157 | -0.56% |
| unified | -1,242 | -0.57% |
| benchmark_smallcap | -3,890 | -1.96% |
| gold | -4,094 | -2.11% |
| snake_abs | -5,448 | -2.57% |
| snake_abs_conv | -5,473 | -2.59% |
| snake_abs_exit_conv | -5,520 | -2.57% |
| snake_abs_exit | -5,588 | -2.60% |
| snake_anaconda | -5,817 | -2.87% |
| snake_viper_tick | -9,082 | -4.51% |
| snake_viper_wild | -9,291 | -4.54% |

Average per day so far: unified Rs +508, benchmark Rs +502, intraweek Rs +403, snake_abs_exit_conv Rs +357, snake_abs_exit Rs +349, intramonth Rs +234, snake_abs_conv Rs +234, snake_abs Rs +231, oracle Rs +165, random_hold Rs +116, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -139, benchmark_smallcap Rs -208, snake_viper_wild Rs -221, gold Rs -340, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -441

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.