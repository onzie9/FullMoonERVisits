import pandas as pd
from main import date_list
import numpy as np
import operator
import matplotlib.pyplot as plt

phases = pd.read_csv('phases.csv')
phases['Count'] = date_list

unique_phases = phases['Phase'].value_counts()

df1 = pd.DataFrame({'Phase': unique_phases.index, 'Count': unique_phases.values})
df1 = df1.sort_values('Phase')

phase_percents = [0.0717831, 0.0306332, 0.0241753, 0.020992, 0.019083, 0.0178384, 0.0170016, 0.0164462, 0.016105,
                  0.0159421, 0.0159421, 0.016105, 0.0164462, 0.0170016, 0.0178384, 0.019083, 0.020992, 0.0241753,
                  0.0306332, 0.0717831]
# These numbers represent the percentage of the ~28 day lunar cycle spent within
# 5% phase intervals.  That is, 7.17831% of the entire cycle is spent within 5%
# of new (after the new moon) and 1.78384% is spent between 25% and 30% phase
# after the new moon. The cycle is repeated in reverse from full to new.

for i in range(len(phase_percents)):
    phase_percents.append(phase_percents[i])


percents = [0, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95, 1, 1.05, 1.1, 1.15,
            1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]
phase_counts = df1['Phase'].value_counts()

phase_list = df1['Phase'].tolist()

merged = phases.merge(df1, on='Phase')


# new_list2 gives the counts of injuries within each 5% phase interval along with the percentage itself.

new_list2 = []
for j in range(len(phase_percents)):
    x = 0
    for i in range(365):
        if merged.iloc[i]['Phase'] >= percents[j] and merged.iloc[i]['Phase'] < percents[j+1]:
            x += merged.iloc[i]['Count_x']
    new_list2.append([percents[j], x])

# scaledtotal gives the number of injuries one could expect in an interval if all the intervals had the same length.

scaledtotal = []
for i in range(len(new_list2)):
    scaledtotal.append(new_list2[i][1]/phase_percents[i])

# Plot scaledtotal against phase.

ls1 = new_list2
lsx = []
lsy = []
for i in range(len(new_list2)):

    #ls1[i][1] = new_list3[i][1]
    ls1[i][1] = scaledtotal[i]
    lsx.append(ls1[i][0])
    lsy.append(ls1[i][1])

plt.plot(lsx, lsy)
plt.show()
