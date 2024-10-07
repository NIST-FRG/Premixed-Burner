#!/usr/bin/env python3
# McDermott
# Oct 2024

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.close('all')

wrk_dir = '../DATA/Shakedown_20241004/'

M = pd.read_csv(wrk_dir+'10-4-2024_PreMixedBurner42.csv', sep=' *, *', engine='python', comment='#', header=[0,1])

time     = M['Time'].values
hrr      = M['HRR_cal'].values
mdot_air = M['Air Flow Rate'].values

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('HRR (kW)', color=color)
ax1.plot(time, hrr, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Air Flow Rate (L/min)', color=color)  # we already handled the x-label with ax1
ax2.plot(time, mdot_air, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# ax.legend()

plt.savefig('plot_HRR_and_Air_Flow.pdf')
