import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def pos1(conn):
    cursor=conn.cursor()
    x=input("enter the word")
    x="'"+x+"'"
    cursor.execute('Select t.pos_UD,t.word,count(*) from Tword t where t.word='+x+' GROUP BY t.pos_UD,t.word')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
        print('POS_UD: '+myresult[i][0]+'\t word:'+myresult[i][1]+'\toccurances'+str(myresult[i][2]))
pos1(conn)
