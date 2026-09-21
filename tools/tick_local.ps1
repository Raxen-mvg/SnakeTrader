# Local fallback for the GitHub Actions workflow: export fresh picks, run one tick, push state.
$py = "C:\Projects\StockTradesModel\.venv\Scripts\python.exe"
Set-Location C:\Projects\oracle-paper-trader
$log = "C:\Projects\StockTradesModel\logs\paper_trader.log"
$now = Get-Date
if ($now.DayOfWeek -in 'Saturday','Sunday' -or $now.TimeOfDay -lt [TimeSpan]'09:14' -or $now.TimeOfDay -gt [TimeSpan]'15:35') { exit 0 }
git pull -q --rebase 2>&1 | Out-Null
& $py tools\export_picks.py --out state\picks_IN.json *>> $log
& $py -m papertrade.engine *>> $log
git add state
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git -c user.name="Saksham Maheshwari" -c user.email="clearaedu@gmail.com" commit -q -m "tick $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git push -q 2>&1 | Out-Null
}
