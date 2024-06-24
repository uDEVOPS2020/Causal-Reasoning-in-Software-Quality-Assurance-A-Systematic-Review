import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
fontsize = 12

# df = pd.read_csv("results_MAJOR.csv")

# # YEARS
# year_data = df["Year"]

# min_year = int(year_data.min())
# max_year = int(year_data.max())

# year_counts = df['Year'].value_counts().sort_index()
# cumulative_counts = year_counts.cumsum()
# all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
# cumulative_counts = cumulative_counts.reindex(all_years['Year'], method='ffill').fillna(0)


# colors = [mcolors.to_rgba('grey', alpha=0.4 + 0.6 * (value - cumulative_counts.min()) / (cumulative_counts.max() - cumulative_counts.min())) for value in cumulative_counts.values]

# fig, ax = plt.subplots(figsize=(8,2.2))

# bars = ax.bar(cumulative_counts.index, cumulative_counts.values, color=colors, width=.6, align='center')
# plt.xlabel("Year", fontsize=fontsize)
# plt.ylabel("# of papers", fontsize=fontsize)
# plt.xticks(range(min_year, max_year + 1), fontsize=fontsize, rotation=45) 
# plt.yticks(np.arange(0, max(cumulative_counts) + 10, 10), fontsize=fontsize)
# plt.grid(axis="y", color="white")
# # plt.ylim(0,55)
# plt.xlim(2003.5,2024.5)

# for bar in bars:
#     height = bar.get_height()
#     ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height-1), xytext=(0, 3),
#                 textcoords='offset points', ha='center', va='bottom', fontsize=fontsize-2)

# # sm = plt.cm.ScalarMappable(cmap=colormap, norm=normalize)
# # sm.set_array([])  # Fake the scalar mappable's data
# # cbar = plt.colorbar(sm, orientation="vertical")
# # cbar.set_label("Frequency Color")

# fig.tight_layout()
# plt.show()
# fig.savefig('images/years.pdf',bbox_inches='tight', dpi=1000)


df = pd.read_csv("data/results_MAJOR_RQ2.csv")

# YEARS
# year_data = df[df['Task'].isin(['inference', 'discovery', 'both'])]
year_data = df["Year"]

min_year = int(year_data.min())
max_year = int(year_data.max())

# Count publications per year
year_counts = year_data.value_counts().sort_index()
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
year_counts = year_counts.reindex(all_years['Year'], fill_value=0)

# # Define colors
colors = [mcolors.to_rgba('grey', alpha=0.4 + 0.6 * (value - year_counts.min()) / (year_counts.max() - year_counts.min())) for value in year_counts.values]

# Plot
fig, ax = plt.subplots(figsize=(8, 2.5))

bars = ax.bar(year_counts.index, year_counts.values, color=colors, width=.6, align='center')
plt.xlabel("Year", fontsize=12)
plt.ylabel("# of papers", fontsize=12)
plt.xticks(range(min_year, max_year + 1), fontsize=12, rotation=45) 
plt.yticks(np.arange(0, max(year_counts) + 10, 10), fontsize=12)
plt.grid(axis="y", color="white")
plt.ylim(0,24)
plt.xlim(min_year - 0.5, max_year + 0.5)

# Annotate bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height ), xytext=(0, 3),
                textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Final adjustments and save
fig.tight_layout()
plt.show()
fig.savefig('images/years_nocumulative.pdf', bbox_inches='tight', dpi=1000)
