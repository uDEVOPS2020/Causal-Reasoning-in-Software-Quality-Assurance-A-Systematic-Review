import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
fontsize = 12

df = pd.read_csv("data/results_MAJOR_RQ2_model.csv")

column = "Model"
categories = ['SCM', 'CausalDAG', 'PO', 'Other']

# Filter the data for the relevant tasks
year_task_data = df[df[column].isin(categories)]

# Create a pivot table to count the occurrences of each task per year
pivot_table = year_task_data.pivot_table(index='Year', columns=column, aggfunc='size', fill_value=0)

# Ensure all years are represented in the pivot table
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
pivot_table = pivot_table.reindex(all_years['Year'], fill_value=0).fillna(0)

# Define colors for the tasks
colors = {'SCM': 'tab:orange', 'CausalDAG': 'tab:blue', 'PO': 'tab:green', 'Other': 'tab:grey'}
# hatches = {'inference': '..', 'discovery': '\\\\', 'both': '//'}
# labels = {'inference': 'Inference', 'discovery': 'Discovery', 'both': 'Both'}

# Plot
fig, ax = plt.subplots(figsize=(8, 2.5))

# Create stacked bar chart
bottom = np.zeros(len(pivot_table))
for task in categories:
    counts = pivot_table[task].values
    bars = ax.bar(pivot_table.index, counts, bottom=bottom, color=colors[task], width=0.6, label=task) #, hatch=hatches[task])
    bottom += counts

# Customize the plot
plt.xlabel("Year", fontsize=12)
plt.ylabel("# of papers", fontsize=12)
plt.xticks(range(min_year, max_year + 1), fontsize=12, rotation=45)
plt.yticks(np.arange(0, pivot_table.values.sum() + 10, 10), fontsize=12)
# plt.grid(axis="y", color="white")
plt.ylim(0, 24)
plt.xlim(min_year - 0.5, max_year + 0.5)
plt.legend()

# # Annotate bars
# for bars in ax.containers:
#     ax.bar_label(bars, fmt='%d', label_type='center', fontsize=10)

# Final adjustments and save
fig.tight_layout()
plt.show()
fig.savefig('images/years_model.pdf', bbox_inches='tight', dpi=1000)

