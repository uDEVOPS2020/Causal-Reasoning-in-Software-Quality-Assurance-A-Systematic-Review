import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter
from matplotlib import colors
import seaborn as sns
import pandas as pd


df = pd.read_csv("data/taskdomain.csv")
df_start = df.groupby(["Task","Domain"]).size().to_frame(name = 'count').reset_index()

df_sorted = df_start.pivot(index="Domain",columns="Task",values="count").sort_values(by=["Fault localization","Testing & analysis"],ascending=False)
df_sorted = df_sorted.reindex(columns=['Fault localization','Testing & analysis','KPI prediction','Fault prediction','Anomaly detection','Threats modeling'])

ax = sns.heatmap(df_sorted, cmap="Greys", norm = colors.TwoSlopeNorm(vmin=-1, vcenter=5, vmax=10), cbar=False, annot=True)

for t in ax.texts:
    if float(t.get_text())>0 and float(t.get_text())<10:
        t.set_text(t.get_text()) 
    else:
        t.set_text("") 

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('images/rq3_map_ext.pdf')