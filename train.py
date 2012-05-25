from svmutil import *
import pickle
# grab complete training set

input = open('data/train.pk');
X = pickle.load(input)
y = pickle.load(input)
input.close()

input = open('data/test.pk');
Xtest = pickle.load(input)
ytest = pickle.load(input)
input.close()

print '\nTraining Linear SVM (TWSS Classification)\n'

prob  = svm_problem(y, X)
param = svm_parameter('-t 0 -c 4 -b 1')
m = svm_train(prob, param)

p_label, p_acc, p_val = svm_predict(ytest, Xtest, m, '-b 1')
ACC, MSE, SCC = evaluations(ytest, p_label)

# would be nice if we could get top predictors here, and perhaps run some tests on the model

svm_save_model("data/svm_model.pk",m)

