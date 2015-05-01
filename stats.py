import pandas as pd
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
meanA = df['Alcohol'].mean()
meanT = df['Tobacco'].mean()
medianA = df['Alcohol'].median()
medianT = df['Tobacco'].median()
modeA = df['Alcohol'].mode()
modeT = df['Tobacco'].mode()
rangeA = max(df['Alcohol']) - min(df['Alcohol'])
rangeT = max(df['Tobacco']) - min(df['Tobacco'])
varA = df['Alcohol'].var()
varT = df['Tobacco'].var()
stdA = df['Alcohol'].std()
stdT = df['Tobacco'].std()
print("The mean alcohol consumption is ") + str(meanA)
print("The mean tobacco consumption is ") + str(meanT)
print("The median alcohol consumption is ") + str(medianA)
print("The median tobacco consumption is ") + str(medianT)
print("The mode alcohol consumption is ") + str(modeA)
print("The mode tobacco consumption is ") + str(modeT)
print("The range of alcohol consumption is ") + str(rangeA)
print("The range of tobacco consumption is ") + str(rangeT)
print("The variance alcohol consumption is ") + str(varA)
print("The variance tobacco consumption is ") + str(varT)
print("The standard devisation alcohol consumption is ") + str(stdA)
print("The standard deviation tobacco consumption is ") + str(stdT)

