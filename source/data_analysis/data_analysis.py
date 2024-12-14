import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder

l_encoder = preprocessing.LabelEncoder()

data = np.array(["kissa", "koira", "kissa", "marsu", "koira", "koira", "kissa", "koira", "kissa", "koira"])
l_encoder.fit(data)

print(list(l_encoder.classes_))

labels = l_encoder.transform(data)
print(labels)



import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Data
data = np.array(["kissa", "koira", "kissa", "marsu", "koira", "koira", "kissa", "koira", "kissa", "koira"]).reshape(-1, 1)

# Initialize OneHotEncoder without 'drop' option (no binary drop handling here)
onehot = OneHotEncoder( handle_unknown='ignore')

# Fit the encoder and transform the data
numeric_data = onehot.fit_transform(data)

# Output categories (unique values)
print("Categories (unique values):")
print(onehot.categories_)

# Output one-hot encoded data
print("\nOne-hot encoded data:")
print(numeric_data)
