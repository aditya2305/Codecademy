import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head())
life_expectancy = data['Life Expectancy'].values
gdp = data['GDP'].values
median_gdp = np.quantile(gdp,0.5)
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25,0.50,0.75])
print(life_expectancy_quartiles)
low_gdp = data[data['GDP'] <=median_gdp]
high_gdp = data[data['GDP']>=median_gdp]
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'],[0.25,0.50,0.75])
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],[0.25,0.50,0.75])
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()
