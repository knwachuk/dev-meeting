from dataclasses import dataclass, field

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


@dataclass
class StreamProcessor:
    """StreamProcessor"""

    frame_store: list = field(default_factory=list)
    frame_gray_store: list = field(default_factory=list)
    frame_hist_store: list = field(default_factory=list)
    frame_intensity_store: list = field(default_factory=list)

    frame_count: int = None

    events: list = field(default_factory=list)
    uri: str = None
    fps: int = 24


def truth_viz(
    perceived_truth, ground_truth=None, spacing=5, ratio=1 / 5, offset=10, image=False
):

    cat_pos = {
        cat: (i * 3) + 2
        for i, cat in enumerate(perceived_truth["Category Tag"].unique())
    }

    x = np.linspace(
        1,
        int(perceived_truth["Time (Seconds)"].max()),
        int(perceived_truth["Time (Seconds)"].max() / spacing),
    )
