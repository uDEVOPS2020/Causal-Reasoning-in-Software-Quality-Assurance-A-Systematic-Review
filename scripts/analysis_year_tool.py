import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


fontsize = 10

df = pd.read_csv("data/results_RQ2_tools.csv")

column = "USED"
categories = ['yes']

year_task_data = df[df[column].isin(categories)]

pivot_table = year_task_data.pivot_table(index='Year', columns=column, aggfunc='size', fill_value=0)

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
pivot_table = pivot_table.reindex(all_years['Year'], fill_value=0).fillna(0)

colors = {'yes': 'tab:blue'}

fig, ax = plt.subplots(figsize=(8, 2.5))

bottom = np.zeros(len(pivot_table))
for task in categories:
    counts = pivot_table[task].values
    bars = ax.bar(pivot_table.index, counts, bottom=bottom, color=colors[task], width=0.6, label=task)
    bottom += counts

plt.xlabel("Year", fontsize=10)
plt.ylabel("# of papers", fontsize=10)
plt.xticks(range(min_year, max_year + 1), fontsize=10, rotation=45)
plt.yticks(np.arange(0, pivot_table.values.sum() + 10, 10), fontsize=10)
plt.ylim(0, 10)
plt.xlim(min_year - 0.5, max_year + 0.5)

total_counts = pivot_table.sum(axis=1)
for i, total in enumerate(total_counts):
    ax.text(total_counts.index[i], total + 0.5, f'{total}', ha='center', fontsize=10)

fig.tight_layout()
plt.show()
fig.savefig('images/years_tool.pdf', bbox_inches='tight', dpi=1000)
