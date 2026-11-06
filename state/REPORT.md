# Paper trading report

Updated 2026-11-06 10:24 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,986 | +7.49% | 0 | - | 237 |
| unified | 214,915 | +7.46% | 0 | - | 236 |
| intraweek | 210,666 | +5.33% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,544 | +4.77% | 1 | 100% | 255 |
| snake_abs_exit | 209,328 | +4.66% | 1 | 100% | 260 |
| intramonth | 206,978 | +3.49% | 0 | - | 235 |
| snake_abs | 206,495 | +3.25% | 1 | 100% | 255 |
| snake_abs_conv | 206,326 | +3.16% | 1 | 100% | 255 |
| oracle | 204,602 | +2.30% | 0 | - | 233 |
| random_hold | 203,566 | +1.78% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 197,794 | -1.10% | 3 | 33% | 702 |
| snake_anaconda | 196,703 | -1.65% | 3 | 33% | 374 |
| benchmark_smallcap | 195,157 | -2.42% | 0 | - | 237 |
| snake_viper_tick | 194,435 | -2.78% | 2 | 0% | 532 |
| gold | 190,292 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,455 (-6.27%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,248 | +0.60% |
| benchmark | +1,216 | +0.57% |
| oracle | +530 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -757 | -0.37% |
| intramonth | -971 | -0.47% |
| unified | -1,069 | -0.49% |
| benchmark_smallcap | -3,531 | -1.78% |
| gold | -3,929 | -2.02% |
| snake_abs | -5,194 | -2.45% |
| snake_abs_conv | -5,219 | -2.47% |
| snake_abs_exit_conv | -5,259 | -2.45% |
| snake_abs_exit | -5,331 | -2.48% |
| snake_anaconda | -5,776 | -2.85% |
| snake_viper_tick | -6,703 | -3.33% |
| snake_viper_wild | -6,862 | -3.35% |

Average per day so far: benchmark Rs +517, unified Rs +514, intraweek Rs +368, snake_abs_exit_conv Rs +367, snake_abs_exit Rs +359, snake_abs_conv Rs +243, intramonth Rs +241, snake_abs Rs +241, oracle Rs +159, random_hold Rs +123, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -105, snake_anaconda Rs -137, benchmark_smallcap Rs -194, snake_viper_tick Rs -309, gold Rs -335, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.