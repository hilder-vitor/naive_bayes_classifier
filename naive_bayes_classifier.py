
# convert each entry of sl to integer
def str_list_to_int_list(sl):
    for i in xrange(len(sl)):
        sl[i] = int(sl[i])

# Read the precomputed logarithms of the probabilities used by the naive Bayes classifier.
# To precompute them, use the script generate_file_probabilities.py.
def read_log_probabilities(filenames):
    number_classes = len(filenames) # one file name for each class
    probs = range(number_classes) # creating a vector with number_classes entries 

    for ci in xrange(number_classes):
        file_log_prob = open(filenames[ci], "r")

        lines = file_log_prob.readlines()
        number_attributes = len(lines)-1

        probs_class = range(number_attributes+1)
    
        log_probability_class = int(lines[0])
        probs_class[0] = log_probability_class

        for i in xrange(1, len(lines)):
            list_line = lines[i].split()
            str_list_to_int_list(list_line)
            probs_class[i] = list_line
        probs[ci] = probs_class

        file_log_prob.close()

    return probs  # probs[c][i][j] has log(Pr[i-th attribute == j : class = c])


# attributes[i] has the value of the i-th attribute of the sample that we want to classify
# log_prob_per_class: is the "3D" matrix returned by the function read_log_probabilities
# For instance, attributes[2] == 10 means that the second variable has value 10.
def classify(attributes, log_prob_per_class):
    number_classes = len(log_prob_per_class)
    number_attributes = len(attributes)

    coef_class = [0 for _ in xrange(number_classes)]

    for c in xrange(number_classes):  # for each class c
        log_probs_c = log_prob_per_class[c]
        for i in xrange(len(attributes)): # for each attribute
            yi = attributes[i]-1
            coef_class[c] += log_probs_c[i+1][yi] # adding log(Pr[i-th attribute == yi])
        coef_class[c] += log_probs_c[0] # adding log(Pr[class == c])
    
    assigned_class = 0
    for c in xrange(1, number_classes):
        if coef_class[c] > coef_class[assigned_class]:
            assigned_class = c
    return assigned_class


# filename: name of the file containing the testing set
# probs_classes: is the "3D" matrix returned by the function read_log_probabilities
# class_labels: map from the strings representing the classes to the integer values
def read_and_classify_test_set(filename, probs_classes, class_labels):
    file_test_set = open(filename, "r")

    correct = 0
    wrong = 0
    
    for line in file_test_set:
        expected_class = class_labels[line[0]]
        attributes = line.split()[1:] # excluding first entry since it is the class
        str_list_to_int_list(attributes)
        assigned_class = classify(attributes, probs_classes)
        if expected_class == assigned_class:
            correct += 1
            print "%s: expected class == assigend class %d ....  OK" % (attributes, assigned_class)
        else:
            wrong += 1
            print "%s: expected class = %d, assigend class = %d ....  ERROR" % (attributes, expected_class, assigned_class)
    print "Accuracy (correct classified / total): ", (float(correct) / (correct + wrong))


def main():
    ######## Class 0: benign
    ######## Class 1: malignant
    class_labels = {'b': 0, 'm': 1}
    filenames = ['breast-cancer/breast-cancer-wisconsin.data.train.benign.scaled_log_prob',
             'breast-cancer/breast-cancer-wisconsin.data.train.malignant.scaled_log_prob']
    probs_classes = read_log_probabilities(filenames)
    read_and_classify_test_set('breast-cancer/breast-cancer-wisconsin.data.test', probs_classes, class_labels)


if __name__ == "__main__":
    main()
