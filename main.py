"""In this code I am defining linear regression from the scratch  """

#importing nessesary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading csv file to input data
df = pd.read_csv("data/Salary_dataset.csv")

"""This part of code define gradient descent 
   gradient descent : In this we are trying to achive local minima 
   of the curve between the cost fuction and w,b"""
def gradient_descent(w , b , df , lr = 0.001 , epochs = 300):
    x = df["YearsExperience"]
    y = df["Salary"]
    n = len(df)

    for i in range(epochs):
        dw = ((((w*x - b) - y)*x).sum())/n
        db = ((((w*x - b) - y)).sum())/n

        w = w - lr*dw
        b = b - lr*db
    return w , b
#predicting Output
def Linear_regression(df , x):
    w = gradient_descent(0.00 , 0.00 , df )[0]
    b = gradient_descent(0.00 , 0.00 , df )[1]
    return (w*x + b)

n = len(df)
lst = []
for i in range(n):
    lst.append(Linear_regression(df , df.iloc[i]["YearsExperience"]))

plt.scatter(df["YearsExperience"],df["Salary"])
plt.plot(df["YearsExperience"], lst)
plt.show()