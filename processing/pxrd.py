# %%

import xrdtools
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read files

pristine = xrdtools.read_xrdml('../data/xrd/PCN777-asreceived.xrdml')
ads_d4 = xrdtools.read_xrdml('../data/xrd/PCN777-adsD4.xrdml')
ads_h2o = xrdtools.read_xrdml('../data/xrd/PCN777-adsH2O.xrdml')

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