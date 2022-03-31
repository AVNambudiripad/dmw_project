from numpy import minimum
import pandas as pd
files = ['cleaned_PC_Export_2014_2015.csv','cleaned_PC_Export_2015_2016.csv','cleaned_PC_Export_2016_2017.csv']

for file in files:
    df = pd.read_csv(file)
    maximum = df['value'].max()
    minimum = df['value'].min()
    # print(df.loc[df['value'].idxmax()])
    # print(df.loc[df['value'].idxmin()])
    for i in range(len(df)):
        df.at[i,'value'] = int(round(100000*(df.at[i,'value'] - minimum)/(maximum-minimum)))
    newFileName = 'normalised_'+file[8:]
    df.to_csv(newFileName, index=False)