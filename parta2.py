## Part A Task 2
import pandas as pd
import sys
import matplotlib.pyplot as plt

covidData = pd.read_csv('owid-covid-data-2020-monthly.csv',encoding = 'ISO-8859-1')
#Finding the total number of cases and deaths for a location
covidDataResults = covidData.groupby([covidData['location']]).agg({'total_deaths':max, 'total_cases':max})
#Calculate the fatality rate of the year 2020
fatalityRate = covidDataResults['total_deaths']/covidDataResults['total_cases']
covidDataResults.insert(0,'case_fatality_rate',fatalityRate)

#Drop regions and continents to compare countries
covidDataResults = covidDataResults.drop(['Africa', 'International', 'Asia', 'North America', 'Oceania', 'South America', 'Europe', 'European Union', 'World'])

#Plotting with linear scaling
plt.scatter(covidDataResults.iloc[:,2], covidDataResults.iloc[:,0], s=8)

#Removing far outliers to better intepret data
plt.xlim(-0.3,2.8e6)
plt.ylim(0,0.1)
plt.xlabel("Total Cases")
plt.ylabel("Fatality Rate")
plt.grid(True)
plt.savefig(sys.argv[1])

plt.close()

#Plotting with logarithmic scaling for total cases (x)
ax = plt.gca()
ax.set_xscale('log')
plt.scatter(covidDataResults.iloc[:,2], covidDataResults.iloc[:,0], s=8)
plt.xlabel("Total Cases")
plt.ylabel("Fatality Rate")

#Removing far outliers to better intepret data
plt.ylim(0,0.1)
plt.grid(True)
plt.savefig(sys.argv[2])