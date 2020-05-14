import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax=plt.subplot()
ax.set_xticks([i for i in range(len(drinks))])
ax.set_xticklabels(drinks,rotation=30)

plt.show()
