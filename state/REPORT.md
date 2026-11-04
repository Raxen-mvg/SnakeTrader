# Paper trading report

Updated 2026-11-04 14:10 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,748 | +7.37% | 0 | - | 236 |
| snake_abs_exit_conv | 214,042 | +7.02% | 1 | 100% | 255 |
| snake_abs_exit | 213,906 | +6.95% | 1 | 100% | 260 |
| snake_abs | 210,927 | +5.46% | 1 | 100% | 255 |
| snake_abs_conv | 210,779 | +5.39% | 1 | 100% | 255 |
| intraweek | 209,984 | +4.99% | 25 | 48% | 2,757 |
| benchmark | 208,216 | +4.11% | 0 | - | 237 |
| snake_viper_wild | 207,686 | +3.84% | 3 | 33% | 702 |
| intramonth | 206,768 | +3.38% | 0 | - | 235 |
| snake_viper_tick | 204,063 | +2.03% | 2 | 0% | 532 |
| random_hold | 203,148 | +1.57% | 8 | 62% | 649 |
| snake_anaconda | 202,533 | +1.27% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,127 | +0.56% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,964 | -2.02% | 0 | - | 237 |
| gold | 191,279 | -4.36% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,809 (-5.10%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,891 | +4.85% |
| snake_abs_exit_conv | +9,703 | +4.75% |
| snake_abs_conv | +9,638 | +4.79% |
| snake_abs | +9,618 | +4.78% |
| snake_anaconda | +8,708 | +4.49% |
| gold | +6,001 | +3.24% |
| intraweek | +4,899 | +2.39% |
| benchmark_smallcap | +3,027 | +1.57% |
| intramonth | +2,797 | +1.37% |
| unified | +2,747 | +1.30% |
| random_hold | +2,680 | +1.34% |
| benchmark | +1,515 | +0.73% |
| oracle | +1,138 | +0.57% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,104 | -1.50% |
| snake_viper_wild | -3,207 | -1.52% |

Average per day so far: snake_abs_exit_conv Rs +585, snake_abs_exit Rs +579, unified Rs +546, snake_abs_conv Rs +449, snake_abs Rs +437, snake_viper_wild Rs +405, intraweek Rs +370, benchmark Rs +304, snake_viper_tick Rs +254, intramonth Rs +251, random_hold Rs +117, snake_anaconda Rs +115, nifty_calls Rs +68, oracle Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -175, gold Rs -323, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.