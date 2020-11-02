from mysqlconnection import *

#check for valid input for fields and tables
def validInput(search, table, field=None):
  # DB Schema
  schema = {
    'users': ['userId','type','firstName','lastName','profileImage','city','state','country','about','companyRepRole','email','companyId','university','graduationYear','major','role','skills','degree'],
    'companies': ['id','name','city','state','country','website','logoImage','description','employees','fundingSize','copmanyRepId'],
    'comments': ['id','newsfeedId','userId','comment','commentedOn'],
    'messages': ['_id','message','receiverId','senderId','createdAt','read'],
    'newsfeed': ['id','user (map)','postText','postedOn'],
    'opportunities': ['id','companyId','role','paid','compensation','description','skills','expired','city','state','createdOn','url','country','remote'],
    'projects': ['id','projectOwnerId','role','city','state','country','description','skills','expired','createdOn','remote'],
    'userSettings': ['id','userId','notifications','visableToStartups','visableToStudents','searchRadius'],
    'favoriteCompanies': ['userId', 'companyId'],
    'favoriteOpportunities': ['userId', 'opportunityId'],
    'favoriteStudents': ['userId', 'studentId'],
  }
  
  # return the name of id field if table or field is found in shema
  if search.lower() == 'table' and field == None:
    return schema[table][0] if table in schema else False
  if search.lower() == 'field':
    return schema[table][0] if field in schema[table] else False

# Get Row of table, By ID
def getRow(table, id):
  field = validInput('table', table)
  # search if field exists and is not a favorite table
  if not field or table.lower().find('favorite') == 0:
    return False
  else:
    mysql = MySQLConnection('SSDB')
    data = { 'id' : id }
    try:
      query = 'SELECT * FROM ' + table + ' WHERE ' + field + ' = %(id)s;'
      rows = mysql.query_db(query, data)
      return rows[0] if len(rows) > 0 else False
    except:
      print('GET-ROW ERROR')
      return False

# delete row
def deleteRow(table, id):
  field = validInput('table', table)
  if not field:
    return False
  else:
    try:
      mysql = MySQLConnection('SSDB')
      data = { 'id': id }
      query = 'DELETE FROM ' + table + ' WHERE ' + field + ' = %(id)s;'
      return mysql.query_db(query, data)
    except:
      print('DELETE FIELD ERROR')
      return False


# getMyFavorites(table=opportunities/companies/students, userId) returns array of opportunities
def getMyFavorites(table, userId):
  field = validInput('table', table)
  if not field:
    return False
  else:
    try:
      mysql = MySQLConnection('SSDB')
      data = { 'userId': userId }
      query  = 'SELECT * FROM ' + table + ' WHERE userId = %(userId)s;'
      favorites = mysql.query_db(query, data)
      return list(favorites) if len(favorites) > 0 else False
    except:
      print('FAVORITES ERROR:')
      return False


def updateField(table, id, fieldName, fieldValue):
  field = validInput('field', table, fieldName)
  if not field:
    return False
  else:
    try:
      mysql = MySQLConnection('SSDB')
      data = {
        'id': id,
        'fieldValue': fieldValue,
      }
      query = 'UPDATE ' + table +  ' SET ' + fieldName + ' = %(fieldValue)s WHERE ' + field + ' = %(id)s;'
      return mysql.query_db(query, data)
    except:
      print('UPDATE FIELD ERROR')
      return False