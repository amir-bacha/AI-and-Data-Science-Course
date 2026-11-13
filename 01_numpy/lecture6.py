import numpy as np
marks=[70,80,90]
# method 1  to add 5 to each element
new_marks=[]

for i in marks:
    new_marks.append(i+5)

# but numpy provide a much simpler way 
marks=np.array([70,80,90])
print(marks)
marks=marks+5
print(marks)
# Problem 1.  Temprature in celsius. Task: Convert to Fhrenheit using F=c*9/5+32
celsius=np.array([0,10,20,30,40])
print(celsius.shape)
Temprature_in_Fahrenheit=celsius* 9/5+32
print(Temprature_in_Fahrenheit)
print(Temprature_in_Fahrenheit.shape)

# problem2: Student bonus marks
marks=np.array([
    [40,44,56],
    [70,75,85],
    [60,65,45]
])
bonus=5
marks=marks+bonus
print(marks)
#problem : 3  months with expanses of three different categaries
expanses=np.array([
    [4000,5000,3000], # each row is month and each column is category
    [2000,2900,3100],
    [1900,2700,2300],
])
additional_expanses=np.array([[100,0,0]]) # Only category 1 increase by 100
print(expanses.shape)
print(expanses.shape)
expanses=expanses+additional_expanses
print(expanses)
twoMonthstax=np.array([[100,200,500],[340,400,600]])
print(twoMonthstax.shape)
expanses=expanses[0:2,:]+twoMonthstax
print(expanses)
# problem : 4 University student Garading system
marks=np.array([
    [70,80,90],
    [60,75,85],
    [90,95,88],
])
weights=np.array([0.2,0.3,0.5])
print(marks)
print(marks.shape)
print(weights)
print(weights.shape)
weighted_Score=marks*weights
print(weighted_Score)
print(weighted_Score.shape)
final_Score=weighted_Score.sum(axis=1)
print(final_Score)