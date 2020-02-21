import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def reltwo(conn):
    cursor=conn.cursor()
    x=input("Enter the relation:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.rel, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.rel='+x+' GROUP BY p.rel, c.pos_UD')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
            print('parent_rel: '+str(myresult[i][0])+'\tchild_pos: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
reltwo(conn)
