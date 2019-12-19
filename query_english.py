import sqlite3
import sys
import glob
import re
import os

conn = sqlite3.connect('Treebank_English.db')
print ('Opened database successfully');
cursor = conn.cursor()

i = 1

while i == 1:
    print("\tSelect an option to execute one of the following quries:\n\t1.No of words in a sentence\n\t2.No of minor field types and information\n\t3.POS combinations and respective records\n\t4.Identify parent(word) corresponding to each word in a given sentence\n\t5.To find the word and it's gender in a given sentence\n\t6.To obtain information about a given relation, including corresponding POS's and sentences\n\t7.To obtain sibling relations in a given sentence\n\t8.To obtain Noun followed by verb cases and print relation\n\t9.To print the sentences for single constructs\n\t10.Dual Constructs with consecutive words.To print the details of these constructs\n\t11.Dual Constructs and to print the parents and child \n\t12.To print the tree of a sentence given it's id\n\t13.To print the tree of all sentences in a file\n\t14.Quit \n\t Enter a number from 1-13 for queries and 14 to exit.")
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
        f = open('morphdetails_english.txt','w')
        Options = input("Enter one of the following fields to view its types:Definite\nPronType\nNumber1\nMood\nPerson\nTense\nVerbForm\nNumType\nDegree\nCase1\nGender1\nPoss\nForeign1\nVoice\nReflex\nTypo\nAbbr\n")
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


    elif choice == "3":
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
            f=open("UD-ILMT_occurrence_english.txt","w")
            for j in range(0,n):
                if pos_UD_type==abc1[j][1] and pos_ILMT_type==abc1[j][2]:
                    f.write("pos_UD:" + abc1[j][1] +"\t pos_ILMT:" + abc1[j][2] + " \t word:" +abc1[j][0] +"\n")
        f.close()

    elif choice == "4":
        sentenceid = input("Enter the sentence ID to word-parent-rel pairs")
        cursor.execute('Select a.sid,a.word, b.word, a.rel from Tword a,Tword b where a.parent = b.wid and a.sid = b.sid')
        rows = cursor.fetchall()
        leng = len(rows)
        f=open("word-parent_english.txt","w")
        for j in range(0,leng):
            if sentenceid in rows[j]:
                f.write(str(rows[j][1:4]))
                f.write("\n")
        f.close()
    elif choice == "5":
        sentenceid0 = input("Enter the sentence ID to obtain gender information")
        sentenceid = "'"+sentenceid0+"'"
        cursor.execute('select sid,word,gender1 from Tword where gender1 != "NULL" and sid ='+sentenceid)
        rows = cursor.fetchall()
        leng = len(rows)
        f=open("Word-Gender_english.txt","w")
        for j in range(0,leng):
            f.write(rows[j][1]+"-"+rows[j][2])
            f.write("\n")
        f.close()

    elif choice == "6":
        pick=input('Enter relation: ')
        pick1="'"+pick+"'"
        str1='SELECT p.pos_UD, c.pos_UD, count(1) FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.rel='+pick1+' GROUP BY p.pos_UD, c.pos_UD;'
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
            str1='SELECT p.word, c.word, p.sid, p.filename FROM Tword p INNER JOIN Tword c ON p.wid = c.parent AND p.sid = c.sid WHERE c.rel='+pick1+'AND p.pos_UD='+pick3+' AND c.pos_UD='+pick4+';'
            curr.execute(str1)
            myresult = curr.fetchall()
            n = len(myresult)
            f = open('relation_to_word_mapping_english.txt', 'w')
            for i in range(n):
                f.write('filename: '+myresult[i][3]+'\tsentence_id: '+myresult[i][2]+'\tp_word: '+myresult[i][0]+'\tc_word: '+myresult[i][1]+'\n')
            f.close()
    elif choice == "7":
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

    elif choice == "8":
        f = open('noun-verb_english.txt','w')
        str1="SELECT t.word,t.pos_UD,t.rel,c.sentence,t.wid,c.sid FROM Tword t INNER JOIN Tsentence c ON t.sid=c.sid ;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        for i in range(n):
            if abc[i][1]=='NOUN' and abc[i+1][1]=='VERB' :
                f.write("Sentence:"+ abc[i][3]+"  Sentence ID:"+ abc[i][5] +"\nNOUN ID:"+str(abc[i][4])+" Word:"+abc[i][0]+"\tVERB ID:"+str(abc[i+1][4])+" Word:"+abc[i+1][0] +"\trelation:"+abc[i][2]+"\n")
        f.close()
    elif choice =='9':
        name=input("Choose one of the following constructs\n\t1.although\n\t2.while\n\t3.as\n\t4.because\n\t5.but\n\t6.since\n\t7.unless\n\t8.whether\n\t9.or\n\t10.and\nChoose the construct you want to see.For example: while\nNOTE:DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!\n")
        name1=name.capitalize()
        print(name+"\t"+name1)
        str1="select sid,word from Tword where word='" + name +"'or word='"+ name1 +"';"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        cursor1=conn.cursor()
        f=open(name+'.txt','w')
        for i in range(n):
            str2="select sentence,sid from Tsentence where sid='"+abc[i][0]+"';"
            cursor1.execute(str2)
            abc1=cursor1.fetchall()
            n1=len(abc1)
            for j in range(n1):
                f.write("Sentence Id:"+abc1[j][1] +"\tSentence:" +abc1[j][0]+"\n")
        f.close()
        print("NOTE:TO VIEW THE TREES OF THE VARIOUS CASES RUN QUERY NUMBER 13\n")
    elif choice =='10':
        print("Choose one of the following dual constructs:\n\t1.even-if\n\t2.even-though\nNOTE:DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!\n")
        name1=input("Enter the first word of the construct you want to see Example:even\n")
        name2=input("Enter the second word of the construct you want to see Example:if\n")
        name1c=name1.capitalize()
        str1="Select a.sid,a.filename,a.wid,a.word,b.word,b.wid,a.pos_UD from Tword a,Tword b where a.parent = b.wid and a.sid = b.sid;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        st=[]
        f=open(name1+"-"+name2+".txt","w")
        for i in range(n):
            if abc[i][0] not in st:
                if abc[i][3]==name1 or abc[i][3]==name1c:
                    if abc[i+1][3]==name2 :
                        f.write("Sentence Id:"+str(abc[i][0]))
                        f.write("\t"+name1+"'s parent:"+abc[i][4]+"("+str(abc[i][5])+")\t"+name2+"'s parent:"+abc[i+1][4]+"("+str(abc[i+1][5])+")\n")
                        st.append(abc[i][0])
        f.close()
        print("NOTE:TO VIEW THE TREES OF THE VARIOUS CASES RUN QUERY NUMBER 13\n")
    elif choice == "11":
        print("Choose one of the following dual constructs:\n\t1.either-or\n\t2.neither-nor\n\t3.since-then\nNOTE:DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!")
        name1=input("Enter the first word of the construct you want to see Example:either\n")
        name2=input("Enter the second word of the construct you want to see Example:or\n")
        name1c=name1.capitalize()
        str1="Select a.sid,a.filename,a.wid,a.word,b.word,b.wid,a.pos_UD from Tword a,Tword b where a.parent = b.wid and a.sid = b.sid;"
        cursor.execute(str1)
        abc=cursor.fetchall()
        n=len(abc)
        st=[]
        f=open(name1+"_"+name2+".txt","w")
        for i in range(n):
            if abc[i][0] not in st:
                if abc[i][3]==name1 or abc[i][3]==name1c:
                    j=i+1
                    while(abc[j][2]!=1):
                        if(abc[j][3]==name2):
                            f.write("Sentence Id:"+str(abc[j][0]))
                            f.write("\t"+name1+"'s parent:"+abc[i][4]+"("+str(abc[i][5])+")\t"+name2+"'s parent:"+abc[j][4]+"("+str(abc[j][5])+")\n")
                            st.append(abc[i][0])
                            break
                        j+=1
        f.close()
        print("NOTE:TO VIEW THE TREES OF THE VARIOUS CASES RUN QUERY NUMBER 13\n")
    elif choice=='12':
        path="treebanks/UD_English-EWT/*.conllu"
        files = sorted(glob.glob(path))  # for open files of a folder
        list=[]
        for name in files:  # for open files in a sequence
            with open(name) as f:
                for line in f:
                    if '# newdoc id' in line:
                        a=re.split(r'= ',line)
                        b=re.split(r'/',name)
                        c={a[-1].rstrip()+","+ b[-1]}
                        list.append(c)
        n=len(list)
        cmd="mkdir conll"
        cmd1="mkdir conll/conll_single"
        cmd2="mkdir conll/conll_single/trees"
        os.system(cmd)
        os.system(cmd1)
        os.system(cmd2)
        sentenceid=input("Enter the sentecne id:")
        sentenceid1="{'"+sentenceid
        sentenceid2=re.split(r'-',sentenceid1)
        sentenceid3=sentenceid2[0]+"-"+sentenceid2[1]
        for i in range(n):
            d=re.split(r',',str(list[i]))
            if(sentenceid3 == d[0]):
                path=d[-1]
                path1=re.split(r'\'',path)[0]
        f=open("treebanks/UD_English-EWT/"+path1,"r").readlines()
        n=len(f)
        f1=open("conll/conll_single/E_conll.dat","w")
        f2=open('conll/conll_single/E_conll.txt','w')
        print(sentenceid)
        for i in range(0,n):
            if sentenceid in f[i]:
                j=i+2
                while(f[j]!='\n'):
                    g=re.split(r'\t',f[j].rstrip())
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

        for i in range(0,n):
            if sentenceid in f[i]:
                print("ENTER")
                text=re.split(r'=',f[i+1])[1]
                f2.write(text[1:])
                break
        f1.close()
        f2.close()
        filename="E_conll.dat"
        folder="conll_single"
        sentencefile="E_conll.txt"
        cmd='python3 E_Createdata.py ' + folder +" " + filename + " " + sentencefile

        os.system(cmd)

    elif choice =='13':
        path="treebanks/UD_English-EWT/*.conllu"
        files = sorted(glob.glob(path))  # for open files of a folder
        list=[]
        for name in files:  # for open files in a sequence
            with open(name) as f:
                for line in f:
                    if '# newdoc id' in line:
                        a=re.split(r'= ',line)
                        b=re.split(r'/',name)
                        c={a[-1].rstrip()+","+ b[-1]}
                        list.append(c)
        n=len(list)
        fname=input("Enter the name of the file:")
        filename11=re.split(r'\.',fname)[0]
        print(filename11)
        path=fname
        f4=open(path,"r").readlines()
        n1=len(f4)
        cmd="mkdir conll"
        cmd1="mkdir conll/conll_" + filename11
        cmd2="mkdir conll/conll_"+filename11+"/trees"
        os.system(cmd)
        os.system(cmd1)
        os.system(cmd2)
        #either-or_case_TEMP.txt
        for i in range(n1):
            if 'Sentence Id' in f4[i]:
                sentenceid5=re.split(r':',f4[i])[1]
                sentenceid4=re.split(r'\t',sentenceid5)[0]
                sentenceid1="{'"+sentenceid4
                sentenceid2=re.split(r'-',sentenceid1)
                sentenceid3=sentenceid2[0]+"-"+sentenceid2[1]
                for i in range(n):
                    d=re.split(r',',str(list[i]))
                    if(sentenceid3 == d[0]):
                        path=d[-1]
                        path1=re.split(r'\'',path)[0]
                        f=open("treebanks/UD_English-EWT/"+path1,"r").readlines()
                        n2=len(f)
                        pathhh="conll/conll_"+filename11+"/"+sentenceid4+".dat"
                        f1=open(pathhh,'w')
                        #str111=senteid4+".txt"
                        f2=open("conll/conll_"+filename11+"/"+sentenceid4+".txt","w")
                        for i in range(0,n2):
                            if sentenceid4 in f[i]:
                                j=i+2
                                while(f[j]!='\n'):
                                    g=re.split(r'\t',f[j].rstrip())
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
                        for i in range(0,n2):
                            if sentenceid4 in f[i]:
                                text=re.split(r'=',f[i+1])[1]
                                f2.write(text[1:])
                                break
                        f2.close()
                        f1.close()
        folder=re.split(r'/',pathhh)[-2]
        opt=int(input("Enter 1, 2 or 3: 1 if you want to view the trees for the first ten; 2 if you want to view the trees for all the sentecnes; 3 if you want to view the tree of a particular sentence :"))
        if(opt==1):
            path2="conll/conll_"+filename11+"/*.dat"
            files = sorted(glob.glob(path2))
            #print(files)  # for open files of a folder
            list=[]
            i=0
            for name in files:# for open files in a sequence
                list.append(re.split(r'/',name)[-1])
            print(list)
            for i in range(10):
                sentid=list[i]
                sentencefile1=re.split('\.',sentid)[0]
                print(sentencefile1)
                sentencefile=sentencefile1+".txt"
                cmd="python E_Createdata.py "+ folder +" "+ sentid + " "+sentencefile
                print(cmd)
                os.system(cmd)


        elif(opt==2):
            path2="conll/conll_"+filename11+"/*.dat"
            files = sorted(glob.glob(path2))  # for open files of a folder
            list=[]
            i=0
            for name in files:# for open files in a sequence
                list.append(re.split(r'/',name)[-1])
            n6=len(list)
            for i in range(n6):
                sentid=list[i]
                sentencefile1=re.split('\.',sentid)[0]
                sentencefile=sentencefile1+".txt"
                cmd="python E_Createdata.py "+ folder +" "+ sentid +" "+sentencefile
                os.system(cmd)
        elif(opt==3):
            path2="conll/conll_"+filename11+"/*.dat"
            print(path2)
            files = sorted(glob.glob(path2))  # for open files of a folder
            list=[]
            print(files)
            i=0
            for name in files:# for open files in a sequence
                list.append(re.split(r'/',name)[-1])
            n6=len(list)
            print(list)
            sentence=input("Enter the id of the sentence for which you wish to see the tree:")
            sentenceiii=sentence+".dat"
            for i in range(n6):
                if(sentenceiii== list[i]):
                    sentid=list[i]
                    sentencefile1=re.split('\.',sentid)[0]
                    sentencefile=sentencefile1+".txt"
                    cmd="python E_Createdata.py "+ folder +" "+ sentid +" "+sentencefile
                    os.system(cmd)



    elif choice =='14':
        print("Please press N or n to exit the query engine\n")
    ip = input("Do you want to continue(y/n)?")
    if ip=="Y" or ip=='y':
        i = 1
    else:
        i = 0
