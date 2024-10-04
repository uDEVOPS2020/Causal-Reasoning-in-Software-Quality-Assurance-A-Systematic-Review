import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter

df_start = pd.read_csv("data/domain.csv")
df = pd.DataFrame()
df["count"] = df_start.value_counts()
df=df.rename_axis('domain').reset_index()

bars = plt.barh(df["domain"],df["count"],height=0.5)

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.ylabel("Domain")
plt.xlabel("# of papers")
plt.grid(axis = 'x', color='white', linestyle='-', linewidth=0.5)

for bar in bars:
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}', va='center')


plt.tight_layout()
plt.savefig('images/domain.pdf')