#Question7:What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) 
#by considering missing values imputed version of dataset? Please  just provide the number as answer.
'''with open("country_vaccination_stats.csv","r") as f:
    counter=0
    for line in f:
        tokens=line.split(',')
        country=tokens[0]
        date=tokens[1]
        daily_vaccinations=tokens[2]
        vaccines=tokens[3]
        if date=="1/6/2021":
            counter+=1 
    print(counter)'''
#Question6:Implement code to list the top-3 countries with highest median daily vaccination numbers 
#by considering missing values imputed version of dataset.
'''import pandas as pd
file = pd.read_csv("country_vaccination_stats.csv")
file['daily_vaccinations'] = file.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.median()))
median = file.groupby('country')['daily_vaccinations'].median()
countries = median.sort_values(ascending=False).head(3)
print(countries)'''

#Question4,5:Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  
'''import pandas as pd
file = pd.read_csv("country_vaccination_stats.csv")
file['daily_vaccinations'] = file['daily_vaccinations'].fillna(0)
file['daily_vaccinations'] = file.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(x.min()))'''