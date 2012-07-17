The faqbot is currently separate from the TWSS system, and provides a Natural Language interface to a SQL database

You'll need [nltk](https://github.com/nltk/nltk) and the [linguistics library](http://nodebox.net/code/index.php/Linguistics#verb_conjugation) on your PYTHONPATH to run

To run from the command line:

`python faq.py`

For development run [sniffer](http://pypi.python.org/pypi/sniffer) in the faq directory for continuous integration, i.e. ongoing running of the unit tests (essential if making tweaks)

Through the faqbot you can create new tables like so:

> "There is a Course Probabilistic Graphical Models called PGM"

Which would create a table "courses" with columns "ident" and "name" and a single entry with ident "Probabilistic Graphical Models" and name "PGM".  Further entries can be added using similar statements:

> "There is a Course Machine Learning called ML"

Which will add another row to the same table, with the expected contents.  Additional columns can be added to table's like so:

> "Probabilistic Graphical Models's instructor is Daphne Koller"
> "Machine Learning's instructor is Andrew Ng"

The system can then respond to queries such as 

> "Who is the instructor for Machine Learning?"
> "Which instructor teaches Probabilistic Graphical Models"

When a sentence fails to match either an assertion or query about an object and it's properties faq bot will fall back on an I feel lucky google search

It turns out the Natural Language interfaces for databases are an old and distinguished topic:

* [Androutsuopoulos et al (1995) Natural Language Interfaces to Databases – An Introduction. Journal of Natural Language Engineering, Cambridge University Press](http://arxiv.org/pdf/cmp-lg/9503016)
* [Popescu et al (2003) Towards a Theory of Natural Language Interfaces to Databases. In IUI ’03](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.1531&rep=rep1&type=pdf)

Which are (or at least were) the 2nd and 3rd hits in this Google Scholar search:

[http://scholar.google.co.uk/scholar?q=natural+language+interfaces+for+databases](http://scholar.google.co.uk/scholar?q=natural+language+interfaces+for+databases)

There are also various patents in the area:

* [http://www.google.com/patents/US4688195 (1987)](http://www.google.com/patents/US4688195)
* [http://www.google.com/patents/US4931935 (1990)](http://www.google.com/patents/US4931935)

