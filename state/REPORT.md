# Paper trading report

Updated 2026-11-26 14:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,140 | +13.07% | 0 | - | 237 |
| unified | 223,090 | +11.54% | 0 | - | 236 |
| oracle | 212,762 | +6.38% | 0 | - | 233 |
| intramonth | 210,435 | +5.22% | 0 | - | 235 |
| random_hold | 208,941 | +4.47% | 13 | 69% | 1,037 |
| intraweek | 207,527 | +3.76% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,840 | +0.42% | 0 | - | 237 |
| snake_abs_exit | 200,327 | +0.16% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,696 | -0.15% | 2 | 50% | 345 |
| snake_abs | 197,967 | -1.02% | 1 | 100% | 255 |
| snake_abs_conv | 197,759 | -1.12% | 1 | 100% | 255 |
| snake_viper_wild | 192,302 | -3.85% | 16 | 50% | 2,827 |
| snake_anaconda | 191,638 | -4.18% | 3 | 33% | 374 |
| snake_viper_tick | 189,035 | -5.48% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,142 | -16.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,442 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,029 | +1.02% |
| gold | +1,545 | +0.94% |
| benchmark | +1,117 | +0.50% |
| intraweek | +784 | +0.38% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -552 | -0.26% |
| unified | -1,010 | -0.45% |
| oracle | -1,033 | -0.48% |
| intramonth | -1,258 | -0.59% |
| snake_abs_exit | -1,929 | -0.95% |
| snake_abs | -2,183 | -1.09% |
| snake_abs_conv | -2,213 | -1.11% |
| snake_abs_exit_conv | -2,280 | -1.13% |
| snake_anaconda | -2,915 | -1.50% |
| snake_viper_tick | -5,142 | -2.65% |
| snake_viper_wild | -5,242 | -2.65% |

Average per day so far: benchmark Rs +638, unified Rs +563, oracle Rs +311, intramonth Rs +255, random_hold Rs +218, intraweek Rs +184, nifty_calls Rs +45, benchmark_smallcap Rs +23, snake_abs_exit Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -8, snake_abs Rs -52, snake_abs_conv Rs -59, snake_anaconda Rs -232, snake_viper_wild Rs -233, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -365, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.