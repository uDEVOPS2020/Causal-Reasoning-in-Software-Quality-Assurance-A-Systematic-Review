import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# plt.rcParams["font.family"] = "Times New Roman"
fontsize = 25

# TASK
df = pd.read_csv("data/results_MAJOR_RQ2_cd.csv")
task_counts = df['Category'].value_counts()

print(task_counts)

fig, ax = plt.subplots(figsize=(8,8))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
ax.pie(task_counts, explode=explode, labels=task_counts.index, colors = ["tab:blue","tab:blue","tab:blue","tab:blue", "tab:blue", "tab:blue"], autopct='%1.1f%%', startangle=90, textprops={'fontsize': fontsize})
ax.axis('equal')
fig.tight_layout()
# plt.show()
fig.savefig('images/cr_cd.pdf',bbox_inches='tight', dpi=1000)


# # MODEL
# df = pd.read_csv("model.txt")
# df['model'] = df['model'].str.split('-')
# df = df.explode('model')

# model_counts = df['model'].value_counts()

# fig, ax = plt.subplots(figsize=(8,3))
# ax.barh(model_counts.index, model_counts.values)
# plt.xlabel('Count', fontsize=fontsize)
# plt.ylabel('Model', fontsize=fontsize)
# # plt.title('Model Distribution')
# plt.xticks(rotation=0, fontsize=fontsize)
# plt.grid(axis="x", color="white")
# plt.show()

# fig.tight_layout()
# # plt.show()
# fig.savefig('images/cr_model.pdf',bbox_inches='tight', dpi=1000)


# CD ALGO
# df = pd.read_csv("cd_algo.txt")
# df['cd_algo'] = df['cd_algo'].str.split('-')
# df = df.explode('cd_algo')

# model_counts = df['cd_algo'].value_counts()

# fig, ax = plt.subplots(figsize=(5,3))
# ax.barh(model_counts.index, model_counts.values)
# plt.xlabel('Count', fontsize=fontsize)
# plt.ylabel('CD Algorithm', fontsize=fontsize)
# plt.xticks(range(min(model_counts.values), max(model_counts.values)+1), fontsize=fontsize)
# plt.grid(axis="x", color="white")
# plt.show()

# fig.tight_layout()
# # plt.show()
# fig.savefig('images/cr_cd_algo.pdf',bbox_inches='tight', dpi=1000)

# CD ESTIM
# df = pd.read_csv("estimation.txt")
# # df['estimation'] = df['estimation'].str.split('-')
# df = df.explode('estimation')

# model_counts = df['estimation'].value_counts()

# fig, ax = plt.subplots(figsize=(4,3))
# ax.barh(model_counts.index, model_counts.values)
# plt.xlabel('Count', fontsize=fontsize)
# plt.ylabel('Estimation', fontsize=fontsize)
# plt.xticks(range(min(model_counts.values), max(model_counts.values)+1), fontsize=fontsize)
# plt.grid(axis="x", color="white")
# plt.show()

# fig.tight_layout()
# # plt.show()
# fig.savefig('images/cr_cd_estimation.pdf',bbox_inches='tight', dpi=1000)