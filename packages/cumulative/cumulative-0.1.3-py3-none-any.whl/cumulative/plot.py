import matplotlib
import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from cumulative.options import options


def supersmooth(x, k=0.5):
    # useful to zoom-in (acceleration) close to 0 and 1 (tending to constant velocity at x=.5)
    # [0,1] -> [0,1]
    # k equal to .0: linear output, no transformation (no acceleration)
    # k equal to .5: sinusoidal curve
    # k close to 1: mostly at .5 (max acceleration close to 0 and 1)

    k = max(k, 0)
    k = min(k, 1 - 1e-5)

    if k == 0:
        return x

    a = 2
    b = -1
    c = 0.5
    d = 0.5
    y = (1 - k) * (a * x + b) / (k - 2 * k * np.abs(a * x + b) + 1) * c + d
    return y


class Figure:
    def __init__(self, x_label="X", y_label="Y", ioff=False):
        mpl.rcParams.update(mpl.rcParamsDefault)
        plt.rcParams["font.family"] = "monospace"
        cmap = matplotlib.colormaps["cool"]

        if ioff:
            plt.ioff()
        else:
            plt.ion()

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.clear()
        ax.set_facecolor("black")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        lim_pad = 0.05
        ax.set_xlim(0 - lim_pad, 1 + lim_pad)
        ax.set_ylim(0 - lim_pad, 1 + lim_pad)

        self.fig = fig
        self.ax = ax
        self.cmap = cmap


class Plot:
    def __init__(self, c):
        self.c = c

    def xrays(self, src=None, figure=None, show=True, alpha=1, ms=1, lw=1, k=60, style="."):
        src = options().default_if_null(src, "transforms.source")
        tmp = options().get("transforms.tmp")
        with options().option_context({"transforms": {"source": tmp, "destination": tmp}}):
            self.c.fit(src=src, method="pchip3", k=k, n_samples=k)
            self.c.plot.scatter(figure=figure, show=show, alpha=alpha, ms=ms, lw=lw, style=style)
            self.c.drop()

    def heatmap(
        self, src=None, figure=None, show=True, ms=4, lw=1, k=60, score="idx", alpha=1, alpha_score=False, style="."
    ):
        src = options().default_if_null(src, "transforms.source")
        tmp = options().get("transforms.tmp")
        tmp_score = f"{tmp}.score"
        with options().option_context({"transforms": {"source": tmp, "destination": tmp}}):
            self.c.fit(src=src, method="pchip3", k=k, n_samples=k)
            self.c.score(src=score, dst=tmp_score).sort(by=tmp_score)
            self.c.plot.scatter(
                figure=figure,
                show=show,
                ms=ms,
                lw=lw,
                alpha=alpha * (1 if not alpha_score else tmp_score),
                score=tmp_score,
                style=style,
            )
            self.c.drop()

    def highways(
        self, src=None, figure=None, show=True, score="idx", style="-", lw=1, ms=1, alpha=1, alpha_score=False
    ):
        src = options().default_if_null(src, "transforms.source")
        tmp = options().get("transforms.tmp")
        tmp_score = f"{tmp}.score"
        with options().option_context({"transforms": {"source": tmp, "destination": tmp}}):
            # TODO: move sort to internals of scatter(), without sorting c.df
            self.c.score(src=score, dst=tmp_score).sort(by=tmp_score)
            self.c.plot.scatter(
                src=src,
                figure=figure,
                show=show,
                score=tmp_score,
                lw=lw,
                ms=ms,
                style=style,
                alpha=alpha if not alpha_score else tmp_score,
            )
            self.c.drop()

    def highlights(self, src=None, figure=None, show=True, score="idx", style="-", lw=1, ms=1, alpha_score=False, k=8):
        self.highways(
            src=src, figure=figure, show=show, score=score, style=style, lw=lw, ms=ms, alpha_score=alpha_score
        )

    def highlight(self, idx=None, src=None, figure=None, show=True):

        if idx is None:
            self.c.plot.scatter(figure=figure, show=show, src=src, style="-", color="white")
            return

        if figure is not None:
            fig = figure
        else:
            fig = Figure()

        self.c.plot.scatter(figure=fig, show=False, src=src, style="-", color="white")

        if not isinstance(idx, list):
            idx = [idx]

        for pos, idx_elem in enumerate(idx):
            c_line = self.c.__class__(df=self.c.df[self.c.df["idx"] == idx_elem])
            c_line.plot.scatter(
                figure=fig,
                show=show if pos == len(idx) - 1 else False,
                src=src,
                alpha=1,
                style="--",
                lw=2,
                color="fuchsia",
            )

    def pixelate(self, src=None, figure=None, show=True, k=30, alpha=0.05, ms=5, style="s"):
        src = options().default_if_null(src, "transforms.source")
        tmp = options().get("transforms.tmp")
        with options().option_context({"transforms": {"source": tmp, "destination": tmp}}):
            self.c.interp(n_samples=k, src=src)
            self.c.bin(n_bins=k)
            self.c.fit(method="pchip3", k=k, n_samples=k)
            self.c.plot.scatter(figure=figure, show=show, alpha=alpha, ms=ms, style=style)
            self.c.drop()

    def scatter(
        self,
        src=None,
        figure=None,
        show=True,
        style=".",
        ms=2,
        lw=1,
        score=None,
        alpha=0.5,
        x_label="x",
        y_label="y",
        color="white",
    ):

        src = options().default_if_null(src, "transforms.source")

        if figure is None:
            figure = Figure(x_label=x_label, y_label=y_label)

        for _, row in self.c.df.iterrows():
            row_color = figure.cmap(row[score]) if isinstance(score, str) else color
            row_alpha = row[alpha] if isinstance(alpha, str) else alpha
            pd.Series(row[f"{src}.y"], index=row[f"{src}.x"]).plot(
                style=style,
                lw=lw,
                ms=ms,
                color=row_color,
                alpha=row_alpha,
                ax=figure.ax,
            )

        if show and plt.isinteractive():
            plt.show()
