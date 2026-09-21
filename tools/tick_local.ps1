# Laptop side: push fresh model picks to the repo. GitHub Actions does the trading,
# so this never ticks the engine (two writers would conflict on accounts.json).
$py = "C:\Projects\StockTradesModel\.venv\Scripts\python.exe"
Set-Location C:\Projects\oracle-paper-trader
$log = "C:\Projects\StockTradesModel\logs\paper_trader.log"
git pull -q --rebase 2>&1 | Out-Null
& $py tools\export_picks.py --out state\picks_IN.json *>> $log
git add state\picks_IN.json state\intraday_model.txt state\intraday_universe.json 2>$null
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git -c user.name="Saksham Maheshwari" -c user.email="clearaedu@gmail.com" commit -q -m "picks $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git push -q 2>&1 | Out-Null
}
