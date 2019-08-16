# Naïve Bayes Classifier

Implementing Naïve Bayes Classifier _ex nihilo_ (from scratch, without third-party libs, using pure and simple python).

It uses the Breast Cancer Data Set (https://archive.ics.uci.edu/ml/datasets/Breast+Cancer), which was divided into a training set (from which the probabilities are computed) and a testing set (used to measure the accuracy).

Use the script split\_dataset\_train\_test.py to randomly generate the training and the test sets, then the script generate\_file\_probabilities.py to precompute the probabilities used by the classifier and to store them in two files. The script naive\_bayes\_classifier.py reads those two files and performs the classification of the instances from the testing data set.

