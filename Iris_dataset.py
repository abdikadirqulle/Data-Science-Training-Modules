import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Data Preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model tranning
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Define the sample input
x1 = np.array(
    [5.6, 2.9, 3.6, 1.3]
)

# Predict the class
y1 = model.predict([x1])[0]

# Map the predicted class to the class name
name = iris.target_names[y1]

#print name +  predicted class
print(f"Predicted class: {y1}")
print(f"Predicted class name: {name}")