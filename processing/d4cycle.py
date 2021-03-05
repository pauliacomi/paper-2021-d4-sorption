# %%

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read / process cycle data

data_f = pd.read_csv('../data/d4sorp/cycle_PCN777_D4_303.csv')
data_f["time"] = pd.to_timedelta(data_f["time"])
data_f = data_f.set_index("time")

x = list(map(lambda x: x.seconds / 60, data_f.index))
p = data_f['pressure (Pa)'].ewm(com=10).mean().values
m = data_f['loading (g/g)'].values


def plot(ax):

    ax2 = ax.twinx()

    ax2.plot(x, p, 'k', label='pressure')
    ax.plot(x, m, 'C0', label='loading', lw=2, zorder=10)

    ax.set_zorder(1)
    ax.patch.set_visible(False)

    ax.set_xlabel("Time ($min$)", fontsize=15)
    ax.set_ylabel(r"Loading ($g\ g^{-1}$)", fontsize=15)
    ax2.set_ylabel(r"Pressure ($Pa$)", fontsize=15)

    ax.set_xlim(-40, 730)
    ax.set_ylim(-.1, 2.1)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
    ax2.set_ylim(-0.5, 10.5)
    ax2.set_yticks([0, 2.5, 5, 7.5, 10])
    ax.tick_params(axis='both', labelsize=13)
    ax2.tick_params(axis='both', labelsize=13)

    ax.arrow(40, 1.5, -50, 0, head_width=0.05, head_length=10, color='C0')
    ax.arrow(660, 0.2, 50, 0, head_width=0.05, head_length=10, color='k')


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    plot(ax)

    fig.tight_layout()
    fig.savefig("../figs/components/d4-cycle.svg")
    fig.savefig("../figs/components/d4-cycle.pdf")
    fig.savefig("../figs/components/d4-cycle.png", dpi=300)

# %%
