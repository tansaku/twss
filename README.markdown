# TWSS #

A Python project inspired by the research of Chloé Kiddon and Yuriy Brun. [Paper available here.](http://www.cs.washington.edu/homes/brun/pubs/pubs/Kiddon11.pdf)

Thanks to [Henry Garner](https://github.com/henrygarner) for original coding initiative, to [Marcin Tolysz](https://github.com/tolysz) for awesome super-fast server modifications, and to Andrew Ng for the [ML course](http://coursera.org/ml)

Part of the [Funniest Computer Ever Open Source Initiative](http://funniestcomputer.neurogrid.com)

This code supported Zarquon Squelchmama III in the [chatbotbattles](http://www.square-bear.co.uk/cbb/groupb.htm) contest.  We didn't come anywhere near close to winning (our coding was all a bit last minute) but we did get one TWSS in there:

Judge: Hello Zarquon  
Zarquon: Greetings.  
Judge: How are you?  
Zarquon: How do you suppose?  
Judge: I suppose you are good but I don't know  
Zarquon: That's what she said!  
Judge: Hehe. Very funny

Note we now have some other chatbot related initiatives in the [faq](faq) and [worldmodel](worldmodel) directories.  Ultimately hoping these will all be integrated into a single coherent whole :-)

## Getting started
1. libsvm with python bindings required: [http://www.csie.ntu.edu.tw/~cjlin/libsvm](http://www.csie.ntu.edu.tw/~cjlin/libsvm) 

2. Apply patch to allow svm_predict to produce quiet output `cp svmutil.patch LIBSVM_HOME/python & cd LIBSVM_HOME/python & patch < svmutil.patch`

[N.B. here's how I add libsvm to my PYTHONPATH: export PYTHONPATH="/Users/samueljoseph/Code/libsvm-3.12/python/:$PYTHONPATH"]

3. Download TWSS source data into data directory in current project

4. You can run some limited unit tests like so `python testTokeniseContents.py`

5. Run `python preprocessData.py` to tokenise the files and create a shared vocabulary which is saved in data/vocab.txt.  The resulting vector contains about 20k words.  `preprocessData` will also split sentences and save the results in pickle files.

6. Run `python generateTrainTestData.py` to create a training data set saved in data/train.pk and data/test.pk which are in the form of a array of dictionaries X<source> and vector y<source>, where X is training instances x features, and y is length #training-instances, and is 1 for TWSS and -1 for non-TWSS instances

7. Run `python train.py` from the command line THIS MAY TAKE A FEW MINUTES 

8. Run `python twss.py "<insert your sentence>"` to have a little chat with the resulting system

## Licence ##

Code is MIT Licence. Data is released under its own licence.
