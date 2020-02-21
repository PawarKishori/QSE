import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def p_pos(conn):
    cursor=conn.cursor()
    x=input("enter the child pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.rel, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.pos_UD='+x+' GROUP BY p.rel, c.pos_UD')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('relation: '+myresult[i][0]+'\tc_pos_UD: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
p_pos(conn)
