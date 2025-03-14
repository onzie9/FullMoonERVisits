import pandas as pd
import matplotlib.pyplot as plt
import copy
import math
import datetime


def get_lunar_day(input_date: datetime, new_moon_date: datetime.datetime = datetime.datetime(2016, 12, 29)) -> float:
    delta_days = (input_date - new_moon_date).days
    lunar_day = delta_days % 29.53
    return lunar_day


def moon_illumination(d: float) -> float:
    return 1-.5*(1 + math.cos(2*math.pi*d/29.53))


def round_to_nearest_05(value):
    if value > 1:
        value = 2 - value
    return round(value * 20) / 20.0

# Pull in injury data.
df = pd.read_csv('injurydatesetc.csv')

dates = df['Treatment_Date'].value_counts()

df1 = pd.DataFrame({'Treatment_Date':dates.index, 'Count':dates.values})
df1 = df1.sort_values('Treatment_Date')

date_list = df1['Count'].tolist()

# Pull in lunar phase data as a percentage of illumination.
phases = pd.read_csv('phases.csv')
phases['Count'] = date_list
phases['five_percent_illumination'] = phases['Phase'].apply(round_to_nearest_05)

percent_grouped = phases[['Count', 'five_percent_illumination']].groupby('five_percent_illumination').sum()
plt.scatter(percent_grouped.index, percent_grouped['Count'])
plt.xlabel('Percentage of Lunar Illumination')
plt.ylabel('Number of ER Visits')
plt.title('Number of ER Visits Compared with Lunar Illumination')
plt.show()

# To get an accurate measure of the ER visits during lunar phases, we will use a lunar illumination formula that takes
# the day of the cycle as the input and outputs the percentage of illumination.

phases_scaled = copy.deepcopy(phases)

# Create the 'actual_illumination' column by using the indices to pull values from phase_list
phases_scaled['datetime_column'] = pd.to_datetime(phases['Date'], format='%m/%d/%y')
phases_scaled['day_of_cycle'] = phases_scaled['datetime_column'].apply(get_lunar_day)
phases_scaled['actual_illumination'] = phases_scaled['day_of_cycle'].apply(moon_illumination)

phases_scaled_grouped = phases_scaled[['Count', 'actual_illumination']].groupby('actual_illumination').sum()
plt.scatter(phases_scaled_grouped.index, phases_scaled_grouped['Count'])
plt.xlabel('Percentage of Lunar Illumination')
plt.ylabel('Number of ER Visits')
plt.title('Number of ER Visits Compared with Lunar Illumination')
plt.show()
