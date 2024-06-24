import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter

df_start = pd.read_csv("Attributes.txt")
df = (df_start.value_counts()).reset_index().rename(columns={"index": "Attribute", 0: "count"})
print(df)

num_fl = df_start.value_counts().reset_index()[0]

plt.figure(figsize=(15,5))
plt.rcParams.update({'font.size': 30})

# plt.bar(df["Attribute"],df["count"],color='green', width=0.5)
plt.bar(df.index,df["count"],color='green', width=0.5)
y_perc = list(map("{:.2%}".format, df["count"]))

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.ylabel("# of papers")

plt.ylim([0,35])

# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals=0))
plt.grid(axis = 'y', color='white', linestyle='-', linewidth=0.5)

plt.text(-0.15,  df["count"][0]+0.3, str(df["count"][0]),rotation=0)
for i in range(1,8):
    plt.text(i-0.085,  df["count"][i]+0.3, str(df["count"][i]),rotation=0)

plt.tight_layout()
plt.savefig('Attribute.pdf')