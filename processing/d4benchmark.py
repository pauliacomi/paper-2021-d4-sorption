# %%

import pygaps as pg
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

mil101_iso = pg.isotherm_from_csv("../data/d4sorp/iso_MIL101Cr_D4_303.csv")
dut4_iso = pg.isotherm_from_csv("../data/d4sorp/iso_DUT4_D4_303.csv")


def plot(ax):

    pg.plot_iso(
        [mil101_iso, dut4_iso],
        ax=ax,
        loading_basis='mass',
        loading_unit='g',
        pressure_unit='Pa',
        lgd_keys=['material'],
        lgd_pos='inner',
        branch="all-nol",
        color=["C2", "C5", "C2"],
        x_range=[-0.1, 10],
        y1_range=[-0.05, 1.5],
        lgd_style=dict(loc='lower right'),
    )

    ax.set_ylabel(r"Loading ($g\ g^{-1}$)")
    ax.set_xlabel(r"Pressure ($Pa$)")


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    plot(ax)

    fig.tight_layout()
    plt.savefig("../figs/benchmark-d4.pdf")
    plt.savefig("../figs/benchmark-d4.svg")
    plt.savefig("../figs/benchmark-d4.png", dpi=300)
