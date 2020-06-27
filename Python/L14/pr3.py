import matplotlib.pyplot as plt
import numpy as np

products=['Laptop','Printer','Router']
reena=[10,25,15]
veena=[5,30,12]

x=np.arange(len(products))
plt.bar(x,reena,width=0.30)
plt.bar(x+0.30,veena,width=0.30)
plt.xticks(x,products)

plt.show()
