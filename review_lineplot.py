import codecademylib
from matplotlib import pyplot as plt
x=range(15)
y1=[i**2 for i in x]
y2=[j**3 for j in x]
plt.plot(x,y1,color='pink',marker='o')
plt.plot(x,y2,color='gray',marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(['y1','y2'],loc=5)
plt.axis[0,16,2000,2500]
plt.show()
