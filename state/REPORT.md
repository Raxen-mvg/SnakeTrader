# Paper trading report

Updated 2026-11-26 12:32 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,216 | +13.11% | 0 | - | 237 |
| unified | 223,471 | +11.73% | 0 | - | 236 |
| oracle | 213,355 | +6.68% | 0 | - | 233 |
| intramonth | 210,668 | +5.33% | 0 | - | 235 |
| random_hold | 209,793 | +4.90% | 13 | 69% | 1,037 |
| intraweek | 208,363 | +4.18% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| snake_abs_exit | 200,273 | +0.14% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,751 | -0.12% | 2 | 50% | 345 |
| snake_abs | 198,172 | -0.91% | 1 | 100% | 255 |
| snake_abs_conv | 197,973 | -1.01% | 1 | 100% | 255 |
| snake_anaconda | 191,958 | -4.02% | 3 | 33% | 374 |
| snake_viper_wild | 191,730 | -4.13% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,476 | -5.76% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,405 | -16.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,853 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,808 | +1.10% |
| benchmark_smallcap | +1,805 | +0.91% |
| intraweek | +1,620 | +0.78% |
| benchmark | +1,193 | +0.53% |
| random_hold | +300 | +0.14% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -440 | -0.21% |
| unified | -629 | -0.28% |
| intramonth | -1,025 | -0.48% |
| snake_abs | -1,978 | -0.99% |
| snake_abs_exit | -1,982 | -0.98% |
| snake_abs_conv | -1,999 | -1.00% |
| snake_abs_exit_conv | -2,224 | -1.10% |
| snake_anaconda | -2,595 | -1.33% |
| snake_viper_tick | -5,701 | -2.94% |
| snake_viper_wild | -5,813 | -2.94% |

Average per day so far: benchmark Rs +639, unified Rs +572, oracle Rs +326, intramonth Rs +260, random_hold Rs +239, intraweek Rs +204, nifty_calls Rs +45, benchmark_smallcap Rs +17, snake_abs_exit Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -7, snake_abs Rs -47, snake_abs_conv Rs -53, snake_anaconda Rs -223, snake_viper_wild Rs -251, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -384, gold Rs -819

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.