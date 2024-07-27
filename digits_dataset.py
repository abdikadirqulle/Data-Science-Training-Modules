import numpy as np

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_digits()

X = digits.data

y = digits.target

# Data Preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#model tranning
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)


x1 = np.array(
    [ 0., 0., 2., 12., 12., 12., 9., 2., 0., 0., 9., 15., 12.,  13., 16., 5., 0., 0., 12., 8., 0., 8., 10., 0., 0., 1.,  16., 3., 3., 15., 2., 0., 0., 1., 3., 0., 12., 7., 0.,  0., 0., 0., 0., 4., 13., 0., 0., 0., 0., 0., 0., 13.,  9., 0., 0., 0., 0., 0., 3., 15., 3., 0., 0., 0.]
)

y1 = model.predict([x1])[0]

print(f"Predicted class:: {y1}")
