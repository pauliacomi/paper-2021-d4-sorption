# %%

import pygaps as pg
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read isotherms

d4_30_1 = pg.isotherm_from_csv("../data/d4sorp/iso_PCN777_D4_303_c1.csv")
d4_30_2 = pg.isotherm_from_csv("../data/d4sorp/iso_PCN777_D4_303_c2.csv")
h2o_30 = pg.isotherm_from_csv("../data/h2osorp/iso_PCN777_H2O_303.csv")
d4_30_1.label = 'D4 cycle 1'
d4_30_2.label = 'D4 cycle 2'
h2o_30.label = 'H$_2$O'

isos = [h2o_30, d4_30_1, d4_30_2]

# plot


def plot(ax):
    pg.plot_iso(
        [d4_30_1, d4_30_2, h2o_30],
        ax=ax,
        branch='all-nol',
        loading_basis='mass',
        loading_unit='g',
        pressure_unit='Pa',
        lgd_keys=['label'],
        lgd_pos='inner',
        color=["#356691", "#96caf7", "C2"],
        x_range=[0, 10],
        y1_range=[-0.1, 2.1],
        lgd_style=dict(loc='center left'),
    )
    ax.set_yticks([0, 0.5, 1, 1.5, 2])

    ax.set_ylabel(r"Loading ($g\ g^{-1}$)")
    ax.set_xlabel(r"Pressure ($Pa$)")


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    plot(ax)

    fig.tight_layout()
    fig.savefig("../figs/components/d4-sorption.svg")
    fig.savefig("../figs/components/d4-sorption.pdf")
    fig.savefig("../figs/components/d4-sorption.png", dpi=300)

# %%
