import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


count = 100000
light = np.random.normal(4, 0.07, 100000)
dark = np.random.normal(6, 0.8, 100000)

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True, figsize=(8,4))

# We can set the number of bins with the `bins` kwarg
axs[0].hist(light, bins=10, color='orange', label='light')
axs[1].hist(dark, bins=10, color='blue', label='dark')

handles, labels = [(a + b) for a, b in zip(axs[0].get_legend_handles_labels(), axs[1].get_legend_handles_labels())]
axs[1].legend(handles, labels, loc='upper right')

# axs[0].tick_params(labelcolor="none", bottom=False, left=False)
# axs[1].tick_params(labelcolor="none", bottom=False, left=False)

axs[0].xaxis.set_major_formatter(mtick.PercentFormatter())
axs[1].xaxis.set_major_formatter(mtick.PercentFormatter())


# fig.text(0.5, 0.04, 'Percent Increase', ha='center')

fig.savefig('hypothesis.png', dpi=300, bbox_inches = 'tight',pad_inches = 0)

