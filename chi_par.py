import sqlite3
conn = sqlite3.connect('Treebank_English.db')

def word1(conn):
    cursor = conn.cursor()
    x = input("enter the first word\n")
    y = input("enter the secone word\n")
    y="'"+y+"'"
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w,Tword k WHERE w.word='+x+' AND k.word='+y+' AND w.sid=k.sid AND w.parent=k.wid AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    for i in range(n):
        print('sentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1])


word1(conn)
