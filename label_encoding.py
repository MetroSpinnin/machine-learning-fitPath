# Author: Samuel Jim Nnamdi
# Title: Fill empty columns in the dataset

# ...
# Import the required libraries
# ...

# Perform label encoding on the target Data

categorical_cols = category_columns= ['workclass', 'race', 'education','marital-status', 'occupation']
label_encoder = preprocessing.LabelEncoder()

# Map each category to a Numerical Value

mapping_dict = {}
for col in categorical_cols:
	read_dataset[col] = label_encoder.fit_transform(read_dataset[col])
	le_name_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
mapping_dict = le_name_mapping              