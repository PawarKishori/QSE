import sqlite3
conn = sqlite3.connect('Treebank_English.db')


def UD_ILMT(conn):
    cursor = conn.cursor()
    cursor.execute(
        'SELECT pos_UD,pos_ILMT,count(*) FROM Tword GROUP BY pos_UD, pos_ILMT')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
        print('UD_pos:'+myresult[i][0]+'\tpos_ILMT: ' +
              myresult[i][1]+'\toccurances: '+str(myresult[i][2]))


UD_ILMT(conn)
