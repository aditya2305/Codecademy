import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

fig1 = plt.figure()
ax1 = plt.subplot()
plt.bar(range(len(games)),viewers, color ='slateblue')
ax1.set_xticks(range(len(games)))
ax1.set_xticklabels(games, rotation=90)
plt.title('Top Games')
plt.ylabel('Viewers')
plt.xlabel('Games')
plt.legend(['Twitch'])
plt.show()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
fig2 = plt.figure()
ax2=plt.subplot()
plt.pie(countries,labels=labels,colors=colors,explode=explode,shadow=True)
plt.legend(labels)
plt.axis('equal')
plt.show()
# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

upper = [i*1.15 for i in viewers_hour]
lower=[i*0.85 for i in viewers_hour]
fig3 = plt.figure()
ax3 = plt.subplot()
plt.plot(hour,viewers_hour)
plt.fill_between(hour, lower, upper, alpha=0.2)
ax3.set_xticks(hour)
ax3.set_xticklabels(hour)
plt.title('Viewers Per Hour')
plt.ylabel('Viewers')
plt.xlabel('Hours')
plt.show()