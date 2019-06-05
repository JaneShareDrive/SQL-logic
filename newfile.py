import pyodbc
import pandas as pd
import json

cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\users\bartogre\desktop\CorpRentalPivot1.accdb;UID="";PWD="";')
crsr = cnxn.cursor()
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name)
cursor = cnxn.cursor()

#get topics
def getTopics():
  cnxn = pyodbc.connect(sqldb_connect)
  sql = "Select distinct Topic_Code From student_practice"
  df = pd.read_sql(sql, cnxn)
  return df.to_json(orient='values')
  cnxn.close()

#get questions by topic
def getQuestionsT(topicIn):
  topic = json.loads(topicIn)
  sql = "Select question_ID, question From student_practice where Topic_Code is topic order by question_ID"
  df = pd.read_sql(sql, cnxn)
  return df.to_json(orient='records')

#get answers by topic
def getAnswersT(topicIn):
  topic = json.loads(topicIn)
  sql = "Select question, correct_answer, explanation From student_practice where Topic_Code is topic order by question_ID"
  df = pd.read_sql(sql, cnxn)
  return df.to_json(orient='records')

#get questions by difficulty
def getQuestionsD(difficultyIn):
  difficulty = json.loads(difficultyIn)
  sql = "Select question_ID, question From student_practice where Difficulty is difficulty order by question_ID"
  df = pd.read_sql(sql, cnxn)
  return df.to_json(orient='records')

#get answers by difficulty
def getAnswersD(difficultyIn):
  difficulty = json.loads(difficultyIn)
  sql = "Select question, correct_answer, explanation From student_practice where Difficulty is difficulty order by question_ID"
  df = pd.read_sql(sql, cnxn)
  return df.to_json(orient='records')

#score tests. Takes 'submitted' parameter, which is a list of tuples: ([(subMittedanswer, correctAnswer)])

i = 0
for a1, a2 in submitted:
  if a1==a2:
      i+=1
return i, len(submitted), round(i*100/len(submitted))



cursor.execute(sql)
for data in cursor.fetchall():
    print (data)