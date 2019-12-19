import sqlite3
import sys
import glob
import re
import os
from wxconv import WXC


conn = sqlite3.connect('Treebank_Hindi.db')
conn1=sqlite3.connect('Treebank.db')
print ('Opened database successfully');
cursor = conn.cursor()
cursor10=conn1.cursor()

i = 1

while i == 1:
    print("\tSelect an option to execute one of the following quries:\n\t1.No of words in a sentence\n\t2.No of chunks in a sentence\n\t3.No of minor field types and information\n\t4.No of chunks given ChunkID\n\t5.POS combinations and respective records\n\t6.Identify the vibhakti-word pairs\n\t7.Identify parent(word) corresponding to each word in a given sentence\n\t8.Obtain chunk information, ie., given words and head word of each chunk in a given sentence\n\t9.Find the transliteration of each word in a given sentence\n\t10.To find the word and it's gender in a given sentence\n\t11.To obtain information about a given relation, including corresponding POS's and sentences\n\t12.To obtain sibling relations in a given sentence\n\t13.To obtain Noun followed by verb cases and print relation\n\t14.sentences with special case OBL relation\n\t15.Sentences with obl but with no CASE or MARK child\n\t16.sentences with either-or cases.\n\t17.Sentences with the given 2 relations\n\t18.ADP cases in the corpus.\n\t19.Draw tree for a given sentence.\n\t20.Draw trees for a given file.\n\t21.'hI' cases\n\t22.'BI' cases\n\t23.Relation that don't have a children at all\n\t24.Connection of SSF database and Conll database\n\tQuit\n\tEnter a number from 1-19 for queries and 15 to exit.")
    m = 0
    list0 = []
    list1 = []
    list2 = []
    choice = input("Enter your choice:")
    if choice == "1":
        sentenceid0 = input("Enter the sentence ID to obtain the corresponding number of words in the sentence")
        sentenceid = "'"+sentenceid0+"'"
        cursor.execute('Select count(word),sid from Tword where sid ='+sentenceid+'group by sid')
        rows = cursor.fetchall()
        leng = len(rows)
        for j in range(0,leng):
            print(rows[j][0]-1)

    elif choice == "2":
        sentenceid0 = input("Enter the sentence ID to obtain the corresponding number of chunks in the sentence")
        sentenceid = "'"+sentenceid0+"'"
        cursor.execute('Select count(distinct(chunkid)),sid from Tchunk where sid ='+sentenceid+' group by sid')
        rows = cursor.fetchall()
        leng = len(rows)
        for j in range(0,leng):
            print(rows[j][0])

    elif choice == "3":
        f = open('morphdetails.txt','w')
        Options = input("Enter one of the following fields to view its types:\nAdpType\nPronType\nAspect\nVerbForm\nVoice\nMood\nTense\nAdvType\nNumType\nPolite\nPossEcho\nPolarity\nForeign_\nStype\nAltTag\nTam")
        str1 = 'select ' +Options+',count(1) from Tword where '+Options+'!= "NULL" group by '+Options+';'
        cursor.execute(str1)
        rows = cursor.fetchall()
        leng = len(rows)
        print(1)
        for j in range(0,leng):
            print(rows[j])
        inp=input("Do you wish to view the word information of a specific type?(Y|N)?")
        if(inp=='Y' or inp=='y'):
            senttype = input("Enter the type of field you wish to view")
            senttype1 = "'"+senttype+"'"
            cursor1=conn.cursor()
            cursor1.execute('Select '+Options+',sid,filename,word from Tword where '+Options+'=='+senttype1)
            rows1 = cursor1.fetchall()
            leng1 = len(rows1)
            for j in range(0,leng1):
                f.write("sid:"+rows1[j][1]+"\tword:"+rows1[j][3]+"\tfilename:"+rows1[j][2]+"\n")
        f.close()

    elif choice == "4":
        chunkid0 = input("Enter the chunk ID to obtain the corresponding number of chunks in the type of the chunk ID")
        chunkid = "'"+chunkid0+"'"
        cursor.execute('Select chunkid,sid from Tchunk where chunkid ='+chunkid+' group by sid,chunkid')
        rows = cursor.fetchall()
        leng = len(rows)
        for j in range(0,leng):
            m = m+1
        print(m)

    elif choice == "5":
        str1='SELECT pos_UD,pos_ILMT,count(*) FROM Tword GROUP BY pos_UD, pos_ILMT ;'
        curr=conn.cursor()
        curr.execute(str1)
        abc=curr.fetchall()
        n=len(abc)
        #a=np.zeros(n)

        for i in range(0,n):
            print("pos_UD:" + abc[i][0] + '\t' +"pos_ILMT:" + abc[i][1] +'\t'+ "No. of occurrences:" + str(abc[i][2]) + '\n')
        choice1=input("Do you want to view all the occurrences of a certain type of pos_UD?\n Press(Y/N):")
        if(choice1=='Y' or choice1=='y'):
            str2='SELECT word,pos_UD,pos_ILMT FROM Tword;'
            pos_UD_type=input("Input the type of pos_UD :")
            pos_ILMT_type=input("Input the type of pos_ILMT:")
            curr.execute(str2)
            abc1=curr.fetchall()
            #print(abc1)
            n=len(abc1)
            f=open("UD-ILMT_occurrence.txt","w")
            for j in range(0,n):
                if pos_UD_type==abc1[j][1] and pos_ILMT_type==abc1[j][2]:
                    f.write("pos_UD: " + abc1[j][1] +"\t pos_ILMT: " + abc1[j][2] + " \t word: " +abc1[j][0] +"\n")
        f.close()

    elif choice == "6":
        sentenceid = input("Enter the sentence ID to find corresponding Vibhakti-word pairs")
        cursor.execute('Select sid,word,Vib from Tword where Vib not in ("NULL", "0")')
        rows = cursor.fetchall()
        leng = len(rows)
        f=open("Word-Vibhakti.txt","w")
        for j in range(0,leng):
            if sentenceid in rows[j]:
                f.write(str(rows[j][1:3]))
                f.write("\n")

    elif choice == "7":
        sentenceid = input("Enter the sentence ID to word-parent-rel pairs")
        cursor.execute('Select a.sid,a.word, b.word, a.rel from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid')
        rows = cursor.fetchall()
        leng = len(rows)
        f=open("word-parent.txt","w")
        for j in range(0,leng):
            if sentenceid in rows[j]:
                f.write(str(rows[j][1:4]))
                f.write("\n")
        f.close()

    elif choice == "8":
        sentenceid = input("Enter the sentence ID to obtain chunk information")
        cursor.execute('Select sid,chunkid,word,chunktype from Tchunk')
        rows = cursor.fetchall()
        leng = len(rows)
        k = 0
        for j in range(0,leng):
            if sentenceid in rows[j] and rows[j][1] not in list0:
                list0.append(rows[j][1])
            if sentenceid in rows[j] and rows[j][3] == "head":
                list1.append(rows[j][2])

        k = len(list0)
        m = len(list1)
        s = 0
        f=open("Chunk-Details.txt","w")
        for i in range(0,k):
            s = 0
            f.write(list0[i])
            f.write("Head:"+list1[i])
            for j in range(0,leng):
                if sentenceid in rows[j] and list0[i] == rows[j][1]:
                    s = s+1
                    f.write("word "+str(s)+": "+rows[j][2])
            f.write("\n")
        f.close()

    elif choice == "9":
        sentenceid0 = input("Enter the sentence ID to obtain words of a sentence and corresponding transliterations")
        sentenceid = "'"+sentenceid0+"'"
        cursor.execute('Select sid,word, translit from Tword where sid ='+sentenceid)
        rows = cursor.fetchall()
        leng = len(rows)
        f=open('Word-Translit.txt','w')
        for j in range(0,leng):
            f.write(rows[j][1]+"-"+rows[j][2])
            f.write("\n")
        f.close()

    elif choice == "10":
        sentenceid0 = input("Enter the sentence ID to obtain gender information")
        sentenceid = "'"+sentenceid0+"'"
        cursor.execute('select sid,word,gender from Tword where gender != "NULL" and sid ='+sentenceid)
        rows = cursor.fetchall()
        leng = len(rows)
        f=open("Word-Gender.txt","w")
        for j in range(0,leng):
            f.write(rows[j][1]+"-"+rows[j][2])
            f.write("\n")
        f.close()

    elif choice == "11":
        pick=input('Enter relation: ')
        pick1="'"+pick+"'"
        str1='SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wordid = c.parent AND p.sid = c.sid WHERE c.rel='+pick1+' GROUP BY p.pos_UD, c.pos_UD;'
        curr=conn.cursor()
        curr.execute(str1)
        myresult = curr.fetchall()
        n = len(myresult)
        for i in range(n):
            print('p_pos: '+myresult[i][0]+'\tc_pos: '+myresult[i][1]+'\tn_occurances: '+str(myresult[i][2]))
        pick=input('Do u want to check cases(y/n): ')
        if pick=='y':
            pick=input('Enter pos of parent: ')
            pick2=input('Enter pos of child: ')
            pick3="'"+pick+"'"
            pick4="'"+pick2+"'"
            str1='SELECT p.word, c.word, p.sid, p.filename FROM Tword p INNER JOIN Tword c ON p.wordid = c.parent AND p.sid = c.sid WHERE c.rel='+pick1+'AND p.pos_UD='+pick3+' AND c.pos_UD='+pick4+';'
            curr.execute(str1)
            myresult = curr.fetchall()
            n = len(myresult)
            f = open('relation_to_word_mapping.txt', 'w')
            for i in range(n):
                f.write('filename: '+myresult[i][3]+'\tsentence_id: '+myresult[i][2]+'\tp_word: '+myresult[i][0]+'\tc_word: '+myresult[i][1]+'\n')
            f.close()

    elif choice == "12":
        cursor.execute('Select distinct rel from Tword')
        rows = cursor.fetchall()
        leng = len(rows)
        print("The relation list in the corpus is:")
        for j in range(0,leng):
            print(rows[j][0])
        rel1_0 = input("Enter sibling relationship 1")
        rel2_0 = input("Enter sibling relationship 2")
        rel1 = "'"+rel1_0+"'"
        rel2 = "'"+rel2_0+"'"
        cursor1=conn.cursor()
        cursor1.execute('select distinct a.sid,b.parent from Tword a, Tword b where a.parent = b.parent  and a.sid = b.sid  and a.rel ='+rel1+' and b.rel ='+rel2)
        rows = cursor1.fetchall()
        for i in range(0,len(rows)):
            print(rows[i])

    elif choice == "13":
        f = open('noun-verb.txt','w')
        str1="SELECT t.word,t.pos_UD,t.rel,c.sentence,t.wordid,c.sid FROM Tword t INNER JOIN Tsentence c ON t.sid=c.sid ;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        for i in range(n):
            if abc[i][1]=='NOUN' and abc[i+1][1]=='VERB' :
                f.write("Sentence: "+ abc[i][3]+"  Sentence ID:"+ abc[i][5] +"\nNOUN ID:"+str(abc[i][4])+" Word:"+abc[i][0]+"\tVERB ID:"+str(abc[i+1][4])+" Word:"+abc[i+1][0] +"\trelation:"+abc[i][2]+"\n")
        f.close()


    elif choice == "14":
        cursor.execute('SELECT a.sid,a.word,b.word,a.rel,a.wordid,b.wordid from Tword a join Tword b on a.filename=b.filename and a.sid=b.sid where b.wordid=a.parent and a.rel="obl";')
        myresult = cursor.fetchall()

        cur1 = conn.cursor()
        cur2 = conn.cursor()
        n=len(myresult)
        f= open("obl_case_mark_child.dat",'w')
        for i in range(n):

            str1 = myresult[i][0]
            str1="'"+str1+"'"
            cur1.execute('SELECT sentence from Tsentence where sid='+str1)
            res = cur1.fetchall()

            final=""
            id=myresult[i][4]
            id="'"+str(id)+"'"

            cur2.execute('SELECT word,rel from Tword where parent='+str(id)+' and sid='+str1)
            res2 = cur2.fetchall()

            for j in range(len(res2)):
                if res2[j][1]=='case' or res2[j][1]=='mark':
                    final += res2[j][0]
            if final=="":
                final="no child with 'case' or 'mark'"
            print("sentenceid: "+myresult[i][0]+"\tcid: "+str(myresult[i][4])+"\tchild: "+myresult[i][1]+"\tpid: "+str(myresult[i][5])+"\tparent: "+myresult[i][2]+"\trelation: "+myresult[i][3]+"\tgrandchild: "+final)

            f.write("sentenceid: "+myresult[i][0]+"\tcid: "+str(myresult[i][4])+"\tchild: "+myresult[i][1]+"\tpid: "+str(myresult[i][5])+"\tparent: "+myresult[i][2]+"\trelation: "+myresult[i][3]+"\tgrandchild: "+final+'\n')
        f.close()
    elif choice == '15':
        cursor.execute('SELECT a.sid,a.word,b.word,a.rel,a.wordid,b.wordid from Tword a join Tword b on a.filename=b.filename and a.sid=b.sid where b.wordid=a.parent and a.rel="obl";')
        myresult = cursor.fetchall()

        cur1 = conn.cursor()
        cur2 = conn.cursor()
        n=len(myresult)
        f= open("obl_no_case_mark_child.dat",'w')
        for i in range(n):

            str1 = myresult[i][0]
            str1="'"+str1+"'"
            cur1.execute('SELECT sentence from Tsentence where sid='+str1)
            res = cur1.fetchall()

            final=""
            id=myresult[i][4]
            id="'"+str(id)+"'"

            cur2.execute('SELECT word,rel from Tword where parent='+str(id)+' and sid='+str1)
            res2 = cur2.fetchall()

            for j in range(len(res2)):
                if res2[j][1]=='case' or res2[j][1]=='mark':
                    final += res2[j][0]
            if final=="":
                final="no child with 'case' or 'mark'"
            if final=="no child with 'case' or 'mark'":

                print("sentenceid: "+myresult[i][0]+"\tcid: "+str(myresult[i][4])+"\tchild: "+myresult[i][1]+"\tpid: "+str(myresult[i][5])+"\tparent: "+myresult[i][2]+"\trelation: "+myresult[i][3]+"\tgrandchild: "+final)
                f.write("sentenceid: "+myresult[i][0]+"\tcid: "+str(myresult[i][4])+"\tchild: "+myresult[i][1]+"\tpid: "+str(myresult[i][5])+"\tparent: "+myresult[i][2]+"\trelation: "+myresult[i][3]+"\tgrandchild: "+final+'\n')
        f.close()
    elif choice == '16':
        cursor.execute('SELECT a.sid,a.wordid,a.word,a.rel,b.wordid,b.word,b.rel from Tword a join Tword b on a.sid=b.sid where a.rel="cc" and a.parent=b.parent and b.rel="conj";')
        myresult = cursor.fetchall()
        n=len(myresult)
        cur1 = conn.cursor()
        f= open("either_or_sentences.dat",'w')
        for i in range(n):

            sibling=myresult[i][4]
            sent=myresult[i][0]
            sent="'"+sent+"'"

            cur1.execute('SELECT sid,wordid,word,rel,parent from Tword where rel="cc" and parent='+str(sibling)+' and sid='+sent)
            res = cur1.fetchall()

            for j in range(len(res)):
                print("sentence: "+sent+"\tnode1_id: "+str(myresult[i][1])+"\tnode1: "+myresult[i][2]+"_"+myresult[i][3]+"\tnode2_id: "+str(myresult[i][4])+"\tnode2: "+myresult[i][5]+"_"+myresult[i][6]+"\tchild_id: "+str(res[j][1])+"\tchild: "+res[j][2]+"_"+res[j][3])
                f.write("sentence: "+sent+"\tnode1_id: "+str(myresult[i][1])+"\tnode1: "+myresult[i][2]+"_"+myresult[i][3]+"\tnode2_id: "+str(myresult[i][4])+"\tnode2: "+myresult[i][5]+"_"+myresult[i][6]+"\tchild_id: "+str(res[j][1])+"\tchild: "+res[j][2]+"_"+res[j][3]+"\n")
        f.close()
    elif choice == '17':
        rel1=input("Enter the relation 1:")
        rel2=input("Enter the relation 2:")
        str1="SELECT r.rel,r.sid,r.word,r.wordid,c.sentence FROM Tword r INNER JOIN Tsentence c WHERE r.sid=c.sid;"
        curr=conn.cursor()
        curr.execute(str1)
        abc=curr.fetchall()
        n=len(abc)
        st=[]
        f=open("sid_relation.dat","w")
        for i in range(n):
            if(abc[i][1] not in st):
                if(rel1 == abc[i][0] or rel2==abc[i][0]):
                    if(rel1==abc[i][0]):
                        temp='1'
                    elif(rel2==abc[i][0]):
                        temp='2'
                    j=i
                    num=0
                    print(i)
                    while(abc[j][3]!='1'):
                        if(temp=='1'):
                            if(rel2 == abc[j][0]):
                                num=j
                                st.append(abc[i][1])
                        elif(temp=='2'):
                            if(rel1 == abc[j][0]):
                                num=j
                                st.append(abc[i][1])

                        if(num!=0):
                            f.write("SentID: "+str(abc[i][1])+"\tWord1:"+abc[i][2]+"("+abc[i][0]+")"+"\tWord2:"+abc[j][2]+"("+abc[j][0]+")"+"Sentence:"+abc[i][4]+"\n")
                            break
                        j=j+1
        f.close()


    elif choice == '18':
        cursor.execute('SELECT a.sid,a.wordid,a.word,a.rel,a.pos_UD,b.wordid,b.word,b.rel,b.pos_UD from Tword a join Tword b on a.sid=b.sid and a.filename=b.filename where b.parent=a.wordid and b.pos_UD="ADP";')
        myresult = cursor.fetchall()

        n=len(myresult)

        print(n)
        auxlist = []
        i=0
        f1= open("ADP_all_cases.dat",'w')
        f2= open("ADP_unique_cases.dat",'w')
        while (i<n):

            final=""

            x= myresult[i][0]
            y= myresult[i][1]
            flag=0
            k=i
            while (k<n and myresult[k][0]==x and myresult[k][1]==y):
                final+=myresult[k][6]+'_'
                k=k+1
                flag=flag+1

            if final not in auxlist:
                auxlist.append(final)
                print("sentenceid: "+myresult[i][0]+"\tid: "+str(myresult[i][1])+"\tparent: "+myresult[i][2]+'\tPOS: '+myresult[i][4]+"\tP_relation: "+myresult[i][3]+"\tvibhakti: "+final)
                f2.write("sentenceid: "+myresult[i][0]+"\tid: "+str(myresult[i][1])+"\tparent: "+myresult[i][2]+'\tPOS: '+myresult[i][4]+"\tP_relation: "+myresult[i][3]+"\tvibhakti: "+final+'\n')
            if i<n:
                print("sentenceid: "+myresult[i][0]+"\tid: "+str(myresult[i][1])+"\tparent: "+myresult[i][2]+'\tPOS: '+myresult[i][4]+"\tP_relation: "+myresult[i][3]+"\tvibhakti: "+final)
                f1.write("sentenceid: "+myresult[i][0]+"\tid: "+str(myresult[i][1])+"\tparent: "+myresult[i][2]+'\tPOS: '+myresult[i][4]+"\tP_relation: "+myresult[i][3]+"\tvibhakti: "+final+'\n')
            if flag>1:
                i=i+flag
            else:
                i=i+1

        print(len(auxlist))
        f1.close()
        f2.close()
    elif choice == '19':

        sentenceid=input("Enter the sentence id: ")
        spl=re.split(r'-',sentenceid)[0]
        f=open("./treebanks/UD_Hindi-HDTB/hi_hdtb-ud-"+spl+".conllu","r").readlines()
        f1=open("./conll/conll_"+sentenceid+".dat","w")
        n=len(f)



        for i in range(0,n):
            if sentenceid in f[i]:
                j=i+2
                while(f[j]!='\n'):
                    g=re.split(r'\t',f[j].rstrip())
                    con = WXC(order='utf2wx')
                    g[1]=con.convert(g[1])
                    g[2]="_"
                    g[4]="_"
                    g[5]="_"
                    g[8]="_"
                    g[9]="_"
                    for x in g:
                        f1.write(x+'\t')
                    f1.write('\n')
                    j=j+1
                break

        f1.close()
        cmd='python3 Createdata.py '+sentenceid
        os.system(cmd)
    elif choice == '20':
        fname = input("enter the filename which has sentenceid as first column: ")
        print(fname)
        l = open(fname,'r').readlines()

        n= len(l)
        foldern = input("enter the folder name where the trees will stored: ")

        cmd='mkdir ./output/'+foldern
        os.system(cmd)
        cmd='mkdir ./conll/'+foldern
        os.system(cmd)

        print("\t1.View only first ten trees\n\t2.View all trees\n")

        option = input("enter the choice")
        if option == "1":
            n=10
        elif option == "2":
            n=len(l)

        for i in range(n):

            x = re.split(r'\t',l[i])
            y = re.split(r' ',x[0])
            y[1]=y[1].replace("'","")
            print(y[1])
            spl=re.split(r'-',y[1])[0]

            f=open("./treebanks/UD_Hindi-HDTB/hi_hdtb-ud-"+spl+".conllu","r").readlines()
            f1=open("./conll/conll_"+y[1]+".dat","w")
            x=len(f)


            for i in range(0,x):
                if y[1] in f[i]:

                    j=i+2
                    while(f[j]!='\n'):
                        g=re.split(r'\t',f[j].rstrip())
                        con = WXC(order='utf2wx')
                        g[1]=con.convert(g[1])
                        g[2]="_"
                        g[4]="_"
                        g[5]="_"
                        g[8]="_"
                        g[9]="_"
                        for x in g:
                            f1.write(x+'\t')
                        f1.write('\n')
                        j=j+1
                    break

            f1.close()
            cmd='python3 Createdata.py '+y[1]+' '+foldern
            os.system(cmd)

    elif choice =='21':
        #str1="Select a.sid,a.word, b.word, a.rel,a.pos_UD from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid and a.word='ही';"
        str1="Select a.sid,a.word, b.word, a.rel,a.pos_UD from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        f=open("hI-case1.txt","w")
        for i in range(n):
            if(abc[i][1] == 'ही'):
                print(abc[i][0])
                f.write("Sentence Id: "+abc[i][0]+"\tParent:" +abc[i][2]+"\tRel:"+abc[i][3]+"\tpos_UD:"+abc[i][4])
                w=abc[i][0]
                str2="Select a.sid,b.word from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid and a.word='ही'"
                cursor1=conn.cursor()
                cursor1.execute(str2)
                abc1=cursor1.fetchall()
                n1=len(abc1)
                temp=0
                for j in range(n1):
                    if(abc1[j][0]==w):
                        if(abc1[j][1]=='ही'):
                            temp=1
                            f.write("\t YES")
                if(temp==0):
                    f.write(" \tNO")
                f.write("\n")

        f.close()



    elif choice =='22':
        #str1="Select a.sid,a.word, b.word, a.rel,a.pos_UD from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid and a.word='ही';"
        str1="Select a.sid,a.word, b.word, a.rel,a.pos_UD from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        f=open("BI-case1.txt","w")
        for i in range(n):
            if(abc[i][1] == 'भी'):
                print(abc[i][0])
                f.write("Sentence Id: "+abc[i][0]+"\tParent:" +abc[i][2]+"\tRel:"+abc[i][3]+"\tpos_UD:"+abc[i][4])
                w=abc[i][0]
                str2="Select a.sid,b.word from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid and b.word='भी'"
                cursor1=conn.cursor()
                cursor1.execute(str2)
                abc1=cursor1.fetchall()
                n1=len(abc1)
                temp=0
                for j in range(n1):
                    if(abc1[j][0]==w):
                        if(abc1[j][1]=='भी'):
                            temp=1
                            f.write("\t YES")
                if(temp==0):
                    f.write(" \tNO")
                f.write("\n")

        f.close()

    elif choice == '23':
        cursor.execute('Select distinct rel from Tword')
        rows = cursor.fetchall()
        leng = len(rows)
        print(leng)
        str2=[]
        for j in range(0,leng):
            str2.append(rows[j][0])
        print("The various relaations present are :")
        print(str2)
        cursor.execute("Select a.sid,a.word,b.word,b.wordid,a.rel,a.pos_UD from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid;")
        abc=cursor.fetchall()
        n=len(abc)
        sentid=[]
        str3=[]
        cursor1=conn.cursor()
        f=open("Relation_Children_FirstOccurrence.txt","w")
        for i in range(0,n):
            if(abc[i][0] not in sentid):
                str1="Select a.sid,a.word,b.word,b.wordid,a.rel,a.pos_UD,a.wordid,a.parent from Tword a,Tword b where a.parent = b.wordid and a.sid = b.sid and a.sid="+"'"+abc[i][0]+"'"
                cursor1.execute(str1)
                abc1=cursor1.fetchall()
                n1=len(abc1)
                for j in range(0,n1):
                    if(abc1[j][4] in str2):
                        for k in range(0,n1):
                            if(int(abc1[j][6])==int(abc1[k][7])):
                                print(abc1[j][6],abc1[k][7])
                                str2.remove(abc1[j][4])
                                str3.append(abc1[j][4])
                                f.write("Sentence Id:"+abc[i][0]+"\tRelation:"+abc1[j][4]+"\tWord Id:"+str(abc1[j][6])+"\n")
                                break
                print(str2)
                print(abc[i][0])
                sentid.append(abc[i][0])
        print("The relations that don't have a children are:")
        print(str2)
        print("The relations that have a children are:")
        print(str3)
        f.close()

    elif choice=='24':
        sentid=input('Enter the sentence id:')
        str1="select sentence,sid,SNo from Tsentence where sid='"+sentid+"';"
        str2="select sentence,sid,SNo,filename from Tsentence;"
        cursor.execute(str1)
        cursor10.execute(str2)
        abc=cursor.fetchall()
        abc1=cursor10.fetchall()
        cursor.execute(str2)
        abc2=cursor.fetchall()
        n=len(abc)
        n1=len(abc1)
        n2=len(abc2)
        f=open('Sentence.txt','w')
        f.write("CONLL_DATABSE\n")
        k=1
        for i in range(n2):
            f.write(str(k)+" ")
            k=k+1
            f.write("Sentence:"+abc2[i][0]+"\tID:"+str(abc2[i][1])+"\tSNO:"+str(abc2[i][2])+"\n")
        f.write('SSF DATABASE')
        k=1
        for i in range(n1):
            f.write(str(k)+" ")
            k=k+1
            f.write("Sentence:"+abc1[i][0]+"\tID:"+str(abc1[i][1])+"\tSNO:"+str(abc1[i][2])+"\n")
        f.close()
        temp=0
        for i in range(n):
            for j in range(n1):
                #print(type(abc[i][0]),type(abc1[j][0]))
                if(abc[i][0] in abc1[j][0]):
                    print("The particulars of your sentence in the SSF database is:"+"Sentence:"+abc1[j][0]+"\tID:"+str(abc1[j][1])+"\tSNO:"+str(abc1[j][2])+"\tfilename:"+abc1[j][3]+"\n")
                    temp=1
                    break
        if(temp==0):
            print("The sentence is not present in the SSF database")

    elif choice == '25':
        print("Please press N or n to exit the query engine\n")
    ip = input("Do you want to continue(y/n)?")
    if ip=="Y" or ip=='y':
        i = 1
    else:
        i = 0
