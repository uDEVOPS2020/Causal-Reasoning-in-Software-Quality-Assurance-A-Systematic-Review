import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter
from matplotlib import colors
import seaborn as sns

df = pd.read_csv("lifecycle_phase.csv")
num_fl = df.value_counts("Phase").reset_index()[0]
print(num_fl)

plt.figure(figsize=(20,6))
plt.rcParams.update({'font.size': 25})

sns.histplot(data=df, x="Phase")

plt.ylabel("# of papers")

plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.ylim([0,30])


plt.text(0-0.05,  num_fl[3]+0.1, str(num_fl[3]),rotation=0)
plt.text(1-0.05,  num_fl[4]+0.1, str(num_fl[4]),rotation=0)
plt.text(2-0.05,  num_fl[0]+0.1, str(num_fl[0]),rotation=0)
plt.text(3-0.05,  num_fl[2]+0.1, str(num_fl[2]),rotation=0)
plt.text(4-0.05,  num_fl[1]+0.1, str(num_fl[1]),rotation=0)

plt.tight_layout()
plt.savefig('phases_hist.pdf')