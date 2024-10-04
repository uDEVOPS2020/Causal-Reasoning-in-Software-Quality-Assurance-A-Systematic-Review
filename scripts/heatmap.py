import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter
from matplotlib import colors
import seaborn as sns

df_start = pd.read_csv("data/heatmap.csv")

df_sorted = df_start.pivot(index="Task",columns="Attribute",values="occurrences").sort_values(by=["Reliability"],ascending=False)
df_sorted = df_sorted.reindex(columns=['Reliability','Performance','Security','Safety','Maintainability','Availability','Usability','Testability'])
ax = sns.heatmap(df_sorted, cmap="Greys", norm = colors.TwoSlopeNorm(vmin=-1, vcenter=8, vmax=24), cbar=False, annot=True)

for t in ax.texts:
    if float(t.get_text())>0 and float(t.get_text())<60:
        t.set_text(t.get_text()) 
    else:
        t.set_text("") 

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('images/map.pdf')