#wapp to generate randomm movie
import random

Marvel_Movies = ["ironman","antman","dr.strang","avengers","capt.america","civil war","spiderman","hanuman"]
r1= random.randrange(len(Marvel_Movies))
print(Marvel_Movies[r1])

r2=random.randint(0,len(Marvel_Movies)-1)
print(Marvel_Movies[r2])