# Author: Samuel Jim Nnamdi
# Title: Fill empty columns in the dataset

# ...
# Import the required libraries
# ...

# Get the dataset
get_dataset = "dataset/adult.csv"

# Read the dataset
read_dataset = pandas.read_csv(get_dataset)

'''
	Fill up the empty rows and columns with the modal value
	of that particular row or column
'''

for col in read_dataset:
	read_dataset[col] = read_dataset[col].replace('?', numpy.NaN)
	read_dataset = read_dataset.apply(lambda x: x.fillna(x.value_counts().index[0]))