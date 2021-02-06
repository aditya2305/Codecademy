import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Scrapping Webpage to get data
index = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(index.content,'html.parser')

#Creating a list of ratings
ratings = soup.find_all(attrs={'class':'Rating'})
rating_list =[]
for rating in ratings:
  rating_list.append(rating.string)
rating_list.remove('Rating')
rating_list = [float(x) for x in rating_list]

#Histogram showing ratings
plt.hist(rating_list)
plt.title('Chocolate Ratings')
plt.show()

#Creating a list of companies
companies =  soup.find_all(attrs={'class':'Company'})
company_list = []
for company in companies:
  company_list.append(company.string)
company_list.pop(0)

#Creating a list of cocoa percentage used
cocoa = soup.find_all(attrs={'class':'CocoaPercent'})
cocoaperc = []
Cocoa_Percent = []
for i in cocoa:
  data = i.string.strip('%')
  cocoaperc.append(data)
cocoaperc.pop(0)
for j in cocoaperc:
  Cocoa_Percent.append(float(j))

#Creating a dataframe for better analysis
df = pd.DataFrame({
  'Company': company_list,
  'Rating' : rating_list,
  'Cocoa Percent': Cocoa_Percent
})

#To find top 10 best rated companies
df_new = df.groupby('Company').Rating.mean().reset_index()
print(df_new.Rating.nlargest(10))


#Scatter plot for the dataframe 'df'
plt.scatter(df['Cocoa Percent'],df['Rating'])
z = np.polyfit(df['Cocoa Percent'], df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df['Cocoa Percent'], line_function(df['Cocoa Percent']), "r--")
plt.show()

