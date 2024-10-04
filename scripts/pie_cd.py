import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

fontsize = 25

df = pd.read_csv("data/results_RQ2_cd.csv")
task_counts = df['Category'].value_counts()

fig, ax = plt.subplots(figsize=(8,8))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
ax.pie(task_counts, explode=explode, labels=task_counts.index, colors = ["tab:blue","tab:blue","tab:blue","tab:blue", "tab:blue", "tab:blue"], autopct='%1.1f%%', startangle=90, textprops={'fontsize': fontsize})
ax.axis('equal')
fig.tight_layout()
fig.savefig('images/cr_cd.pdf',bbox_inches='tight', dpi=1000)