import pyodbc
import pandas as pd
import json

#get topics
def getTopics():
  cnxn = pyodbc.connect(sqldb_connect)
  sql = "Select distinct Topic_Code From student_practice"
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  return df.to_json(orient='records')

#get questions by topic
def getQuestionsT(topicIn):
  cnxn = pyodbc.connect(sqldb_connect)
  topic = json.loads(topicIn)
  sql = f"Select question_ID, question, possible_answer From student_practice where Topic_Code = '{topic}' order by question_ID"
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  return df.to_json(orient='records')

#get answers by topic
def getAnswersT(topicIn):
  cnxn = pyodbc.connect(sqldb_connect)
  topic = json.loads(topicIn)
  sql = f"Select question, correct_answer, explanation From student_practice where Topic_Code = '{topic}' order by question_ID"
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  return df.to_json(orient='records')

#get questions by difficulty
def getQuestionsD(difficultyIn):
  cnxn = pyodbc.connect(sqldb_connect)
  difficulty = json.loads(difficultyIn)
  sql = f"Select question_ID, question, possible_answer From student_practice where Difficulty is '{difficulty}' order by question_ID"
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  return df.to_json(orient='records')

#get answers by difficulty
def getAnswersD(difficultyIn):
  cnxn = pyodbc.connect(sqldb_connect)
  difficulty = json.loads(difficultyIn)
  sql = f"Select question, correct_answer, explanation From student_practice where Difficulty is '{difficulty}' order by question_ID"
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  return df.to_json(orient='records')

#score tests. NOT WORKING
def scoreTests(qaTuple):
  i = 0
  cnxn = pyodbc.connect(sqldb_connect)
  sql = Select question_ID, correct_answer from student_practice
  df = pd.read_sql(sql, cnxn)
  cnxn.close()
  QAs = json.loads(qaTuple) #dictionary
  for key, value in QAs:
    for 
    if df[0].key = 

for a1, a2 in submitted:
  if a1==a2:
      i+=1
return i, len(submitted), round(i*100/len(submitted))



cursor.execute(sql)
for data in cursor.fetchall():
    print (data)