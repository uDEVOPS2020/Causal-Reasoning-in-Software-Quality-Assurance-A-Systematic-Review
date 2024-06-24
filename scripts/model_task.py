import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.ticker import MaxNLocator
plt.rcParams.update({'font.size': 25})

# plt.rcParams["font.family"] = "Times New Roman"

# TASK
df = pd.read_csv("data/task.txt")
task_counts = df['task'].value_counts()

# fig, ax = plt.subplots(figsize=(8,8))
# explode = (0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
# ax.pie(task_counts, explode=explode, labels=task_counts.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 22})
# ax.axis('equal')
# fig.tight_layout()
# # plt.show()
# fig.savefig('images/cr_task.pdf',bbox_inches='tight', dpi=1000)


# MODEL
df = pd.read_csv("data/model.csv")
df['Model'] = df['Model'].str.split(';')
df = df.explode('Model')

model_counts = df['Model'].value_counts()

fig, ax = plt.subplots(figsize=(17,5))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

ax.barh(model_counts.index, model_counts.values,color="white",edgecolor="black",linewidth=1.5)
plt.xlabel('Count')
plt.ylabel('Model')
# plt.title('Model Distribution')
# plt.xticks(rotation=0)
# plt.grid(which='both',axis="x", color="white", alpha=0.5)

ax.barh(model_counts.index, model_counts.values-0.015, height=0.78,hatch="/",color="grey")


df_inference_discovery = df[df["Task"]!="both"]
model_counts = df_inference_discovery['Model'].value_counts()
ax.barh(model_counts.index, model_counts.values-0.015, height=0.78, hatch="\\")

df_temp = df.groupby(["Model","Task"]).size()
print(df_temp)

df_inference = df[df["Task"]=="inference"]
model_counts = df_inference['Model'].value_counts()
ax.barh(model_counts.index, model_counts.values-0.015, height=0.78, hatch=".")
plt.xlabel('# of papers')
plt.ylabel('Framework')

plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.xticks(range(0,60,5))

df_temp = df.groupby(["Model","Task"]).size()
print(df_temp)

plt.legend(["total","both","discovery","inference"])

# ax.barh(task_counts.index, model_counts.values)
# plt.xlabel('Count')
# plt.ylabel('Model')
# # plt.title('Model Distribution')
# # plt.xticks(rotation=0)
# plt.grid(axis="x", color="white")
# plt.show()
plt.xlim([0,58])
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
fig.tight_layout()
# plt.show()
fig.savefig('images/cr_model.pdf')