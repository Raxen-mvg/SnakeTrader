# Paper trading report

Updated 2026-11-09 09:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,807 | +10.90% | 0 | - | 236 |
| benchmark | 217,358 | +8.68% | 0 | - | 237 |
| intraweek | 215,730 | +7.87% | 25 | 48% | 2,757 |
| intramonth | 211,736 | +5.87% | 0 | - | 235 |
| snake_abs_exit_conv | 211,604 | +5.80% | 1 | 100% | 255 |
| snake_abs_exit | 211,513 | +5.76% | 1 | 100% | 260 |
| oracle | 209,134 | +4.57% | 0 | - | 233 |
| snake_abs | 208,540 | +4.27% | 1 | 100% | 255 |
| snake_abs_conv | 208,372 | +4.19% | 1 | 100% | 255 |
| random_hold | 204,921 | +2.46% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,844 | -0.08% | 4 | 25% | 842 |
| snake_anaconda | 198,694 | -0.65% | 3 | 33% | 374 |
| benchmark_smallcap | 197,914 | -1.04% | 0 | - | 237 |
| snake_viper_tick | 196,451 | -1.77% | 3 | 0% | 672 |
| gold | 192,775 | -3.61% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,899 (-4.55%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +6,197 | +2.87% |
| intraweek | +5,368 | +2.55% |
| intramonth | +4,133 | +1.99% |
| snake_viper_wild | +3,807 | +1.94% |
| snake_viper_tick | +3,741 | +1.94% |
| oracle | +3,307 | +1.61% |
| snake_abs_exit | +3,201 | +1.54% |
| snake_abs_exit_conv | +3,183 | +1.53% |
| snake_abs_conv | +3,145 | +1.53% |
| snake_abs | +3,121 | +1.52% |
| snake_anaconda | +2,867 | +1.46% |
| gold | +1,726 | +0.90% |
| benchmark_smallcap | +1,121 | +0.57% |
| random_hold | +1,014 | +0.50% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -130 | -0.06% |

Average per day so far: unified Rs +727, benchmark Rs +579, intraweek Rs +524, snake_abs_exit_conv Rs +430, snake_abs_exit Rs +426, intramonth Rs +391, snake_abs_conv Rs +310, snake_abs Rs +305, oracle Rs +304, random_hold Rs +164, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -7, snake_anaconda Rs -52, benchmark_smallcap Rs -80, snake_viper_tick Rs -187, gold Rs -241, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.