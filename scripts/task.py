import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter

df_start = pd.read_csv("data/task.csv")
df_start = df_start.drop(columns="Secondary")
num_papers = df_start.shape[0]-1
df = (df_start.value_counts()/num_papers).reset_index().rename(columns={"index": "Task", 0: "count"})
df = df.sort_index(ascending=False).reset_index(drop=True)

num_fl = df_start.value_counts().reset_index()

plt.figure(figsize=(15,10))
plt.rcParams.update({'font.size': 30})

plt.barh(df.index,df["count"],tick_label=df["Task"],height=0.5)#, width=0.5)

y_perc = list(map("{:.2%}".format, df["count"]))

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.ylabel("Task")
plt.xlabel("% of papers")
plt.xlim([0,0.7])

plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
plt.grid(axis = 'x', color='white', linestyle='-', linewidth=0.5)

for i in range(0,6):
    plt.text(df["count"][i]+0.01, i-0.075, str(y_perc[i])+" ("+str(df_start.value_counts().sort_values()[i])+")",rotation=0)

plt.tight_layout()
plt.savefig('images/tasks.pdf')

df_start = pd.read_csv("data/task.csv")
df_start = df_start.drop(columns="Task")
print(df_start)
print(num_fl)
df = (df_start.value_counts()/num_fl).reset_index().rename(columns={"index": "Secondary", 0: "count"})
plt.figure(figsize=(10,10))

y_perc = list(map("{:.2%}".format, df["count"]))

plt.pie(df["count"], labels=[df["Secondary"][0]+" ("+y_perc[0]+")",df["Secondary"][1]+" ("+y_perc[1]+")"],labeldistance=1.1)

plt.tight_layout()
plt.savefig('images/FaultLoc.pdf')