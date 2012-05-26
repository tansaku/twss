Raw data used for training and testing included by permission from Kiddon and Brun.

POSITIVE DATA
twssstories.txt: 2027 TWSS jokes from twssstories.com

NEGATIVE DATA
usaquotes.txt: 4199 One sentence English quotations from wikiquote
fml.txt: 1768 FML stories from the intimacy section of fmylife.com
tfln.onesent.txt: 11870 One liner texts from textsfromlastnight.com


to train grab at random 2001 sentences from TWSS (i.e. most of them)
and 667 from each of the negative data sets

naive Bayesian classifier


okay, so we have fml, tfln, twws and usa, which we can detect newlines in


split them up into sentences

given a sentence - negative example:

"Tactics flow from a positionally superior game."

want P(TWSS|"Tactics flow from a positionally superior game.")
= P("Tactics flow from a positionally superior game."|TWSS)P(TWSS)/P("Tactics flow from a positionally superior game.")

where P("Tactics flow from a positionally superior game.") = P("Tactics flow from a positionally superior game."|TWSS)P(TWSS) + P("Tactics flow from a positionally superior game."|!TWSS)P(!TWSS)

need P("Tactics"|TWSS)*P("flow"|TWSS)* ...
and P("Tactics"|!TWSS)*P("flow"|!TWSS)* ...

P("Tactics"|TWSS) = #TWSSwTactics/#TWSSTokens
P("Tactics"|!TWSS) = #!TWSSwTactics/#!TWSSTokens

for each token we need to know how many times it occurs in TWSS and how many times it occurs in !TWSS



SVM ML preprocessing gives me feature vectors

