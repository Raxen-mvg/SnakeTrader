# Paper trading report

Updated 2026-11-18 14:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,196 | +11.10% | 0 | - | 236 |
| benchmark | 220,333 | +10.17% | 0 | - | 237 |
| snake_abs_exit | 214,369 | +7.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,717 | +6.36% | 2 | 50% | 345 |
| intramonth | 211,852 | +5.93% | 0 | - | 235 |
| intraweek | 211,601 | +5.80% | 35 | 54% | 3,851 |
| oracle | 211,286 | +5.64% | 0 | - | 233 |
| snake_abs | 209,858 | +4.93% | 1 | 100% | 255 |
| snake_abs_conv | 209,748 | +4.87% | 1 | 100% | 255 |
| snake_viper_wild | 207,135 | +3.57% | 16 | 50% | 2,827 |
| random_hold | 206,818 | +3.41% | 10 | 70% | 733 |
| snake_anaconda | 204,678 | +2.34% | 3 | 33% | 374 |
| snake_viper_tick | 203,597 | +1.80% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,708 | -0.15% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,107 | -11.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,629 (-4.69%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,328 | +0.64% |
| snake_abs | +1,300 | +0.62% |
| snake_abs_exit | +1,227 | +0.58% |
| snake_abs_exit_conv | +1,143 | +0.54% |
| unified | +757 | +0.34% |
| snake_anaconda | +623 | +0.30% |
| intramonth | +310 | +0.15% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -863 | -0.43% |
| oracle | -1,200 | -0.56% |
| benchmark | -1,270 | -0.57% |
| random_hold | -1,614 | -0.77% |
| intraweek | -1,722 | -0.81% |
| snake_viper_tick | -2,239 | -1.09% |
| snake_viper_wild | -2,280 | -1.09% |
| gold | -3,617 | -2.00% |

Average per day so far: unified Rs +617, benchmark Rs +565, snake_abs_exit Rs +435, snake_abs_exit_conv Rs +385, intramonth Rs +329, intraweek Rs +322, oracle Rs +314, snake_abs_conv Rs +295, snake_abs Rs +290, snake_viper_wild Rs +255, random_hold Rs +189, snake_anaconda Rs +151, snake_viper_tick Rs +144, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -9, snake_nonews Rs -326, snake Rs -347, gold Rs -636

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.