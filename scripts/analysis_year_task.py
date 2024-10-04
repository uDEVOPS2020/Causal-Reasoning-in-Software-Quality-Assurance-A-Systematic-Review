import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

fontsize = 10

df = pd.read_csv("data/results_RQ2.csv")

year_task_data = df[df['Task'].isin(['inference', 'discovery', 'both'])]

pivot_table = year_task_data.pivot_table(index='Year', columns='Task', aggfunc='size', fill_value=0)

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})

pivot_table = pivot_table.reindex(all_years['Year'], fill_value=0).fillna(0)

colors = {'inference': 'tab:orange', 'discovery': 'tab:blue', 'both': 'tab:grey'}
hatches = {'inference': '..', 'discovery': '\\\\', 'both': '//'}
labels = {'inference': 'Inference', 'discovery': 'Discovery', 'both': 'Both'}

fig, ax = plt.subplots(figsize=(8, 2.5))

bottom = np.zeros(len(pivot_table))

for task in ['inference', 'discovery', 'both']:
    counts = pivot_table[task].values
    bars = ax.bar(pivot_table.index, counts, bottom=bottom, color=colors[task], width=0.6, label=labels[task])
    bottom += counts

plt.xlabel("Year", fontsize=10)
plt.ylabel("# of papers", fontsize=10)
plt.xticks(range(min_year, max_year + 1), fontsize=10, rotation=45)
plt.yticks(np.arange(0, pivot_table.values.sum() + 10, 10), fontsize=10)
plt.ylim(0, 24)
plt.xlim(min_year - 0.5, max_year + 0.5)
plt.legend()

totals = pivot_table.sum(axis=1)
for i, total in enumerate(totals):
    ax.text(totals.index[i], total + 0.5, f'{total}', ha='center', fontsize=10)

fig.tight_layout()
plt.show()
fig.savefig('images/years_task.pdf', bbox_inches='tight', dpi=1000)
