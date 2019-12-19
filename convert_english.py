import glob
import re
path="/home/guruprasad/Desktop/Intern_IIITH/treebanks/UD_English-EWT/*.conllu"
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
sentenceid=input("Enter the sentecne id:")
sentenceid1="{'"+sentenceid
sentenceid2=re.split(r'-',sentenceid1)
sentenceid3=sentenceid2[0]+"-"+sentenceid2[1]
print(sentenceid3)
for i in range(n):
    d=re.split(r',',str(list[i]))
    if(sentenceid3 == d[0]):
        path=d[-1]
        path1=re.split(r'\'',path)[0]
f=open("/home/guruprasad/Desktop/Intern_IIITH/treebanks/UD_English-EWT/"+path1,"r").readlines()
n=len(f)
f1=open("/home/guruprasad/Desktop/Intern_IIITH/E_conll.dat","w")
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
f1.close()
