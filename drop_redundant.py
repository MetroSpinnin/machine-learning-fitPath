# Author: Samuel Jim Nnamdi
# Title: Fill empty columns in the dataset

# ...
# Import the required libraries
# ...

# Drop redundant columns

read_data=read_data.drop(['fnlwgt','educational-num'], axis=1)
read_data.head()