import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

fontsize = 12

df = pd.read_csv("data/results_RQ2.csv")

year_data = df["Year"]

min_year = int(year_data.min())
max_year = int(year_data.max())

year_counts = year_data.value_counts().sort_index()
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
year_counts = year_counts.reindex(all_years['Year'], fill_value=0)

colors = [mcolors.to_rgba('grey', alpha=0.4 + 0.6 * (value - year_counts.min()) / (year_counts.max() - year_counts.min())) for value in year_counts.values]

fig, ax = plt.subplots(figsize=(8, 2.5))

bars = ax.bar(year_counts.index, year_counts.values, color=colors, width=.6, align='center')
plt.xlabel("Year", fontsize=12)
plt.ylabel("# of papers", fontsize=12)
plt.xticks(range(min_year, max_year + 1), fontsize=12, rotation=45) 
plt.yticks(np.arange(0, max(year_counts) + 10, 10), fontsize=12)
plt.grid(axis="y", color="white")
plt.ylim(0,24)
plt.xlim(min_year - 0.5, max_year + 0.5)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height ), xytext=(0, 3),
                textcoords='offset points', ha='center', va='bottom', fontsize=10)

fig.tight_layout()
plt.show()
fig.savefig('images/years_nocumulative.pdf', bbox_inches='tight', dpi=1000)
