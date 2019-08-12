from math import log
from math import ceil

train_set = open("breast-cancer/breast-cancer-wisconsin.data.train", "r")

# The nine attributes . . . . . . . Range of values
#
#0. Clump Thickness    . . . . . . . 1 - 10
#1. Uniformity of Cell Size  . . . . 1 - 10
#2. Uniformity of Cell Shape . . . . 1 - 10
#3. Marginal Adhesion  . . . . . . . 1 - 10
#4. Single Epithelial Cell Size  . . 1 - 10
#5. Bare Nuclei        . . . . . . . 1 - 10
#6. Bland Chromatin    . . . . . . . 1 - 10
#7. Normal Nucleoli    . . . . . . . 1 - 10
#8. Mitoses            . . . . . . . 1 - 10

total_benign = 0
total_malignant = 0

##   M[i][j] will store the number of times the i-th attribute has value j among the samples
## whose class is m (i.e., malignant).
##   For example, M[0][4] = 10 means that the first attribute (Clump Thickness) has the value 4
## ten times among the malignant samples.
##   Therefore, the probability that a sample has Clump Thickness equal to 4 given that it is
## malignant is M[0][5] / total_malignant (in this example, 10 / total_malignant)
M = [ [0 for _ in xrange(11) ] for _ in xrange(9)]
B = [ [0 for _ in xrange(11) ] for _ in xrange(9)]

for line in train_set:
    list_line = line.split()
    if 'm' == list_line[0]:
        A = M
        total_malignant += 1
    else:
        A = B
        total_benign += 1
    for i in xrange(1, len(list_line)):
        val = int(list_line[i])
        print val
        A[i-1][val] += 1

train_set.close()


prob_class_m = (float(total_malignant) / (total_malignant + total_benign))
prob_class_b = (float(total_benign) / (total_malignant + total_benign))
print "Probability of being malignant: P(class = m) =", prob_class_m
print "Probability of being benign: P(class = b) =", prob_class_b


prob_M = [ [0 for _ in xrange(11) ] for _ in xrange(9)]
prob_B = [ [0 for _ in xrange(11) ] for _ in xrange(9)]
for i in xrange(9):
    for j in xrange(1, 11):
        prob_M[i][j] = float(M[i][j]) / total_malignant
        print "P(x_%d = %d | class = m) = %f" % (i, j, prob_M[i][j])
for i in xrange(9):
    for j in xrange(1, 11):
        prob_B[i][j] = float(B[i][j]) / total_benign
        print "P(x_%d = %d | class = b) = %f" % (i, j, prob_B[i][j])



log_M = [ [0 for _ in xrange(11) ] for _ in xrange(9)]
log_B = [ [0 for _ in xrange(11) ] for _ in xrange(9)]

SCALE_FACTOR = 1000 

for i in xrange(9):
    for j in xrange(1, 11):
        if prob_M[i][j] > 0:
            log_M[i][j] = int(ceil(SCALE_FACTOR * log(prob_M[i][j])))
        if prob_B[i][j] > 0:
            log_B[i][j] = int(ceil(SCALE_FACTOR * log(prob_B[i][j])))

log_prob_train_set = open("breast-cancer/breast-cancer-wisconsin.data.train.malignant.scaled_log_prob", "w")
scaled_log_prob_m = int(ceil(SCALE_FACTOR * log(prob_class_m)))
log_prob_train_set.write(str(scaled_log_prob_m) + "\n")
for i in xrange(9):
    for j in xrange(1, 11):
        log_prob_train_set.write(str(log_M[i][j]))
        log_prob_train_set.write(" ")
    log_prob_train_set.write("\n")
log_prob_train_set.close()
print "Finished file breast-cancer/breast-cancer-wisconsin.data.train.malignant.scaled_log_prob."


log_prob_train_set = open("breast-cancer/breast-cancer-wisconsin.data.train.benign.scaled_log_prob", "w")
scaled_log_prob_b = int(ceil(SCALE_FACTOR * log(prob_class_b)))
log_prob_train_set.write(str(scaled_log_prob_b) + "\n")
for i in xrange(9):
    for j in xrange(1, 11):
        log_prob_train_set.write(str(log_B[i][j]))
        log_prob_train_set.write(" ")
    log_prob_train_set.write("\n")
log_prob_train_set.close()
print "Finished file breast-cancer/breast-cancer-wisconsin.data.train.benign.scaled_log_prob."
