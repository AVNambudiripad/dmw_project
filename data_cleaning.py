import pandas as pd
files = ['PC_Export_2014_2015.csv', 'PC_Export_2015_2016.csv', 'PC_Export_2016_2017.csv']
textiles = ["Cotton Yarn","Cotton Fabrics, Madeups Etc.","Oth Txtl Yrn, Fbric Mdup Artcl","Silk,Raw","Natrl Silk Yarn,Fabrics,Madeup","Manmade Yarn,Fabrics,Madeups","Wool, Raw","Wollen Yarn,Fabrics,Madeupsetc","Rmg Cotton Incl Accessories","Rmg Silk","Rmg Manmade Fibres","Rmg Wool","Rmg Of Othr Textle Matrl","Coir And Coir Manufactures","Handloom Products","Silk Waste","Jute, Raw","Jute Yarn","Jute Hessian","Floor Cvrng Of Jute","Other Jute Manufactures","Handcrfs(Excl.Handmade Crpts)","Carpet(Excl. Silk) Handmade","Silk Carpet","Cotton Raw Incld. Waste"]
columns = ['pc_code','pc_description','country_code','country_name','value']

for file in files:
    print('Filename is ',file)
    df = pd.read_csv(file, usecols= columns)
    print('Total rows: ',len(df))
    NAs = ['NA', 'Na', 'Unspecified', 0, '0']
    rowsToDrop = []
    for i in range(len(df)):
        if df.at[i,'pc_description'] not in textiles:
            rowsToDrop.append(i)
        else:
            for col in columns:
                if df.at[i,col] in NAs:
                    rowsToDrop.append(i)
            
    df.drop(labels=rowsToDrop, inplace=True)
    print("Total rows after removing noise: ",len(df), "\n")
    newFileName = 'cleaned_'+file
    df.to_csv(newFileName, index=False)