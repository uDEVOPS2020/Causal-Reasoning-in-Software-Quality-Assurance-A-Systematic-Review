import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.ticker import MaxNLocator

plt.rcParams.update({'font.size': 25})

df_task = pd.read_csv("data/task.txt")
task_counts = df_task['task'].value_counts()

df_model = pd.read_csv("data/model.csv")
df_model['Model'] = df_model['Model'].str.split(';')
df_model = df_model.explode('Model')

model_counts = df_model['Model'].value_counts()

fig, ax = plt.subplots(figsize=(17, 5))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

ax.barh(model_counts.index, model_counts.values, color="grey", height=0.78)

df_inference_discovery = df_model[df_model["Task"] != "both"]
model_counts_id = df_inference_discovery['Model'].value_counts()
ax.barh(model_counts_id.index, model_counts_id.values, height=0.78)

df_inference = df_model[df_model["Task"] == "inference"]
model_counts_inf = df_inference['Model'].value_counts()
ax.barh(model_counts_inf.index, model_counts_inf.values, height=0.78)

plt.xlabel('# of papers')
plt.ylabel('Framework')

plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
plt.xticks(range(0, 60, 5))
plt.xlim([0, 58])

for i, (model, count) in enumerate(model_counts.items()):
    ax.text(count + 1, i, str(count), va='center', fontsize=25)

plt.legend(["Total", "Both", "Discovery", "Inference"])

fig.tight_layout()
plt.savefig('images/cr_model.pdf')
plt.show()
