import codecademylib
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]
x_range=[i*0.1 for i in range(-5,65,5)]
y_range=[j for j in range(70,95)]
# Make your chart here
plt.figure(figsize=(10,8))
ax=plt.subplot()
plt.bar(range(len(years)),past_years_averages,yerr=error,capsize=5)
#ax.set_xticks(x_range)
#ax.set_yticks(70,95)
plt.axis([-0.5,6.5,70,95])
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test average')
plt.show()
plt.savefig('my_bar_chart.png')
