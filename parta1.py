## Part A Task 1
import pandas as pd
import sys
covidData = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1')

#Removing dates that are not in 2020 and creating a numeric month column
covidData['date'] = pd.to_datetime(covidData['date'])
covidData = covidData[~(covidData['date'] > '2020-12-31')]
covidData = covidData[~(covidData['date'] < '2020-1-01')]
covidData['month'] = covidData['date'].dt.strftime('%m')

#Taking the aggregate for new cases/deaths (sum) and total cases/deaths (max) then calculating the new case fatality rate
covidData = covidData.loc[:,['location', 'month', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
covidDataResults = covidData.groupby([covidData['location'], covidData['month']]).agg({'total_cases':max, 'new_cases':sum, 'total_deaths':max, 'new_deaths':sum})
covidDataResults.insert(0,'case_fatality_rate', covidDataResults['new_deaths']/covidDataResults['new_cases'])

#Sorting by location then month and saving to csv
covidDataResults.sort_values(['location', 'month'], ascending=[True, True])
print(covidDataResults.head(5))
covidDataResults.to_csv(sys.argv[1])