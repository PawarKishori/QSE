import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def p_pos(conn):
    cursor=conn.cursor()
    x=input("enter the parent pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.rel, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.pos_UD='+x+' GROUP BY p.pos_UD, c.rel')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\trelation: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
p_pos(conn)
