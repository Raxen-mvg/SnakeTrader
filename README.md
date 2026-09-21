# Oracle paper trader

Every strategy trades its own Rs 50,000 of fake money at live (slightly delayed) NSE prices,
paying Zerodha's published charges on every order. Runs on GitHub Actions every 15 minutes
during market hours, so it keeps going when the research machine is off.

## Strategies

| Account | Rule |
|---|---|
| intraday | Top 5 model picks bought after 09:30, sold after 15:05 |
| intraweek | Top 5 held for 5 trading days |
| intramonth | Top 5; a name is kept while the model ranks it in its top 25% |
| random_hold | Top 5, each held a random 2-40 trading days (control) |
| gold | GOLDBEES held |
| gold_trend | GOLDBEES only while above its 200-day average |
| nifty_calls | SIMULATED: one ATM Nifty call Monday to Thursday, Black-Scholes priced |
| benchmark | NIFTYBEES held; every strategy must beat this |

A virtual combined account re-weights across strategies by recent risk-adjusted return.

## Data for a frontend or backend

All in `state/`, updated every tick:

| File | Contents |
|---|---|
| `summary.json` | Per strategy: equity, return %, cash, open positions, closed trades, win rate, costs paid; plus the combined account |
| `trades.csv` | Every order: time, strategy, side, symbol, qty, fill price, value, costs, product, realised P&L, reason |
| `equity.csv` | Equity per strategy at every tick |
| `combined.csv` | Combined account equity and daily weights |
| `REPORT.md` | Human-readable table |
| `picks_IN.json` | Current model picks (pushed from the research machine) |
| `accounts.json` | Full account state (source of truth) |

Raw file URLs from this repo (or the GitHub contents API) are enough for a frontend; a backend can
poll `summary.json`.

## Manual run

`python -m papertrade.engine --force` acts regardless of market hours. In GitHub: Actions,
paper-trade, Run workflow, tick "force".

## Honest limits

- Prices come from a free delayed feed; fills add slippage (0.15% stocks, 0.05% ETFs, 0.5% options).
- Option trades are simulated from the real Nifty level and realised volatility, not real option quotes.
- Futures are excluded: Rs 50,000 cannot margin one Nifty lot.
- If new picks are not pushed, strategies keep trading on the last picks.
