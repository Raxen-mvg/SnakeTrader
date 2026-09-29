"""Stub: imported by quantlab/features.py at the top, never used on SNAKE's scoring path.

The real module needs the production database, which a cloud runner does not have. Anything that
calls into it here is a bug in the release, so it fails loudly instead of quietly.
"""


def _refuse(*_a, **_k):
    raise RuntimeError("fundamentals is a release stub; SNAKE's scoring path must not call it")


fundamentals_asof = _refuse

