from sklearn.datasets import load_iris
from sklearn.datasets import load_digits

iris = load_iris()
X = iris.data
y = iris.target

# Number of samples
no_samples = X.shape[0]

# Number of features
no_features = X.shape[1]

print(f"No. of samples: {no_samples}")
print(f"No. of features: {no_features}")

# Number of unique classes
no_unique_classes = len(set(y))

print(f"No. of unique classes: {no_unique_classes}")

print("    ")
print("----------------------------------------------------------------")
print("    ")
######################################################
###############################
####################################################
#######################
# Load the Digits dataset
digits = load_digits()
X = digits.data
y = digits.target

# Calculate the number of samples and features
no_samples = X.shape[0]
no_features = X.shape[1]

print(f"No. of samples: {no_samples}")
print(f"No. of features: {no_features}")

# Calculate the number of unique classes
no_unique_classes = len(set(y))

print(f"No. of unique classes: {no_unique_classes}")

print(" ")