# %%

import xrdtools
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read files

pristine = xrdtools.read_xrdml('../data/xrd/PCN777-asreceived.xrdml')
ads_d4 = xrdtools.read_xrdml('../data/xrd/PCN777-adsD4.xrdml')
ads_h2o = xrdtools.read_xrdml('../data/xrd/PCN777-adsH2O.xrdml')
simulated = pd.read_csv(
    '../data/xrd/PCN777-RESP-sim.xy',
    delim_whitespace=True,
    names=["intensity", "N/A"],
)

pristine['name'] = "pristine"
ads_d4['name'] = "D4 cycling"
ads_h2o['name'] = "$H_2O$ sorption"

# plot


def plot(ax):

    offset = 1200
    ymax = 20

    for ind, (pxrd, c) in enumerate(
        zip([ads_h2o, ads_d4, pristine], ['C2', 'C0', 'k'])
    ):

        ax.plot(pxrd['x'], pxrd['data'] + ind * offset, color=c)
        ax.text(
            ymax - 2.5,
            ind * offset + 100,
            pxrd['name'],
            horizontalalignment='center',
            fontsize=15,
        )

    ax.set_xlim(2, ymax)
    ax.set_xlabel("Angle ($2\\theta$)", fontsize=15)

    ax.set_ylabel("Intensity (a.u.)", fontsize=15)
    ax.set_yticks([])
    ax.tick_params(axis='both', labelsize=13)


if __name__ == '__main__':

    fig, ax = plt.subplots(1, figsize=(6, 4))
    plot(ax)
    fig.tight_layout()
    fig.savefig("../figs/components/pxrd-all.svg")
    fig.savefig("../figs/components/pxrd-all.pdf")
    fig.savefig("../figs/components/pxrd-all.png", dpi=300)

# %%
import numpy as np

fig, ax = plt.subplots(1, figsize=(10, 4))
ax.plot(pristine['x'], np.log(pristine['data'] + 1), color='blue')
ax.plot(simulated.index * 0.97, np.log(simulated.intensity + 1), color="k")
ax.text(14, 1, "simulated", horizontalalignment='center', fontsize=14)
ax.text(14, 4, "synthesised", horizontalalignment='center', fontsize=14)
ax.set_ylim(-1, 8)
ax.set_xlim(4, 16)
ax.set_xlabel("Angle ($2\\theta$)", fontsize=15)

ax.set_ylabel("Log Intensity (a.u.)", fontsize=15)
ax.set_yticks([])
ax.tick_params(axis='both', labelsize=13)

fig.savefig("../figs/components/pxrd-synth.svg", bbox_inches="tight")
fig.savefig("../figs/components/pxrd-synth.pdf", bbox_inches="tight")
fig.savefig("../figs/components/pxrd-synth.png", dpi=300, bbox_inches="tight")

# %%
