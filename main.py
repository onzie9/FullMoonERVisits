import pandas as pd

#df = pd.read_excel('/Users/trevormcguire/Downloads/neiss2017.xlsx')

#df1 = df[['Treatment_Date', 'Age', 'Sex', 'Race', 'Location']]

#df1.to_csv('injurydatesetc.csv')

df = pd.read_csv('injurydatesetc.csv')

dates = df['Treatment_Date'].value_counts()

df1 = pd.DataFrame({'Treatment_Date':dates.index, 'Count':dates.values})
df1 = df1.sort_values('Treatment_Date')

date_list = df1['Count'].tolist()
