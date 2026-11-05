# Paper trading report

Updated 2026-11-05 12:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,947 | +8.97% | 0 | - | 236 |
| snake_abs_exit_conv | 213,643 | +6.82% | 1 | 100% | 255 |
| snake_abs_exit | 213,345 | +6.67% | 1 | 100% | 260 |
| benchmark | 212,951 | +6.48% | 0 | - | 237 |
| intraweek | 211,528 | +5.76% | 25 | 48% | 2,757 |
| snake_abs | 210,530 | +5.26% | 1 | 100% | 255 |
| snake_abs_conv | 210,395 | +5.20% | 1 | 100% | 255 |
| intramonth | 209,692 | +4.85% | 0 | - | 235 |
| snake_viper_wild | 206,537 | +3.27% | 3 | 33% | 702 |
| random_hold | 206,478 | +3.24% | 8 | 62% | 649 |
| oracle | 203,969 | +1.98% | 0 | - | 233 |
| snake_viper_tick | 202,985 | +1.49% | 2 | 0% | 532 |
| snake_anaconda | 201,841 | +0.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| gold | 194,024 | -2.99% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,051 (-4.97%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,192 | +2.01% |
| unified | +3,507 | +1.64% |
| random_hold | +3,169 | +1.56% |
| intramonth | +2,677 | +1.29% |
| gold | +2,630 | +1.37% |
| benchmark_smallcap | +2,377 | +1.21% |
| oracle | +2,177 | +1.08% |
| intraweek | +1,830 | +0.87% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,364 | -0.64% |
| snake_abs_exit_conv | -1,372 | -0.64% |
| snake_abs | -1,373 | -0.65% |
| snake_abs_exit | -1,555 | -0.72% |
| snake_anaconda | -1,979 | -0.97% |
| snake_viper_tick | -2,416 | -1.18% |
| snake_viper_wild | -2,493 | -1.19% |

Average per day so far: unified Rs +641, snake_abs_exit_conv Rs +546, snake_abs_exit Rs +534, benchmark Rs +463, snake_abs_conv Rs +416, intraweek Rs +412, snake_abs Rs +405, intramonth Rs +346, snake_viper_wild Rs +327, random_hold Rs +231, snake_viper_tick Rs +176, oracle Rs +142, snake_anaconda Rs +80, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -213, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.