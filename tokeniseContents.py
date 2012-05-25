import re
def tokeniseContents(contents):
  
  # Lower case
  contents = contents.lower()
  
  # Strip all HTML
  # Looks for any expression that starts with < and ends with > and replace
  # and does not have any < or > in the tag it with a space
  contents = re.sub('<[^<>]+>', ' ', contents);

  # Handle Numbers
  # Look for one or more characters between 0-9
  contents = re.sub('[0-9]+', 'number', contents) 

  # Handle URLS
  # Look for strings starting with http:// or https://
  contents = re.sub('(http|https)://[^\s]*', 'httpaddr', contents)

  # Handle Email Addresses
  # Look for strings with @ in the middle
  contents = re.sub('[^\s]+@[^\s]+', 'emailaddr', contents)

  # Handle $ sign
  contents = re.sub('[$]+', 'dollar', contents)
  
  return re.findall("[a-zA-Z]+",contents)
  