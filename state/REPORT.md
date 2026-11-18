# Paper trading report

Updated 2026-11-18 10:13 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,644 | +11.32% | 0 | - | 236 |
| benchmark | 220,678 | +10.34% | 0 | - | 237 |
| intraweek | 214,592 | +7.30% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,692 | +6.35% | 2 | 50% | 345 |
| intramonth | 212,519 | +6.26% | 0 | - | 235 |
| oracle | 212,386 | +6.19% | 0 | - | 233 |
| snake_abs_exit_conv | 211,003 | +5.50% | 2 | 50% | 345 |
| snake_abs | 208,254 | +4.13% | 1 | 100% | 255 |
| snake_abs_conv | 208,101 | +4.05% | 1 | 100% | 255 |
| random_hold | 207,556 | +3.78% | 10 | 70% | 733 |
| snake_viper_wild | 207,089 | +3.54% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,551 | +1.78% | 15 | 47% | 2,625 |
| snake_anaconda | 203,152 | +1.58% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,321 | -11.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,541 (-4.23%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,270 | +0.59% |
| unified | +1,206 | +0.54% |
| intramonth | +977 | +0.46% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -100 | -0.05% |
| snake_abs | -304 | -0.15% |
| snake_abs_conv | -319 | -0.15% |
| benchmark_smallcap | -348 | -0.17% |
| snake_abs_exit | -450 | -0.21% |
| snake_abs_exit_conv | -570 | -0.27% |
| random_hold | -876 | -0.42% |
| snake_anaconda | -903 | -0.44% |
| benchmark | -926 | -0.42% |
| snake_viper_tick | -2,285 | -1.11% |
| snake_viper_wild | -2,326 | -1.11% |
| gold | -3,403 | -1.88% |

Average per day so far: unified Rs +629, benchmark Rs +574, intraweek Rs +405, snake_abs_exit Rs +385, intramonth Rs +348, oracle Rs +344, snake_abs_exit_conv Rs +333, snake_viper_wild Rs +253, snake_abs_conv Rs +245, snake_abs Rs +243, random_hold Rs +210, snake_viper_tick Rs +142, snake_anaconda Rs +102, nifty_calls Rs +51, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.