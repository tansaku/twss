import sqlite3
import pdb

# TODO this should be objectified, and have the database_name set once for some factory object

def createTable(name, columns, database_name):
  conn = sqlite3.connect(database_name)
  c = conn.cursor()
  columns = [scrub(column) for column in columns]
  body = 'name text, ' + ', '.join([column + " text" for column in columns])
  name = scrub(name)
  # Create table
  # http://stackoverflow.com/questions/3247183/variable-table-name-in-sqlite
  sql = 'CREATE TABLE IF NOT EXISTS %s ( %s )' % (name, body)
  #raise Exception(sql)
  c.execute(sql) #[name,','.join(columns)]
  conn.commit()
  c.close()

def scrub(name):
  return ''.join( chr for chr in name if chr.isalnum() or chr == '_' )

def scrubQuoted(name):
  return ''.join( chr for chr in name if chr.isalnum() or chr == '_'  or chr == ' ')

def dictValuePad(key):
    return '"' + str(key) + '"'
  
def addEntity(name, hashtable, database_name):
  conn = sqlite3.connect(database_name)
  c = conn.cursor()
  name = scrub(name)
  # Insert a row of data
  sql = "INSERT INTO %s (%s) VALUES (%s)"% (name, ','.join(hashtable.keys()),', '.join(['"'+value+'"'for value in hashtable.values()]))
  try:
    c.execute(sql)
  except sqlite3.OperationalError, e: 
    raise Exception(str(e.message) + ":" + sql)
  conn.commit()

  # We can also close the cursor if we are done with it
  c.close()
  
def findTableContainingEntityWithIdent(ident, database_name,flag=False):
  conn = sqlite3.connect(database_name)
  c = conn.cursor()
  c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
  results = c.fetchall()
  #if flag: raise Exception(database_name)
  for result in results:
    result = result[0]
    sql = "SELECT * FROM %s WHERE ident = '%s'" % (result,ident)
    #raise Exception(sql)
    #if flag:
     # raise Exception(str(c.execute("PRAGMA table_info(courses)").fetchall()) + sql)
    c.execute(sql)
    fromThisTable = c.fetchone()
    if fromThisTable:
      c.close()
      return (result,fromThisTable)
  c.close()
  return (None,None)
  
def grabColumnNames(table, database_name):
  conn = sqlite3.connect(database_name)
  c = conn.cursor()
  sql = ("PRAGMA table_info(%s)"%scrub(table))
  c.execute(sql)
  results = c.fetchall()
  return [result[1] for result in results]
    
def modifyTable(table, new_column, database_name):
  conn = sqlite3.connect(database_name)
  c = conn.cursor()
  new_column = new_column.replace(' ','_')
  sql = "ALTER TABLE %s ADD COLUMN %s TEXT" % (table, new_column.lower())
  #raise Exception(sql)
  c.execute(sql)
  c.close()
  conn.commit()
  
def grabEntity(name, ident, database_name):
  conn = sqlite3.connect(database_name)
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  name = scrub(name)
  ident = scrubQuoted(ident)
  sql = "SELECT * FROM %s WHERE ident = '%s'" % (name,ident)
  #raise Exception(sql)
  c.execute(sql)
  result = c.fetchone()
  c.close()
  return result
  
def updateEntity(table, hashtable ,database_name):
  conn = sqlite3.connect(database_name)
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  table = scrub(table)
  update = ', '.join([key.replace(' ','_')+" = '"+value+"'" for (key,value) in hashtable.items()])
  sql = "UPDATE %s SET %s WHERE ident = '%s'" % (table,update,hashtable["ident"])
  #raise Exception(sql)
  c.execute(sql)
  c.close()
  conn.commit()
  

  