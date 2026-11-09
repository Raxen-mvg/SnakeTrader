# Paper trading report

Updated 2026-11-09 14:40 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,809 | +9.90% | 0 | - | 236 |
| benchmark | 217,870 | +8.94% | 0 | - | 237 |
| intraweek | 214,255 | +7.13% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,607 | +6.30% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,392 | +6.20% | 2 | 50% | 330 |
| snake_abs | 209,976 | +4.99% | 1 | 100% | 255 |
| snake_abs_conv | 209,808 | +4.90% | 1 | 100% | 255 |
| intramonth | 209,607 | +4.80% | 0 | - | 235 |
| oracle | 209,034 | +4.52% | 0 | - | 233 |
| random_hold | 204,361 | +2.18% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 200,019 | +0.01% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,060 | -0.97% | 0 | - | 237 |
| snake_viper_wild | 197,571 | -1.21% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,218 | -2.89% | 6 | 50% | 1,154 |
| gold | 192,101 | -3.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,079 (-4.96%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,581 | +2.23% |
| snake_abs | +4,557 | +2.22% |
| snake_abs_exit | +4,295 | +2.06% |
| unified | +4,200 | +1.95% |
| snake_anaconda | +4,192 | +2.14% |
| snake_abs_exit_conv | +3,970 | +1.91% |
| intraweek | +3,893 | +1.85% |
| oracle | +3,207 | +1.56% |
| intramonth | +2,004 | +0.96% |
| snake_viper_wild | +1,534 | +0.78% |
| snake_viper_tick | +1,508 | +0.78% |
| benchmark_smallcap | +1,267 | +0.64% |
| gold | +1,052 | +0.55% |
| random_hold | +455 | +0.22% |
| benchmark | +382 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +660, benchmark Rs +596, intraweek Rs +475, snake_abs_exit Rs +467, snake_abs_exit_conv Rs +459, snake_abs_conv Rs +363, snake_abs Rs +356, intramonth Rs +320, oracle Rs +301, random_hold Rs +145, nifty_calls Rs +61, snake_anaconda Rs +1, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -75, snake_viper_wild Rs -110, gold Rs -263, snake_viper_tick Rs -304, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.