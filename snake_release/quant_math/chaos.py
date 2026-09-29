"""Nonlinear dynamics and complexity measures for return series.

Honest framing first. The strong claim — that markets are low-dimensional
deterministic chaos — has largely failed testing: correlation-dimension and
Lyapunov estimates on financial data are dominated by noise, and most careful
studies (Hsieh 1991; Brock, Hsieh & LeBaron 1991) find nonlinear dependence in
VOLATILITY rather than a forecastable attractor in returns. Lyapunov exponents
on daily equity returns are not trustworthy and are deliberately not used here
as a signal.

The weak claim is the useful one: measures built for chaotic systems quantify
structure that mean, variance and autocorrelation miss — how predictable a
series is, how persistent, how much it repeats itself. Those work as features
whether or not the underlying process is truly chaotic, and each is cheap to
compute on a rolling window.

Implemented:
  permutation_entropy   - Bandt & Pompe (2002). Ordinal-pattern complexity.
                          Low = predictable structure, high = noise.
  sample_entropy        - Richman & Moorman (2000). Regularity, robust to
                          series length; low = repeating patterns.
  dfa_alpha             - Detrended fluctuation analysis (Peng et al. 1994).
                          Long-memory exponent; 0.5 = random walk increments,
                          >0.5 persistent, <0.5 mean-reverting.
  recurrence_rate       - Fraction of revisited states in a reconstructed
                          phase space (Takens embedding), the base measure of
                          recurrence quantification analysis.
  lempel_ziv_complexity - Compressibility of the sign sequence; a
                          distribution-free measure of randomness.

All functions take a 1-D return series and return a scalar, with NaN when the
window is too short to be meaningful.
"""

from __future__ import annotations

import math

import numpy as np

__all__ = ["permutation_entropy", "sample_entropy", "dfa_alpha",
           "recurrence_rate", "lempel_ziv_complexity", "rolling_apply"]


def _clean(x) -> np.ndarray:
    a = np.asarray(x, dtype=float)
    return a[np.isfinite(a)]


def permutation_entropy(x, order: int = 3, delay: int = 1,
                        normalize: bool = True) -> float:
    """Shannon entropy of ordinal patterns (Bandt & Pompe 2002).

    Each window of `order` points is replaced by the permutation that sorts it,
    so the measure depends only on the ORDER of values, making it immune to
    monotonic transformations and to outliers — useful on fat-tailed returns.
    Returns 0 for a perfectly ordered series and 1 (normalised) for noise.
    """
    a = _clean(x)
    n = len(a) - delay * (order - 1)
    if n < order + 1:
        return np.nan
    idx = np.arange(order) * delay
    windows = np.lib.stride_tricks.sliding_window_view(a, delay * (order - 1) + 1)[:, idx]
    patterns = np.argsort(windows, axis=1, kind="stable")
    # Encode each permutation as an integer for counting.
    weights = order ** np.arange(order)
    codes = patterns @ weights
    _, counts = np.unique(codes, return_counts=True)
    p = counts / counts.sum()
    h = -np.sum(p * np.log(p))
    if normalize:
        h /= np.log(math.factorial(order))
    return float(h)


def sample_entropy(x, m: int = 2, r: float | None = None) -> float:
    """Negative log conditional probability that similar patterns stay similar.

    Lower = more regular/repeating. `r` defaults to 0.2 standard deviations,
    the convention in the literature. O(n^2), so keep windows modest.
    """
    a = _clean(x)
    n = len(a)
    if n < m + 2:
        return np.nan
    sd = a.std()
    if sd == 0:
        return np.nan
    tol = 0.2 * sd if r is None else r * sd

    def _count(k: int) -> int:
        blocks = np.lib.stride_tricks.sliding_window_view(a, k)
        # Chebyshev distance between every pair of blocks, excluding self-pairs.
        d = np.abs(blocks[:, None, :] - blocks[None, :, :]).max(axis=2)
        np.fill_diagonal(d, np.inf)
        return int((d <= tol).sum())

    b = _count(m)
    c = _count(m + 1)
    if b == 0 or c == 0:
        return np.nan
    return float(-np.log(c / b))


def dfa_alpha(x, scales: tuple[int, ...] = (8, 16, 32, 64)) -> float:
    """Detrended fluctuation analysis exponent (Peng et al. 1994).

    Integrates the series, then measures how the residual fluctuation after
    removing a local linear trend grows with window size. The slope on a
    log-log plot is alpha: 0.5 for an uncorrelated series, above 0.5 for
    persistent (trending) behaviour, below for mean-reverting. More robust to
    non-stationarity than the classical rescaled-range Hurst estimate.
    """
    a = _clean(x)
    usable = [s for s in scales if len(a) >= 4 * s]
    if len(usable) < 3:
        return np.nan
    y = np.cumsum(a - a.mean())
    fluct = []
    for s in usable:
        n_seg = len(y) // s
        seg = y[: n_seg * s].reshape(n_seg, s)
        t = np.arange(s)
        # Least-squares linear detrend of every segment at once.
        tm, ym = t.mean(), seg.mean(axis=1, keepdims=True)
        slope = ((t - tm) * (seg - ym)).sum(axis=1) / ((t - tm) ** 2).sum()
        trend = ym + slope[:, None] * (t - tm)
        fluct.append(np.sqrt(((seg - trend) ** 2).mean()))
    f = np.asarray(fluct)
    ok = f > 0
    if ok.sum() < 3:
        return np.nan
    return float(np.polyfit(np.log(np.asarray(usable)[ok]), np.log(f[ok]), 1)[0])


