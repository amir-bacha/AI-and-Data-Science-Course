
import numpy as np
marks=np.array([60,70,40,45])
TotalSum=np.sum(marks)
print(TotalSum) # it returns the total sum 215
print(np.min(marks)) # 40
print(np.max(marks)) # 70
avarage=TotalSum / 4
print('Calculated avarage : ', avarage)
print(np.mean(marks))
