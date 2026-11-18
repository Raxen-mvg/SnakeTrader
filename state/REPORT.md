# Paper trading report

Updated 2026-11-18 10:16 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,198 | +11.10% | 0 | - | 236 |
| benchmark | 220,456 | +10.23% | 0 | - | 237 |
| intraweek | 214,411 | +7.21% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,690 | +6.34% | 2 | 50% | 345 |
| oracle | 212,300 | +6.15% | 0 | - | 233 |
| intramonth | 212,178 | +6.09% | 0 | - | 235 |
| snake_abs_exit_conv | 211,029 | +5.51% | 2 | 50% | 345 |
| snake_abs | 208,293 | +4.15% | 1 | 100% | 255 |
| snake_abs_conv | 208,143 | +4.07% | 1 | 100% | 255 |
| random_hold | 207,385 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 207,323 | +3.66% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,781 | +1.89% | 15 | 47% | 2,625 |
| snake_anaconda | 202,866 | +1.43% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,145 | +0.07% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,337 | -11.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,330 (-4.34%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,088 | +0.51% |
| unified | +759 | +0.34% |
| intramonth | +635 | +0.30% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -186 | -0.09% |
| snake_abs | -265 | -0.13% |
| snake_abs_conv | -277 | -0.13% |
| benchmark_smallcap | -426 | -0.21% |
| snake_abs_exit | -452 | -0.21% |
| snake_abs_exit_conv | -545 | -0.26% |
| random_hold | -1,047 | -0.50% |
| benchmark | -1,148 | -0.52% |
| snake_anaconda | -1,189 | -0.58% |
| snake_viper_tick | -2,056 | -1.00% |
| snake_viper_wild | -2,092 | -1.00% |
| gold | -3,387 | -1.87% |

Average per day so far: unified Rs +617, benchmark Rs +568, intraweek Rs +400, snake_abs_exit Rs +385, oracle Rs +342, intramonth Rs +338, snake_abs_exit_conv Rs +334, snake_viper_wild Rs +262, snake_abs_conv Rs +247, snake_abs Rs +244, random_hold Rs +205, snake_viper_tick Rs +151, snake_anaconda Rs +92, nifty_calls Rs +51, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.