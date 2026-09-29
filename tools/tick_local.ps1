# Laptop clock for the paper trader (GitHub's scheduler skips many runs, so this is the main one
# whenever the laptop is on). Pull, export fresh picks, tick, push. The engine skips a tick if
# GitHub Actions ticked in the last 10 minutes, so the two never double-trade.
$py = "C:\Projects\StockTradesModel\.venv\Scripts\python.exe"
Set-Location C:\Projects\oracle-paper-trader
$log = "C:\Projects\StockTradesModel\logs\paper_trader.log"
git pull -q --rebase 2>&1 | Out-Null
& $py tools\export_picks.py --out state\picks_IN.json *>> $log
$now = Get-Date
if ($now.DayOfWeek -notin 'Saturday','Sunday' -and $now.TimeOfDay -ge [TimeSpan]'09:14' -and $now.TimeOfDay -le [TimeSpan]'15:35') {
    & $py -m papertrade.engine *>> $log
}
git add state
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git -c user.name="Saksham Maheshwari" -c user.email="rockboy5431@gmail.com" commit -q -m "tick $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    for ($i = 0; $i -lt 3; $i++) {
        git push -q 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) { break }
        git pull -q --rebase -X theirs 2>&1 | Out-Null
    }
}
