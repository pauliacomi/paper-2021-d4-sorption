# %%

import pxrd
import d4iso
import d4cycle
import d4compare

import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.style.use('seaborn-muted')

fig = plt.figure(figsize=(15, 10))
gs = fig.add_gridspec(2, 6)

ax1 = fig.add_subplot(gs[0:1, 0:3])
ax2 = fig.add_subplot(gs[0:1, 3:6])
ax3 = fig.add_subplot(gs[1:2, 0:3])
ax4 = fig.add_subplot(gs[1:2, 3:6])

d4iso.plot(ax1)
d4compare.plot(ax2)
d4cycle.plot(ax3)
pxrd.plot(ax4)

ax1.text(0.025, 0.93, "(a)", fontsize=15, transform=ax1.transAxes)
ax2.text(0.025, 0.93, "(b)", fontsize=15, transform=ax2.transAxes)
ax3.text(0.025, 0.93, "(c)", fontsize=15, transform=ax3.transAxes)
ax4.text(0.025, 0.93, "(d)", fontsize=15, transform=ax4.transAxes)

fig.tight_layout()

fig.savefig("../figs/d4-experiment.svg")
fig.savefig("../figs/d4-experiment.pdf")
fig.savefig("../figs/d4-experiment.png", dpi=300)

# %%