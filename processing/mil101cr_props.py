# %%

import xrdtools
import pygaps as pg
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read files

pxrd = xrdtools.read_xrdml('../data/xrd/MIL101Cr-pristine.xrdml')
iso = pg.isotherm_from_csv('../data/n2sorp/iso_MIL101Cr_N2_77_pristine.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(pxrd['x'], pxrd['data'], 'k')
ax1.set_xlim(2, 50)
ax1.set_xlabel("Angle ($2\\theta$)", fontsize=15)
ax1.set_ylabel("Intensity (a.u.)", fontsize=15)
ax1.set_yticks([])
ax1.tick_params(axis='both', labelsize=13)

pg.plot_iso(
    iso,
    ax=ax2,
    loading_unit='cm3(STP)',
    branch='all',
    lgd_pos='inner',
    lgd_keys=['material', 'branch'],
    color=['k'],
)
ax2.set_ylabel(r"Loading ($cm^3_{STP}\ g^{-1}$)")
ax2.set_xlabel(r"Pressure ($p/p^0$)")

ax1.text(-0.09, 0.93, "(a)", fontsize=15, transform=ax1.transAxes)
ax2.text(-0.09, 0.93, "(b)", fontsize=15, transform=ax2.transAxes)

plt.savefig("../figs/mil101_summary.svg")
plt.savefig("../figs/mil101_summary.pdf")
plt.savefig("../figs/mil101_summary.png", dpi=300)

# %%
