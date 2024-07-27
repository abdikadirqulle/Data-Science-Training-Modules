import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the data
iris = load_iris()
X = iris.data
y = iris.target

# Data Preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Define the sample input
x1 = np.array([

 [5.8, 2.7, 3.9, 1.2]

])

# Predict the class
predicted_class = model.predict(x1)[0]

# Map the predicted class to the class name
predicted_class_name = iris.target_names[predicted_class]

print(f"Predicted class: {predicted_class}")
print(f"Predicted class name: {predicted_class_name}")
