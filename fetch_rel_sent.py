import sqlite3
conn=sqlite3.connect('Treebank_English.db')
def fetch_rel_sent(conn):
	cursor=conn.cursor()
	x=input("enter the first relation:\n")
	#y=input("enter the second U_POS:\n")
	
	k=open("outputfile_relation","w")
	cursor.execute("SELECT t.sentence,s.word,s.wid,a.word,a.wid from Tsentence t,Tword s,Tword a WHERE s.rel=? AND a.wid=s.parent AND s.sid=a.sid AND t.sid=s.sid",(x,))
	rows=cursor.fetchall()
	k.seek(0)
	print("Total number of sentences : ")
	print(len(rows)) 
	n=int(input("Enter the number of sentences you need:\n"))
	#for i in rows:
    	#	res.append('|'.join(str(v) for v in rows[i])) 
	for i in range(n):
		print('|'.join(str(v) for v in rows[i]))
		k.write('|'.join(str(v) for v in rows[i]))
		k.write("\n")
	k.close()
	#for row in rows:
	#	print(row)
fetch_rel_sent(conn)
