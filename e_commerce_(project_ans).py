# -*- coding: utf-8 -*-
"""E-commerce (project ANS).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JqcK1WQAP5qH0G9G978TGHxRlHlLH_it

#**Linear Regression Project**
 
***Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home and order either on a mobile app or website for the clothes they want.***

***The company is trying to decide whether to focus their efforts on their mobile app experience or their website. They've hired you on contract to help them figure it out! Let's get started!***

***Just follow the steps below to analyze the customer data (it's has some bogus data, don't worry I didn't give you real credit card numbers or emails).***

##**Required libraries**
**Numpy**
   
   **Pandas**

**Matplotlib**

**Seaborn**

**Sklearn**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

"""##Loding dataset"""

data = pd.read_csv('/Ecommerce Customers.csv')
data.head()

"""##Working with the data
Avg. Session Length: Average session of in-store style advice sessions.

Time on App: Average time spent on App in minutes

Time on Website: Average time spent on Website in minutes

Length of Membership: How many years the customer has been a member.
"""

data.describe()

data.info()

data.columns

"""##Exploratory Data Analysis
Let's explore the data!

Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.
"""

sb.jointplot(x='Time on Website',y='Yearly Amount Spent',data=data)

"""Time on App and Yearly Amount Spend Analysis"""

sb.jointplot(x='Time on App',y='Yearly Amount Spent', data = data)

"""Time on App and Length of Membership analysis"""

sb.jointplot(x='Time on App',y='Length of Membership',data=data, kind = 'reg')

"""Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below."""

sb.pairplot(data)

sb.lmplot(x='Length of Membership',y='Yearly Amount Spent',data = data)

"""##Training and Testing Data
Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets. Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column.
"""

x = data[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]
y = data['Yearly Amount Spent']

"""Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101"""

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y = train_test_split(x, y, test_size = 0.3, random_state=101)

"""###Training the Model
Now its time to train our model on our training data!

Create an instance of a LinearRegression() model named ml.

Train/fit lm on the training data.

Print out the coefficients of the model
"""

from sklearn.linear_model import LinearRegression
ml=LinearRegression()
ml.fit(train_x,train_y)
print(ml.coef_)

"""Predicting Test Data

Now that we have fit our model, let's evaluate its performance by predicting off the test values!

Create a scatterplot of the real test values versus the predicted values.
"""

prdins = ml.predict(test_x)
plt.scatter(test_y,prdins)
plt.xlabel("Test y")
plt.ylabel("Predictions ")

"""###Evaluating the Model
Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas
"""

import sklearn.metrics as skm
a=skm.mean_absolute_error(test_y,prdins)
b=skm.mean_squared_error(test_y,prdins)
c=np.sqrt(b)
print("MAE: ",a,"\nMSE: ",b,"\nRMSE: ",c)

"""###Residuals
You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data.

Plot a histogram of the residuals and make sure it looks normally distributed.
"""

sb.distplot(test_y-prdins)

"""##Conclusion
**We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important. Let's see if we can interpret the coefficients at all to get an idea.**

Recreate the dataframe below.
"""

df=pd.DataFrame(ml.coef_,x.columns,columns=['cofficients'])
df

"""**Given that the coefficients are all positive, for every unit change in the features, the average yearly spend increases by the coefficient holding all other features fixed. In this case, the most important factor seems to be the length of membership of a customer.**

**Should the company focus more on their mobile app or on their website?**

**If the company really needs to choose now between the two, they should focus more on their mobile app as it has a bigger influence on yearly spend based on the length of time the customers spend on it. It would be also good to explore the relationship between how long a customer has been a member (length of membership) and the time they spend on the app and website. That might yield some better conclusions and action plans for the company.**

How can you interpret these coefficients?

The greater the value the more related it is to the target, in this case yearly amount spent

Do you think the company should focus more on their mobile app or on their website?

The company should focus on the mobile app
"""