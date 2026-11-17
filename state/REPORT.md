# Paper trading report

Updated 2026-11-17 12:16 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,330 | +11.16% | 0 | - | 237 |
| unified | 222,041 | +11.02% | 0 | - | 236 |
| snake_abs_exit | 214,956 | +7.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,192 | +6.60% | 2 | 50% | 345 |
| intraweek | 212,537 | +6.27% | 35 | 54% | 3,851 |
| oracle | 212,210 | +6.11% | 0 | - | 233 |
| intramonth | 212,160 | +6.08% | 0 | - | 235 |
| snake_abs | 209,884 | +4.94% | 1 | 100% | 255 |
| snake_abs_conv | 209,740 | +4.87% | 1 | 100% | 255 |
| snake_viper_wild | 208,074 | +4.04% | 14 | 50% | 2,496 |
| random_hold | 207,689 | +3.85% | 10 | 70% | 733 |
| snake_anaconda | 205,393 | +2.70% | 3 | 33% | 374 |
| snake_viper_tick | 204,517 | +2.26% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,168 | -9.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,221 (-4.39%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,249 | +1.02% |
| snake_viper_wild | +1,930 | +0.94% |
| snake_viper_tick | +1,897 | +0.94% |
| benchmark_smallcap | +1,300 | +0.65% |
| intraweek | +1,271 | +0.60% |
| unified | +603 | +0.27% |
| snake_abs_exit | +547 | +0.26% |
| intramonth | +542 | +0.26% |
| snake_anaconda | +290 | +0.14% |
| gold | +214 | +0.12% |
| oracle | +187 | +0.09% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit_conv | -25 | -0.01% |
| random_hold | -104 | -0.05% |
| snake_abs_conv | -249 | -0.12% |
| snake_abs | -250 | -0.12% |

Average per day so far: benchmark Rs +638, unified Rs +630, snake_abs_exit Rs +467, snake_abs_exit_conv Rs +412, intraweek Rs +358, oracle Rs +349, intramonth Rs +347, snake_abs_conv Rs +304, snake_abs Rs +300, snake_viper_wild Rs +299, random_hold Rs +220, snake_viper_tick Rs +188, snake_anaconda Rs +180, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -538

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.