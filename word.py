import sqlite3
conn = sqlite3.connect('Treebank_English.db')


def word(conn):
    cursor = conn.cursor()
    x = input("enter the word to get the sentence\n")
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w WHERE w.word='+x+' AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    for i in range(n):
        print('sentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1])


word(conn)
