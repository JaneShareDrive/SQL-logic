import pyodbc
import pandas as pd
import json

#get topics
def getTopics(): #returns Topic Code, Topic
    query = "Select distinct Topic_Code, Topic From student_practice" #Check whether SQL column name "Topic" is correct
    with pyodbc.connect(sqldb_connect) as cnxn:  #this with block can probably be modularized, but it's not trivial - the function must be aware of any variables which might be used in query
        df = pd.read_sql(query, cnxn)
    cnxn.close()
    return df.to_json(orient='records')

#get questions by topic
def getQuestionsT(topicIn): #returns questionID, question, possible_answer by topic
    topic = json.loads(topicIn) #Expects numeric Topic_Code
    query = f"Select question_ID, question, possible_answer From student_practice where Topic_Code = '{topic}' order by question_ID"
    with pyodbc.connect(sqldb_connect) as cnxn:
        df = pd.read_sql(query, cnxn)
    cnxn.close()
    return df.to_json(orient='records')

#get answers by topic
def getAnswersT(topicIn): #returns question, correct_answer, explanation by topic
    topic = json.loads(topicIn) #Expects numeric Topic_Code
    query = f"Select question, correct_answer, explanation From student_practice where Topic_Code = '{topic}' order by question_ID"
    with pyodbc.connect(sqldb_connect) as cnxn:
        df = pd.read_sql(query, cnxn)
    cnxn.close()
    return df.to_json(orient='records')

#get questions by difficulty
def getQuestionsD(difficultyIn): #returns questionID, question, possible_answer by difficulty
    difficulty = json.loads(difficultyIn) #Expects difficulty = E,M, or D
    query = f"Select question_ID, question, possible_answer From student_practice where Difficulty = '{difficulty}' order by question_ID"
    with pyodbc.connect(sqldb_connect) as cnxn:
        df = pd.read_sql(query, cnxn)
    cnxn.close()
    return df.to_json(orient='records')

#get answers by difficulty
def getAnswersD(difficultyIn): #returns question, correct_answer, explanation by difficulty
    difficulty = json.loads(difficultyIn) #Expects difficulty = E,M, or D
    query = f"Select question, correct_answer, explanation From student_practice where Difficulty = '{difficulty}' order by question_ID"
    with pyodbc.connect(sqldb_connect) as cnxn:
        df = pd.read_sql(query, cnxn)
    cnxn.close()
    return df.to_json(orient='records')

#score tests
def scoreTests(qaTuple): #expects JSON-formatted list of tuples of the form (questionIDs, submitted_answers). Returns score, number of questions, percentage score.
    QAs = json.loads(qaTuple) #read in as list of tuples
    query = f"SELECT question_ID, correct_answer FROM student_practice WHERE question_ID IN ({','.join(str(i[0]) for i in QAs)});"
    with pyodbc.connect(sqldb_connect) as cnxn:
        df = pd.read_sql(query, cnxn) #dataframe with columns for question_ID and correct_answer, only including question_IDs in QAs
    cnxn.close()
    score = 0
    for i,j in zip([k[1] for k in QAs],[list(df.pop('correct_answer'))]): #elementwise iteration through list of submitted_answers from QAs, and correct_answers from df
        if i==j: #probably possible to make for loop a one-liner, but might impact readability
            score+=1
    return json.dumps(score, len(QAs), round(score*100/len(QAs))) # returns score, number of questions, percentage score.  Probably need to tweak JSON format.   
