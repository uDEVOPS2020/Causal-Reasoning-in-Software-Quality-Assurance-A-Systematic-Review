import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

fontsize = 25

# CD ALGO
df_cd = pd.read_csv("data/cd_algo.txt")
df_cd = df_cd.explode('cd_algo')

model_counts_cd = df_cd['cd_algo'].value_counts()

fig, ax = plt.subplots(figsize=(10, 8))
bars_cd = ax.barh(model_counts_cd.index, model_counts_cd.values)
plt.xlabel('# of papers', fontsize=fontsize)
plt.ylabel('CD Algorithm', fontsize=fontsize)
plt.xticks(range(min(model_counts_cd.values), max(model_counts_cd.values) + 1), fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.grid(axis="x", color="white")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

for bar in bars_cd:
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
            f'{int(bar.get_width())}', va='center', fontsize=fontsize)

fig.tight_layout()
fig.savefig('images/cr_cd_algo.pdf', bbox_inches='tight', dpi=1000)

# CI ALGO
df_ci = pd.read_csv("data/ci_algo.txt")
df_ci = df_ci.explode('ci_algo')

model_counts_ci = df_ci['ci_algo'].value_counts()

fig, ax = plt.subplots(figsize=(15, 4))
bars_ci = ax.barh(model_counts_ci.index, model_counts_ci.values)
plt.xlabel('# of papers', fontsize=fontsize)
plt.ylabel('CI Method', fontsize=fontsize)
plt.xticks(range(min(model_counts_ci.values), max(model_counts_ci.values) + 1, 2), fontsize=fontsize)
plt.yticks(fontsize=fontsize)

plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.grid(which='both', axis="x", color="white")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

for bar in bars_ci:
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
            f'{int(bar.get_width())}', va='center', fontsize=fontsize)

fig.tight_layout()
fig.savefig('images/cr_ci_algo.pdf', bbox_inches='tight', dpi=1000)