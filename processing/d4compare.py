# %%

import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

import numpy as np

capacities = {
    "Carbons": [0.334, 0.0052, 0.065, 1.732, 0.225, 0.404, 0.192, 0.41],
    "Silicas": [0.184, 0.216, 0.25],
    "Zeolites": [0.143, 0.052, 0.105, 0.113, 0.051],
    # "MOFs": -1,
}
mofs = {
    "PCN-777": 1.8,
    "MIL-101(Cr)": 0.95,
    "DUT-4": 0.42,
}


def plot(ax):

    bars = {}

    for x in mofs:
        bars[x] = [mofs[x], 0]

    for x in capacities:
        bars[x] = [np.mean(capacities[x]), np.std(capacities[x])]

    ax.bar(
        x=range(len(bars)),
        height=[x[0] for x in bars.values()],
        width=0.5,
        tick_label=list(bars.keys()),
        color=list(reversed(['C3', 'C2', 'C4', 'C1', 'C5', 'C0'])),
        edgecolor='k',
        yerr=([0 for x in bars.values()], [x[1] for x in bars.values()]),
        capsize=4,
    )

    ax.set_ylim(-0.1, 2.1)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.set_ylabel(r"Loading ($g\ g^{-1}$)", fontsize=15)
    ax.tick_params(axis='y', labelsize=13)

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='x', labelsize=13)


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))

    plot(ax)

    fig.savefig("../figs/components/d4-compare.png", dpi=300)
    fig.savefig("../figs/components/d4-compare.svg")
    fig.savefig("../figs/components/d4-compare.pdf")

# %%
