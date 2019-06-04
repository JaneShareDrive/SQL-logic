import pyodbc
import pandas
from pandas import DataFrame

cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\users\bartogre\desktop\CorpRentalPivot1.accdb;UID="";PWD="";')
crsr = cnxn.cursor()
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name)
cursor = cnxn.cursor()
sql = "Select sum(CYTM), sum(PYTM), BRAND From data Group By BRAND"

#get questions by topic
sql = "Select questionID, question From student_practice where Topic_Code is topic"

#get answers by topic
sql = "Select question, correct_answer, explanation From student_practice where Topic_Code is topic"

#get questions by difficulty
sql = "Select questionID, question From student_practice where Difficulty is difficulty"

#get answers by difficulty
sql = "Select question, correct_answer, explanation From student_practice where Difficulty is difficulty"

#score tests. Takes 'submitted' parameter, which is a list of tuples: ([(subMittedanswer, correctAnswer)])

i = 0
for a1, a2 in submitted:
  if a1==a2:
      i+=1
return i, len(submitted), round(i*100/len(submitted))



cursor.execute(sql)
for data in cursor.fetchall():
    print (data)