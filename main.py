import matplotlib.pyplot as plt
%matplotlib inline

x = [1,2,3,4,5,6,7]
y = [51,52,53,50,48,49,46]

plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='blue',alpha=0.1)