def recurrence_rate(x, dim: int = 3, delay: int = 1,
                    threshold: float = 0.2) -> float:
    """Fraction of pairs of states that recur in a Takens-embedded phase space.

    The series is embedded into `dim` dimensions and two states count as
    recurrent when their distance is within `threshold` standard deviations.
    A high rate means the series revisits similar configurations — the
    signature chaotic systems leave and pure noise does not.
    """
    a = _clean(x)
    span = delay * (dim - 1)
    if len(a) < span + 10:
        return np.nan
    sd = a.std()
    if sd == 0:
        return np.nan
    emb = np.lib.stride_tricks.sliding_window_view(a, span + 1)[:, ::delay]
    d = np.linalg.norm(emb[:, None, :] - emb[None, :, :], axis=2)
    np.fill_diagonal(d, np.inf)
    return float((d <= threshold * sd * np.sqrt(dim)).mean())


def lempel_ziv_complexity(x) -> float:
    """Compressibility of the sign sequence, normalised to [0, 1] roughly.

    Counts distinct substrings needed to build the binary up/down sequence.
    A trending or alternating series compresses well (low value); a random
    one does not (near 1). Distribution-free, so fat tails do not distort it.
    """
    a = _clean(x)
    if len(a) < 20:
        return np.nan
    s = (a > 0).astype(np.uint8)
    n = len(s)
    i, k, l, c, k_max = 0, 1, 1, 1, 1
    while True:
        if s[i + k - 1] == s[l + k - 1]:
            k += 1
            if l + k > n:
                c += 1
                break
        else:
            k_max = max(k_max, k)
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    break
                i, k, k_max = 0, 1, 1
            else:
                k = 1
    return float(c * np.log2(n) / n)


def ordinal_codes(x, order: int = 4, delay: int = 1) -> np.ndarray:
    """Ordinal-pattern code for every position, vectorised.

    Computed once per series so a rolling entropy only has to count codes in a
    window instead of re-sorting it. Returns an array aligned to the END of
    each pattern, with the first delay*(order-1) entries set to -1.
    """
    a = np.asarray(x, dtype=float)
    span = delay * (order - 1)
    if len(a) <= span:
        return np.full(len(a), -1, dtype=np.int64)
    windows = np.lib.stride_tricks.sliding_window_view(a, span + 1)[:, ::delay]
    patterns = np.argsort(windows, axis=1, kind="stable")
    codes = patterns @ (order ** np.arange(order))
    bad = ~np.isfinite(windows).all(axis=1)
    codes[bad] = -1
    return np.concatenate([np.full(span, -1, dtype=np.int64), codes])


def rolling_permutation_entropy(x, window: int = 252, order: int = 4,
                                min_periods: int = 120) -> np.ndarray:
    """Permutation entropy over a trailing window, for every position.

    Uses precomputed ordinal codes and a running histogram, so the whole
    series costs one pass instead of one sort per window. The value at index i
    uses only data up to and including i.
    """
    codes = ordinal_codes(x, order=order)
    n_codes = order ** order
    counts = np.zeros(n_codes, dtype=np.int64)
    out = np.full(len(codes), np.nan)
    norm = np.log(math.factorial(order))
    valid = 0
    for i, c in enumerate(codes):
        if c >= 0:
            counts[c] += 1
            valid += 1
        if i >= window:
            old = codes[i - window]
            if old >= 0:
                counts[old] -= 1
                valid -= 1
        if valid >= min_periods:
            p = counts[counts > 0] / valid
            out[i] = -np.sum(p * np.log(p)) / norm
    return out


def rolling_apply(series, func, window: int, min_periods: int | None = None,
                  step: int = 1, **kwargs):
    """Apply a scalar complexity measure over a rolling window.

    `step` evaluates only every step-th point and forward-fills between, which
    matters because sample entropy and recurrence rate are O(n^2) per window.
    """
    import pandas as pd

    s = pd.Series(series).astype(float)
    min_periods = min_periods or window
    out = pd.Series(np.nan, index=s.index, dtype=float)
    positions = range(min_periods - 1, len(s), step)
    for i in positions:
        w = s.iloc[max(0, i - window + 1): i + 1].to_numpy()
        if np.isfinite(w).sum() >= min_periods:
            out.iloc[i] = func(w, **kwargs)
    return out.ffill() if step > 1 else out
