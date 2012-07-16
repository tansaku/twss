The faqbot is currently separate from the TWSS system, and provides a Natural Language interface to a SQL database

To run from the command line:

`python faq.py`

For development run [sniffer](http://pypi.python.org/pypi/sniffer) in the faq directory

Through the faqbot you can create new tables like so:

"There is a Course Probabilistic Graphical Models called PGM"

Which would create a table "courses" with columns "ident" and "name" and a single entry with ident "Probabilistic Graphical Models" and name "PGM".  Further entries can be added using similar statements:

"There is a Course Machine Learning called ML"

Which will add another row to the same table, with the expected contents.  Additional columns can be added to table's like so:

"Probabilistic Graphical Models's instructor is Daphne Koller"
"Machine Learning's instructor is Andrew Ng"

The system can then respond to queries such as 

"Who is the instructor for Machine Learning?"
"Which instructor teaches Probabilistic Graphical Models"

When a sentence fails to match either an assertion or query about an object and it's properties faq bot will fall back on an I feel lucky google search

