import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("job_demand.csv")
lang=data['LANGUAGE'].tolist()
job_2017=data['JOBS_2017'].tolist()
job_2018=data['JOBS_2018'].tolist()

x=np.arange(len(lang))
plt.bar(x,job_2017,label='JOB_2017',width=0.3)
plt.bar(x+0.3,job_2018,label='JOB_2018',width=0.3)

plt.title("Job DEmand")
plt.xlabel("Languages")
plt.ylabel("Jobs")
plt.xticks(x,lang)
plt.legend()
plt.grid()
plt.show()