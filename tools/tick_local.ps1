# Laptop clock for the paper trader (GitHub's scheduler skips many runs, so this is the main one
# whenever the laptop is on). Pull, export fresh picks, tick, push. The engine skips a tick if
# GitHub Actions ticked in the last 10 minutes, so the two never double-trade.
$py = "C:\Projects\StockTradesModel\.venv\Scripts\python.exe"
Set-Location C:\Projects\oracle-paper-trader
$log = "C:\Projects\StockTradesModel\logs\paper_trader.log"
# GitHub's state is the truth. A pull that hit a conflict once left a rebase half done, and later
# runs committed files with conflict markers in them (2026-10-07). So start every run from GitHub's
# latest state, as the cloud runner does: a laptop tick that lost the race to the cloud is dropped.
# Unpushed commits that touch anything outside state/ (code) are never dropped: stand down instead.
function Rebasing { (Test-Path .git\rebase-merge) -or (Test-Path .git\rebase-apply) }
if (Rebasing) { git rebase --abort 2>&1 | Out-Null }
git fetch -q origin main 2>&1 | Out-Null
$code = git diff --name-only origin/main...HEAD | Where-Object { $_ -notlike 'state/*' }
if ($code) {
    "$(Get-Date -Format s) unpushed code commits on the laptop ($($code -join ', ')); not ticking" | Out-File -Append -Encoding utf8 $log
    exit 1
}
git checkout -q -- state 2>&1 | Out-Null
git reset -q --keep origin/main 2>&1 | Out-Null
& $py tools\export_picks.py --out state\picks_IN.json *>> $log
$now = Get-Date
# GitHub's own schedule starts hours late or not at all, and this laptop drops into standby when idle.
# So whenever it is awake in market hours it makes sure a cloud session is running: one wake covers
# the rest of the day even if the laptop sleeps again straight after.
if ($now.DayOfWeek -notin 'Saturday','Sunday' -and $now.TimeOfDay -ge [TimeSpan]'09:00' -and $now.TimeOfDay -le [TimeSpan]'15:00') {
    $runs = gh run list --workflow papertrade.yml -L 5 --json status 2>$null | ConvertFrom-Json
    if ($runs -and -not ($runs | Where-Object { $_.status -in 'in_progress', 'queued', 'waiting', 'pending' })) {
        gh workflow run papertrade.yml 2>&1 | Out-Null
        "$(Get-Date -Format s) no cloud session running; started one" | Out-File -Append -Encoding utf8 $log
    }
}
# From 16:00 the engine values every account at the official close instead of trading (once a day).
if ($now.DayOfWeek -notin 'Saturday','Sunday' -and (($now.TimeOfDay -ge [TimeSpan]'09:14' -and $now.TimeOfDay -le [TimeSpan]'15:35') -or $now.TimeOfDay -ge [TimeSpan]'16:00')) {
    & $py -m papertrade.engine *>> $log
}
git add state
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git -c user.name="Saksham Maheshwari" -c user.email="rockboy5431@gmail.com" commit -q -m "tick $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    # If the cloud pushed first this tick is dropped at the start of the next run.
    git push -q 2>&1 | Out-Null
}
