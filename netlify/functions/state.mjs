// Serves the latest paper-trading state from this repository on GitHub.
// Only an explicit allow-list of files can be read, so the function cannot be used to fetch
// anything else from the repository.
const REPO = "Raxen-mvg/SnakeTrader";
const BRANCH = "main";
const ALLOWED = {
  "summary.json": "application/json",
  "picks_snake.json": "application/json",
  "picks_snake_nonews.json": "application/json",
  "picks_snake_abs.json": "application/json",
  "trades.csv": "text/csv",
  "daily_profit.csv": "text/csv",
};

export default async (req) => {
  const file = new URL(req.url).searchParams.get("f") || "";
  if (!(file in ALLOWED)) {
    return new Response("unknown file", { status: 400 });
  }
  const headers = {
    Accept: "application/vnd.github.raw+json",
    "User-Agent": "paper-trader-dashboard",
  };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  const url = `https://api.github.com/repos/${REPO}/contents/state/${file}?ref=${BRANCH}`;
  const r = await fetch(url, { headers });
  const body = await r.text();
  return new Response(body, {
    status: r.status,
    headers: { "content-type": ALLOWED[file], "cache-control": "public, max-age=60" },
  });
};
