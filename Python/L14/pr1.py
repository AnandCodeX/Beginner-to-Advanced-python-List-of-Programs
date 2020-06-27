#Python progeam for line plot 
import matplotlib.pyplot as plt

months=['jun','july','aug','sep','oct','nov','dec']
mumbai=[82.5,83.06,83.61,85.6,90.75,85.24,84.06]
plt.plot(months,mumbai,linewidth=3,marker='o',markersize=10,label='Mumbai')
plt.title("Petrol Prices")
plt.xlabel("months")
plt.ylabel("prices")
plt.grid()
plt.legend()
plt.show()