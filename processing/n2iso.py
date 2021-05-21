# %%

import matplotlib.pyplot as plt
import pygaps as pg
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

# read isotherms

isoD4 = pg.isotherm_from_csv('../data/n2sorp/iso_PCN777_N2_77_afterD4.csv')
isoH2O = pg.isotherm_from_csv('../data/n2sorp/iso_PCN777_N2_77_afterH2O.csv')
isoPCN = pg.isotherm_from_csv('../data/n2sorp/iso_PCN777_N2_77_pristine.csv')

# plot isotherms

ax = pg.plot_iso(
    [isoPCN, isoD4, isoH2O],
    pressure_mode='relative',
    loading_unit='mmol',
    branch='all-nol',
    lgd_pos='inner',
    lgd_keys=['batch'],
    color=['C0', 'C1', 'C2'],
)
ax.set_ylabel(r"Loading ($mmol\ g^{-1}$)")
ax.set_xlabel(r"Pressure ($p/p^0$)")

plt.savefig("../figs/n2-phys.svg")
plt.savefig("../figs/n2-phys.pdf")
plt.savefig("../figs/n2-phys.png", dpi=300)

# %% calculate and plot BET area

pg.area_BET(isoPCN, limits=[0.005, 0.35], verbose=True)

figs = list(map(plt.figure, plt.get_fignums()))

figs[0].savefig("../figs/n2-bet.svg")
figs[0].savefig("../figs/n2-bet.pdf")
figs[0].savefig("../figs/n2-bet.png", dpi=300)
figs[1].savefig("../figs/n2-roq.svg")
figs[1].savefig("../figs/n2-roq.pdf")
figs[1].savefig("../figs/n2-roq.png", dpi=300)

# %%

pg.t_plot(isoPCN, limits=[0.6, 2], verbose=True)
pg.t_plot(isoD4, limits=[0.6, 2], verbose=True)
pg.t_plot(isoH2O, limits=[0.6, 2], verbose=True)

# %%

fig, ax = plt.subplots(1, figsize=(6, 4))

ax = pg.plot_iso(
    [isoPCN],
    ax=ax,
    pressure_mode='relative',
    loading_unit='mmol',
    branch='all-nol',
    lgd_pos='inner',
    lgd_keys=['batch'],
    color=['k'],
)
ax.set_ylabel(r"Loading ($mmol\ g^{-1}$)")
ax.set_xlabel(r"Pressure ($p/p^0$)")

plt.savefig("../figs/components/n2-phys-1.svg")
plt.savefig("../figs/components/n2-phys-1.pdf")
plt.savefig("../figs/components/n2-phys-1.png", dpi=300)
# %%
