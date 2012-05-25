# TWSS #

A Python project inspired by the research of Chloé Kiddon and Yuriy Brun. [Paper available here.](http://www.cs.washington.edu/homes/brun/pubs/pubs/Kiddon11.pdf)

## Getting started ##

1. libsvm with python bindings required: [http://www.csie.ntu.edu.tw/~cjlin/libsvm](http://www.csie.ntu.edu.tw/~cjlin/libsvm) 

2. Apply patch to allow svm_predict to produce quiet output `cp svmutil.patch LIBSVM_HOME/python & cd LIBSVM_HOME/python & patch < svmutil.patch`

3. Download TWSS source data into data directory in current project

4. You can run some limited unit tests like so `python testTokeniseContents.py`

5. Run `python preprocessData.py` to tokenise the files and create a shared vocabulary which is saved in data/vocab.txt.  The resulting vector contains about 20k words.  `preprocessData` will also split sentences and save the results in pickle files.

6. Run `python generateTrainTestData.py` to create a training data set saved in data/train.pk and data/test.pk which are in the form of a array of dictionaries X<source> and vector y<source>, where X is training instances x features, and y is length #training-instances, and is 1 for TWSS and -1 for non-TWSS instances

7. Run `python train.py` from the command line THIS MAY TAKE A FEW MINUTES 

8. Run `python twss.py "<insert your sentence>"` to have a little chat with the resulting system

## Licence ##

Code is MIT Licence. Data is released under its own licence.
