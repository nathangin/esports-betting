"""The fitted win model and the model + market blend, as used by the paper trader.

``Params`` is written by ``esalpha backtest`` (``state/params/fitted.json``) from the same
walk-forward run that produced the backtest numbers:

  * Elo K per game (tuned on matches before the first priced match),
  * logistic win model on Elo features (``ratings.model_matrix``), fitted on every result,
  * blend: logistic regression of the result on [logit p_model, logit q_market], fitted on
    every priced match using out-of-sample model probabilities.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from . import ratings as rt


@dataclass
class Params:
    k: dict = field(default_factory=dict)            # game -> Elo K
    win_w: list | None = None                        # intercept + model_matrix columns
    blend_w: list | None = None                      # intercept, logit p_model, logit q
    meta: dict = field(default_factory=dict)

    def elo_configs(self) -> dict:
        return {g: rt.EloConfig(k=float(v)) for g, v in self.k.items()}

    def p_model(self, feats: pd.DataFrame) -> np.ndarray:
        if self.win_w is None:
            return feats["p_elo"].to_numpy(dtype=float)
        return rt.predict_logistic(np.asarray(self.win_w, dtype=float), rt.model_matrix(feats))

    def p_blend(self, p_model, q) -> np.ndarray | None:
        if self.blend_w is None:
            return None
        X = np.column_stack([rt.logit(np.atleast_1d(p_model)), rt.logit(np.atleast_1d(q))])
        return rt.predict_logistic(np.asarray(self.blend_w, dtype=float), X)

    @property
    def version(self) -> str:
        return str(self.meta.get("fitted", "defaults"))[:16]

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(asdict(self), indent=1, default=str))

    @classmethod
    def load(cls, path: str | Path) -> "Params":
        p = Path(path)
        if not p.exists():
            return cls()
        d = json.loads(p.read_text())
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})
