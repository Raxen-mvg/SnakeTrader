"""SNAKE's network: the supervised autoencoder that won on money in the daily India test.

Architecture borrowed from the published Jane Street Market Prediction solutions: noise on the input,
an encoder to a small bottleneck, a decoder whose reconstruction error stays in the loss, and two
prediction heads - one on the bottleneck alone, one on the raw input alongside it. Every horizon is
predicted at once from one representation, which regularises the fit and yields the whole term
structure a variable-holding rule needs.

Kept separate from training so the live predictor loads exactly the same class.
"""

from __future__ import annotations

HORIZONS = [1, 3, 5, 10, 21, 63]
BOTTLENECK = 24
HIDDEN = 256
NOISE = 0.10
DROPOUT = 0.30


def build(n_features: int, n_targets: int = len(HORIZONS)):
    import torch
    from torch import nn

    class Snake(nn.Module):
        def __init__(self):
            super().__init__()
            self.in_norm = nn.BatchNorm1d(n_features)
            self.encoder = nn.Sequential(
                nn.Linear(n_features, HIDDEN), nn.BatchNorm1d(HIDDEN), nn.SiLU(),
                nn.Linear(HIDDEN, BOTTLENECK), nn.BatchNorm1d(BOTTLENECK), nn.SiLU())
            self.decoder = nn.Sequential(
                nn.Linear(BOTTLENECK, HIDDEN), nn.BatchNorm1d(HIDDEN), nn.SiLU(),
                nn.Linear(HIDDEN, n_features))
            self.head_bottleneck = nn.Sequential(
                nn.Dropout(DROPOUT), nn.Linear(BOTTLENECK, 64), nn.BatchNorm1d(64), nn.SiLU(),
                nn.Dropout(DROPOUT), nn.Linear(64, n_targets))
            self.head_full = nn.Sequential(
                nn.Dropout(DROPOUT), nn.Linear(n_features + BOTTLENECK, HIDDEN),
                nn.BatchNorm1d(HIDDEN), nn.SiLU(),
                nn.Dropout(DROPOUT), nn.Linear(HIDDEN, 128), nn.BatchNorm1d(128), nn.SiLU(),
                nn.Dropout(DROPOUT), nn.Linear(128, n_targets))

        def forward(self, x):
            x = self.in_norm(x)
            xi = x + torch.randn_like(x) * NOISE if self.training else x
            z = self.encoder(xi)
            return self.decoder(z), self.head_bottleneck(z), self.head_full(torch.cat([x, z], 1)), x

        def predict(self, x):
            _, y1, y2, _ = self.forward(x)
            return (y1 + y2) / 2

    return Snake()
