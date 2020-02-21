import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def rel2(conn):
    cursor=conn.cursor()
    cursor2=conn.cursor()
    x=input("enter the first relation\n:")
    y=input("enter the second relation\n:")
    x="'"+x+"'"
    y="'"+y+"'"
    cursor.execute('SELECT p.rel, c.rel, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.rel='+x+' AND c.rel='+y+' GROUP BY p.rel, c.rel')
    cursor2.execute('SELECT p.rel, c.rel, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.rel='+y+' AND c.rel='+x+' GROUP BY p.rel, c.rel')
    myresult1=cursor2.fetchall()
    myresult=cursor.fetchall()
    #print(myresult1)
    n = len(myresult)
    for i in range(n):
            print('parent_rel: '+myresult[i][0]+'\tchild_relation: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    m=len(myresult1)
    for i in range(m):
            print('child_rel: '+myresult1[i][0]+'\tparent_relation: '+myresult1[i][1]+'\tn_occurances: '+str(myresult1[i][2]))
rel2(conn)
