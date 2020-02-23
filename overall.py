import sqlite3
conn=sqlite3.connect('Treebank_English.db')
print("\t1.Parent pos's and its frequencies for the child_pos\n\t2.Child pos's and its frequencies for the parent_pos\n\t3.enter relation to get parent and child pos along with the frequencies\n\t4.Enter child pos to get its parent relations and frequencies with it\n\t5.Enter the parent pos to get child realtions and its frequencies with it\n\t6.Enter two relations to get the no.of occurances of it\n\t7.Enter the relation to get frequencies of th pos with it\n\t8.Get sentences using words\n\t9.UD_ILMT relations\n\t10.enter word or pos to get pos or word frequency.")
choice=int(input("Enter your choice"))




def p_pos(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT pos_UD,count(*) from Tword GROUP BY pos_UD')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('pos : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("enter the child pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.pos_UD='+x+' GROUP BY p.pos_UD, c.pos_UD')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\tc_pos: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter child pos")
        opt2=input("enter the parent pos")
        fi="output_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.pos_UD,c.pos_UD FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.pos_UD='+opt1+' AND p.pos_UD='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close


def p_pos1(conn):
    cursor=conn.cursor()

    cursor.execute('SELECT pos_UD,count(*) from Tword GROUP BY pos_UD')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('pos : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("enter the parent pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.pos_UD='+x+' GROUP BY p.pos_UD, c.pos_UD')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\tc_pos: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter child pos")
        opt2=input("enter the parent pos")
        fi="output2_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,p.filename,l.sentence,p.pos_UD, c.pos_UD  FROM Tword p,Tsentence l,Tword c on p.wid=c.parent and p.sid=c.sid and l.sid=p.sid where c.pos_UD='+opt1+' AND p.pos_UD='+opt2+'')
        myresult1=cursor1.fetchall()
        #print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n")
        f.close



def rel(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT rel,count(*) from Tword GROUP BY rel')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('rel : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("Enter the relation\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.rel='+x+' GROUP BY p.pos_UD, c.pos_UD')
    myresult=cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\tc_pos_UD: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter child pos")
        opt2=input("enter the parent pos")
        fi="output3_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.pos_UD,c.pos_UD FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.rel='+x+' AND c.pos_UD='+opt1+' AND p.pos_UD='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close



def p_posr(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT pos_UD,count(*) from Tword GROUP BY pos_UD')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('pos : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("enter the child pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.rel, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.pos_UD='+x+' GROUP BY p.rel, c.pos_UD')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('relation: '+myresult[i][0]+'\tc_pos_UD: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter relation")
        opt2=input("enter the child pos")
        fi="output4_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.rel,c.pos_UD FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.pos_UD='+opt2+' AND p.rel='+opt1)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close



def p_posr1(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT pos_UD,count(*) from Tword GROUP BY pos_UD')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('pos : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("enter the parent pos:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.rel, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.pos_UD='+x+' GROUP BY p.pos_UD, c.rel')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
            print('p_pos: '+myresult[i][0]+'\trelation: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter relation")
        opt2=input("enter the parent pos")
        fi="output5_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.pos_UD,c.rel FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.rel='+opt1+' AND p.pos_UD='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close




def rel2(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT rel,count(*) from Tword GROUP BY rel')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('rel : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

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
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter parent relation")
        opt2=input("enter the child relation")
        fi="output6_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.rel,c.rel FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.rel='+opt2+' AND p.rel='+opt1)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.rel,c.rel FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.rel='+opt1+' AND p.rel='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close




def relone(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT rel,count(*) from Tword GROUP BY rel')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('rel : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("Enter the child relation:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.pos_UD, c.rel, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.rel='+x+' GROUP BY p.pos_UD, c.rel')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
            print('parent_pos: '+str(myresult[i][0])+'\trelation: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter relation")
        opt2=input("enter the parent pos")
        fi="output7_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.pos_UD,c.rel FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE c.rel='+opt1+' AND p.pos_UD='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close



def reltwo(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT rel,count(*) from Tword GROUP BY rel')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('rel : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("Enter the parent relation:\n")
    x="'"+x+"'"
    cursor.execute('SELECT p.rel, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE p.rel='+x+' GROUP BY p.rel, c.pos_UD')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
            print('parent_rel: '+str(myresult[i][0])+'\tchild_pos: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
    print("Do you want to check some specific case(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter relation")
        opt2=input("enter the child pos")
        fi="output7_query_"+opt1+"_"+opt2+".txt"
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor1=conn.cursor()
        cursor1.execute('SELECT p.sid,l.filename,l.sentence,p.pos_UD,c.rel FROM Tsentence l,Tword p,Tword c ON p.wid = c.parent AND p.sid = c.sid AND l.sid=p.sid WHERE p.rel='+opt1+' AND c.pos_UD='+opt2)
        myresult1=cursor1.fetchall()
        print(myresult1)
        l=len(myresult1)
        f=open(fi,'w')
        for i in range(l):
            f.write("sid= "+str(myresult1[i][0])+"\tfilename: "+str(myresult1[i][1])+"\tsentence: "+str(myresult1[i][2])+"\tparent_pos: "+str(myresult1[i][3])+"\tchild_pos: "+str(myresult1[i][4])+"\n\n")
        f.close



def words(conn):
    cursor = conn.cursor()
    x = input("enter the word to get the sentence\n")
    y=x
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w WHERE w.word='+x+' AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    fi="output_1word_"+y+".txt"
    f=open(fi,'w')
    for i in range(n):
        f.write('sentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1])
    f.close()


def word(conn):
    cursor = conn.cursor()
    x = input("enter the first word\n")
    x1=x
    y = input("enter the secone word\n")
    y1=y
    y="'"+y+"'"
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w,Tword k WHERE w.word='+x+' AND k.word='+y+' AND w.sid=k.sid AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    fi="output_2words_"+x1+"_"+y1+".txt"
    f=open(fi,'w')
    for i in range(n):
        f.write('\nsentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1]+"\n")
    f.close()

def word1(conn):
    cursor = conn.cursor()
    x = input("enter the first word\n")
    x1=x
    y = input("enter the secone word\n")
    y1=y
    y="'"+y+"'"
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w,Tword k WHERE w.word='+x+' AND k.word='+y+' AND w.sid=k.sid AND w.parent=k.parent AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    fi="output_3words_"+x1+"_"+y1+".txt"
    f=open(fi,'w')
    for i in range(n):
        f.write('\nsentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1]+"\n")
    f.close()




def word2(conn):
    cursor = conn.cursor()
    x = input("enter the first word\n")
    x1=x
    y = input("enter the secone word\n")
    y1=y
    y="'"+y+"'"
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w,Tword k WHERE w.word='+x+' AND k.word='+y+' AND w.sid=k.sid AND w.wid=k.parent AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    fi="output_4words_"+x1+"_"+y1+".txt"
    f=open(fi,'w')
    for i in range(n):
        f.write('\nsentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1]+"\n")
    f.close()
    


def word3(conn):
    cursor = conn.cursor()
    x = input("enter the first word\n")
    x1=x
    y = input("enter the secone word\n")
    y1=y
    y="'"+y+"'"
    x = "'"+x+"'"
    cursor.execute('select t.sid,t.sentence from Tsentence t,Tword w,Tword k WHERE w.word='+x+' AND k.word='+y+' AND w.sid=k.sid AND w.parent=k.wid AND t.sid=w.sid')
    myresult = cursor.fetchall()
    n = len(myresult)
    print("number of sentences with given word are :"+str(n))
    fi="output_5words_"+x1+"_"+y1+".txt"
    f=open(fi,'w')
    for i in range(n):
        f.write('\nsentence_id:'+myresult[i][0]+'\tsentence: '+myresult[i][1]+"\n")
    f.close()
    

def UD_ILMT(conn):
    cursor = conn.cursor()
    cursor.execute(
        'SELECT pos_UD,pos_ILMT,count(*) FROM Tword GROUP BY pos_UD, pos_ILMT')
    myresult = cursor.fetchall()
    n = len(myresult)
    for i in range(n):
        print('UD_pos:'+myresult[i][0]+'\tpos_ILMT: ' +
              myresult[i][1]+'\toccurances: '+str(myresult[i][2]))
    print("Do you want to check for some specific conditions(y/n)")
    pick=input()
    if(pick=='y'):
        opt1=input("enter the pos_UD")
        x=opt1
        opt2=input("enter the pos_ILMT")
        y=opt2
        opt1="'"+opt1+"'"
        opt2="'"+opt2+"'"
        cursor.execute('SELECT t.sid,t.sentence,w.pos_UD,w.pos_ILMT from Tsentence t,Tword w WHERE t.sid=w.sid AND w.pos_UD='+opt1+'AND w.pos_ILMT='+opt2)
        myresult=cursor.fetchall()
        m=len(myresult)
        fi="output_9"+x+"_"+y+".txt"
        f=open(fi,'w')
        for i in range(m):
            f.write('\nsentence_id:'+myresult[i][0]+'\tsentence:'+myresult[i][1]+'\tpos_UD:'+myresult[i][2]+'pos_ILMT :'+myresult[i][3])
        f.close()

def pos1(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT pos_UD,count(*) from Tword GROUP BY pos_UD')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('pos : '+mm[i][0]+'\tcount :'+str(mm[i][1]))

    x=input("enter the pos")
    k=x
    x="'"+x+"'"
    cursor.execute('Select t.pos_UD,t.word,count(*) from Tword t where t.pos_UD='+x+' GROUP BY t.pos_UD,t.word')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
        print('POS_UD: '+myresult[i][0]+'\t word:'+myresult[i][1]+'\toccurances'+str(myresult[i][2]))
    print("Do you want to check specific cases(y/n)\n")
    pick=input()
    if(pick=='y'):
        opt1=input("enter the word")
        y=opt1
        opt1="'"+opt1+"'"
        cursor.execute('SELECT l.sid,l.sentence,t.pos_UD,t.word from Tsentence l,Tword t WHERE t.pos_UD='+x+' AND t.word='+opt1+' AND l.sid=t.sid')
        res=cursor.fetchall()
        fi="output_10"+k+"_"+y+".txt"
        f=open(fi,'w')
        lenres=len(res)
        for i in range(lenres):
            f.write("\nsentence_id :"+res[i][0]+"\tsentence :"+res[i][1]+"pos :"+res[i][2]+"word :"+res[i][3])
        f.close()
        
def pos2(conn):
    cursor=conn.cursor()
    x=input("enter the word")
    k=x
    x="'"+x+"'"
    cursor.execute('Select t.pos_UD,t.word,count(*) from Tword t where t.word='+x+' GROUP BY t.pos_UD,t.word')
    myresult=cursor.fetchall()
    n=len(myresult)
    for i in range(n):
        print('POS_UD: '+myresult[i][0]+'\t word:'+myresult[i][1]+'\toccurances'+str(myresult[i][2]))
    print("Do you want to check specific cases(y/n)\n")
    pick=input()
    if(pick=='y'):
        opt1=input("enter the pos")
        y=opt1
        opt1="'"+opt1+"'"
        cursor.execute('SELECT l.sid,l.sentence,t.pos_UD,t.word from Tsentence l,Tword t WHERE t.pos_UD='+opt1+' AND t.word='+x+' AND l.sid=t.sid')
        res=cursor.fetchall()
        fi="output_10"+k+"_"+y+".txt"
        f=open(fi,'w')
        lenres=len(res)
        for i in range(lenres):
            f.write("\nsentence_id :"+res[i][0]+"\tsentence :"+res[i][1]+"pos :"+res[i][2]+"word :"+res[i][3])
        f.close()




def relationc(conn):
    cursor=conn.cursor()
    cursor.execute('SELECT rel,count(*) from Tword GROUP BY rel')
    mm=cursor.fetchall()
    lenmm=len(mm)
    for i in range(lenmm):
        print('rel : '+mm[i][0]+'\tcount :'+str(mm[i][1]))


if(choice==1):
    p_pos(conn)
elif(choice==2):
    p_pos1(conn)
elif(choice==3):
    rel(conn)
elif(choice==4):
    p_posr(conn)
elif(choice==5):
    p_posr1(conn)
elif(choice==6):
    rel2(conn)
elif(choice==7):
    relationc(conn)
    print("\n\n1.enter child relation\n2.enter parent relation")
    option=int(input("enter your option"))
    if(option==1):
        relone(conn)
    elif(option==2):
        reltwo(conn)
elif(choice==8):
    print("\n\n\n1.get all sentences with particular word\n2.Get all the sentences with given two words\n3.Enter sibling words to get those sentences with those words\n4.Enter child_parent words to get the sentences\n5.Enter parent-child words to get the sentences\n")
    opt=int(input("enter your choice"))
    if(opt==1):
        words(conn)
    elif(opt==2):
        word(conn)
    elif(opt==3):
        word1(conn)
    elif(opt==4):
        word2(conn)
    elif(opt==5):
        word3(conn)
elif(choice==9):
    UD_ILMT(conn)
elif(choice==10):
    print("\n\n1.enter the word to get word pos frequencies\n2.enter pos to get pos word frequencies\n")
    o=int(input("Enter your choice"))
    if(o==1):
        pos2(conn)
    elif(o==2):
        pos1(conn)
