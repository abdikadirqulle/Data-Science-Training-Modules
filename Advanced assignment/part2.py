import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load the Digits dataset
digits = load_digits()
X = digits.data
y = digits.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# Define the new sample
x1 = np.array(


)

# Predict the class of the new sample
predicted_class = model.predict([x1])[0]

print(f"Predicted class: {predicted_class}")
