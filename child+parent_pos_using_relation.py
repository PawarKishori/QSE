import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def rel(conn):
    cursor=conn.cursor()
    x=input("Enter the relation\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.rel='+x+' GROUP BY p.pos_UD, c.pos_UD')
    myresult=cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\tc_pos_UD: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
rel(conn)
