# SnakeTrader

Every strategy trades its own ₹2,00,000 of fake money at live NSE prices, paying Zerodha's
published charges on every order: transaction tax, stamp duty, exchange and SEBI fees, GST, the
flat depository charge on every sale, and slippage. It runs from two clocks — the research laptop
during market hours, and GitHub Actions — so it keeps going when the laptop is off.

## Accounts

| Account | Rule |
|---|---|
| **snake** | **SNAKE with news**: the deep multi-horizon model with NSE announcement features, trained on 2010 onward. Buys only what it expects to beat its own round trip; keeps a holding only while it still expects to beat the cost of selling it. Holding period is whatever the model says. |
| **snake_abs** | **SNAKE absolute return**: the same trading rule, with a network trained to predict each stock's own return (not its rank against the others), with NSE news, the results calendar (announced board meetings, past results reactions, peers' reactions) and market state as inputs. Backtest 2013–2026: Rs 2 lakh became Rs 63.8 and Rs 71.5 lakh on two seed pairs, with worst drawdowns near −44%. Live from 30 September 2026. |
| **snake_abs_conv** | **SNAKE absolute return, conviction-staked**: the same picks as snake_abs, but each new buy is staked by conviction - the equal share times (its expected return / the book's average) squared, between 0.5x and 1.6x, never above 30% of the account. Backtest 2013–2026: Rs 2 lakh became Rs 1.24 and 1.62 crore on two seed pairs against Rs 63.8 and 71.5 lakh equal-staked, with worst drawdowns near −50%. Live from 1 October 2026. |
| **snake_abs_exit** | **VIPER** - SNAKE absolute return with a trained exit: the same picks as snake_abs, but it also sells when SNAKE's exit model says switching to the best fresh names beats holding by more than 2% over the next ten sessions, after the cost of switching (never in a holding's first ten sessions). The exit model learned hold-versus-switch from 800,000 hypothetical positions since 2013 (gain since entry, best gain and the fall from it, age, expected return at entry and now, ranks, market state). Backtest on an exact next-close clock, Rs 2 lakh from 2013: Rs 1.91 and 2.39 crore on two seed pairs, against Rs 56.7 and 51.9 lakh holding until the expected return fades. Live from 1 October 2026. |
| **snake_abs_exit_conv** | **VIPER CONVICTION** - the Viper above, with conviction stakes as in snake_abs_conv. |
| **snake_nonews** | **SNAKE without news**: the same network and the same trading rule, trained on the full price history without announcements. The two run side by side until December 2026 to see which makes more money. |
| oracle | The production model. Money goes to whatever is expected to earn most per day net of costs; nothing is bought below its cost. |
| unified | The production model's top names, sized by rank |
| intraweek | Top 5 held for 5 trading days |
| intramonth | Top 5; a name is kept while the model ranks it in its top 25% |
| random_hold | Top 5, each held a random 2–40 trading days (control) |
| intraday | Same-day trades, gated on a calibrated expected edge (rarely trades, by design) |
| statarb | Market-neutral reversion sleeve (currently switched off) |
| gold | GOLDBEES held |
| gold_trend | GOLDBEES only while above its 200-day average |
| nifty_calls | SIMULATED: one at-the-money Nifty call, Black-Scholes priced |
| benchmark | NIFTYBEES held; every strategy must beat this |

## Where picks come from

- **Oracle** picks (`state/picks_IN.json`) are exported from the research machine's nightly
  snapshot.
- **SNAKE** picks (`state/picks_snake.json` with news, `state/picks_snake_nonews.json` without)
  come from either clock:
  - the laptop, each morning, after refreshing a fortnight of NSE announcements;
  - the `snake-daily` workflow on GitHub Actions, after the close and again before the open, from
    the model release in `snake_release/`. It fetches prices from Yahoo and a year of
    announcements from NSE, computes the same features with the same code, and commits the picks.
    If the laptop already wrote picks for the latest session, it stops at once.

`snake_release/` holds both SNAKE models' weights (`model/` with news, `model_nonews/` without,
about a megabyte each), their feature lists and calibration, the
universe it scores, and its code with the production feature modules copied verbatim, so cloud
features cannot drift from training. The research machine republishes it whenever SNAKE is
retrained. No price data is ever committed.

## Dashboard

`site/` is a static dashboard showing every account, SNAKE's current top names with expected return
and horizon, and recent trades with the reason for each. It reads state through a Netlify function
(`netlify/functions/state.mjs`) that fetches an allow-list of files from this repository, so the
site never needs rebuilding when the accounts change.

To deploy on Netlify (free tier):

1. In Netlify: **Add new site → Import an existing project → GitHub**, and pick **SnakeTrader**.
   Build settings come from `netlify.toml`; leave them as they are.
2. While this repository is private, create a fine-grained GitHub token with **read-only access to
   this repository's Contents**, and add it in Netlify under **Site configuration → Environment
   variables** as `GITHUB_TOKEN`. Once the repository is public this step is unnecessary.

To check the page locally: `python tools/dashboard_dev.py`, then open `http://127.0.0.1:8765`.

## State files

All in `state/`:

| File | Contents |
|---|---|
| `summary.json` | Per strategy: equity, return %, cash, open positions, closed trades, win rate, costs paid; plus the combined account |
| `trades.csv` | Every order: time, strategy, side, symbol, quantity, fill price, value, costs, product, reason |
| `equity.csv` | Equity per strategy at every tick |
| `daily_profit.csv` | Profit per strategy per day |
| `picks_IN.json` | The production model's current picks |
| `picks_snake.json` | SNAKE with news: every scored name's expected return and best horizon |
| `picks_snake_nonews.json` | SNAKE without news, same format |
| `picks_snake_abs.json` | SNAKE absolute return, same format |
| `accounts.json` | Full account state (source of truth) |

## Manual runs

- `python -m papertrade.engine --force` acts regardless of market hours. On GitHub: **Actions →
  paper-trade → Run workflow**, tick *force*.
- **Actions → snake-daily → Run workflow** recomputes both SNAKE picks files in the cloud now.

Tests: `python tests/test_papertrade.py`, `python tests/test_oracle_account.py`,
`python tests/test_snake_account.py`.

## Honest limits

- Prices come from a free feed; fills add slippage (0.15% stocks, 0.05% ETFs, 0.5% options).
- Option trades are simulated from the real Nifty level and realised volatility, not real quotes.
- GitHub starts scheduled workflows late and sometimes skips them, so with the laptop off the
  accounts may tick only a few times a day. SNAKE decides once a day, so it is least affected.
- If picks go stale, strategies keep trading on the last ones; SNAKE stops buying and stops
  selling on its model's say-so once its picks are more than four days old, keeping only its
  disaster stop.
- Nothing here is investment advice.
