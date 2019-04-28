# Author: Samuel Jim Nnamdi
# Title: Fit and train model here

# ...
# Import the required libraries
# ...

'''
	Fit and train the model here, afterwards write
	the file and model which was trained to a file 
	model.pkl which is a binary file, to enable model
	usage always
'''

X = read_data.values[:,:12]
y = read_data.values[:, 12]

# Train the data using SupportVector Algorithm
# Testdata should be 30% -- TrainingData should be 70%

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state=100)# Train the data using SupportVectorClassifier
# Testdata should be 0.3 -- TrainingData should be 0.7

support_vector = SVC()
support_vector.fit(X_train,y_train)
prediction_support_vector = support_vector.predict(X_test)

# Classification report for SupportVector

visualiser = classificationReport(support_vector,classes = ['won','loss'])
visualiser.fit(X_train,y_train)
visualiser.score(y_test,prediction_support_vector)
result = visualiser.poof()

# Now lets say that after all our analysis we choose
# SVC as our algorithm to work with
# We'll write the model to a pkl file

pickle.dump(support_vector,open('model.pkl','wb'))
