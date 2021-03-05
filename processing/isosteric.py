# %%

import numpy as np
import pygaps as pg
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read files

d4_30 = pg.isotherm_from_csv("../data/d4sorp/iso_PCN777_D4_303_c1.csv")
d4_40 = pg.isotherm_from_csv("../data/d4sorp/iso_PCN777_D4_313.csv")
isos = [d4_30, d4_40]

# Calculate isosteric enthalpy

for iso in isos:
    iso.convert_loading(basis_to="molar", unit_to="mmol")

res = pg.isosteric_enthalpy(
    isos,
    loading_points=np.linspace(0.3, 6.0, 300),
)
res['loading_g'] = res['loading'] * iso.adsorbate.molar_mass() / 1000

# Plot isotherms and results

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

pg.plot_iso(
    isos,
    ax=axs[0],
    lgd_keys=['temperature'],
    lgd_pos=None,
    loading_basis='mass',
    loading_unit='g',
    color=['C0', "C7"],
    branch="all-nol",
    pressure_unit='Pa',
    y1_range=[-0.1, 2.1],
)

axs[0].set_ylabel(r"Loading ($g\ g^{-1}$)")
axs[0].set_xlabel(r"Pressure ($Pa$)")

pg.plot_iso(
    isos,
    ax=axs[1],
    lgd_keys=['temperature'],
    lgd_pos="inner",
    loading_basis='mass',
    loading_unit='g',
    pressure_mode='relative%',
    color=['C0', "C7"],
    branch="all-nol",
    pressure_unit='Pa',
    y1_range=[-0.1, 2.1],
    lgd_style=dict(loc='center left'),
)

axs[1].set_ylabel(r"Loading ($g\ g^{-1}$)")
axs[1].set_xlabel(r"Pressure (%$p/p^0$)")

axs[2].errorbar(
    res['loading_g'],
    res['isosteric_enthalpy'],
    yerr=res['std_errs'],
    marker="o",
    color="C2",
    markersize=2,
)
axs[2].set_xlabel(r"Loading ($g\ g^{-1}$)", fontsize=15)
axs[2].set_ylabel(r"Isosteric Enthalpy ($-kJ\ mol^{-1}$)", fontsize=15)
axs[2].set_ylim(-5, 105)
axs[2].set_xlim(0, 2.1)
axs[2].tick_params(axis='both', labelsize=13)

axs[0].text(0.05, 0.9, "(a)", fontsize=15, transform=axs[0].transAxes)
axs[1].text(0.05, 0.9, "(b)", fontsize=15, transform=axs[1].transAxes)
axs[2].text(0.05, 0.9, "(c)", fontsize=15, transform=axs[2].transAxes)

fig.savefig("../figs/isosteric-enth.svg", bbox_inches='tight')
fig.savefig("../figs/isosteric-enth.pdf", bbox_inches='tight')
fig.savefig("../figs/isosteric-enth.png", dpi=300, bbox_inches='tight')

# %%