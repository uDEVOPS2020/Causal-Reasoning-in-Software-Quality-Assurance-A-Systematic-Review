import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/task.txt")

task_counts = df['task'].value_counts()

print(task_counts)

def autopct_func(pct, task_counts):
    total = sum(task_counts)
    absolute = int(round(pct * total / 100.0))
    return f'{pct:.1f}%\n({absolute:d})'

fig, ax = plt.subplots(figsize=(8,8))
explode = (0.1, 0.1, 0.1) 
ax.pie(task_counts, 
       explode=explode, 
       labels=task_counts.index, 
       colors=["tab:orange", "tab:blue", "tab:grey"], 
       autopct=lambda pct: autopct_func(pct, task_counts), 
       startangle=90, 
       textprops={'fontsize': 25}) 
ax.axis('equal')  

fig.tight_layout()
fig.savefig('images/cr_task.pdf', bbox_inches='tight', dpi=1000)
