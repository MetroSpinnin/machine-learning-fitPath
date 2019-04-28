# Author: Samuel Jim Nnamdi
# Title: Fill empty columns in the dataset

# ...
# Import the required libraries
# ...

# Perform Data discretization and make data easy
# to read and Understand more clearly

read_data.replace(['Divorced','Married-AF-spouse','Married-civ-spouse','Married-spouse-absent','Never-married','Separated','Widowed'],['divorced','married','married','married','not married','not married','not married'], inplace=True)