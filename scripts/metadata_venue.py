import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

fontsize = 25

df_orig = pd.read_csv("data/results.csv")

df = df_orig.explode('Document Type')

model_counts = df['Document Type'].value_counts()

print (model_counts)

fig, ax = plt.subplots(figsize=(8,8))
explode = (0.1, 0.1, 0.1) 
ax.pie(model_counts, explode=explode, labels=model_counts.index, colors = ["tab:blue","tab:blue","tab:blue"], autopct='%1.1f%%', startangle=90, textprops={'fontsize': fontsize-5})
ax.axis('equal')
fig.tight_layout()
fig.savefig('images/metadata_venue.pdf',bbox_inches='tight', dpi=1000)

df_conference = df_orig[df_orig["Document Type"]=="Conference paper"]

model_counts = df_conference['Acronym'].value_counts()
model_counts = model_counts[model_counts >= 2]

print (model_counts)

fig, ax = plt.subplots(figsize=(10,4))
ax.barh(model_counts.index, model_counts.values)
plt.xlabel('# of papers', fontsize=fontsize)
plt.ylabel('Conference', fontsize=fontsize)
plt.xticks(range(0, max(model_counts.values)+1,2), fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.grid(axis="x", color="white")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

fig.tight_layout()
fig.savefig('images/metadata_conference.pdf',bbox_inches='tight', dpi=1000)


df_journal = df_orig[df_orig["Document Type"]=="Journal paper"]

model_counts = df_journal['Source title'].value_counts()
model_counts = model_counts[model_counts >= 2]
print (model_counts)

fig, ax = plt.subplots(figsize=(10,4))
ax.barh(model_counts.index, model_counts.values)
plt.xlabel('# of papers', fontsize=fontsize)
plt.ylabel('Journal', fontsize=fontsize)
plt.xticks(range(0, max(model_counts.values)+1,1), fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.grid(axis="x", color="white")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

fig.tight_layout()
fig.savefig('images/metadata_journal.pdf',bbox_inches='tight', dpi=1000)