import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter
from matplotlib import colors
import seaborn as sns

df_start = pd.read_csv("heatmap.txt")

df_sorted = df_start.pivot(index="Task",columns="Attribute",values="occurrences").sort_values(by=["Reliability"],ascending=False)
df_sorted = df_sorted.reindex(columns=['Reliability','Performance','Safety','Security','Availability','Maintainability','Usability','Testability'])
ax = sns.heatmap(df_sorted, cmap="Greys", norm = colors.TwoSlopeNorm(vmin=-1, vcenter=8, vmax=24), cbar=False, annot=True)

for t in ax.texts:
    if float(t.get_text())>0 and float(t.get_text())<30:
        t.set_text(t.get_text()) #if the value is greater than 0.4 then I set the text 
    else:
        t.set_text("") # if not it sets an empty text

plt.tight_layout()
plt.savefig('map.pdf')