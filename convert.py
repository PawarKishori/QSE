import re
from wxconv import WXC
sentenceid=input("Enter the sentence id: ")
spl=re.split(r'-',sentenceid)[0]
f=open("/home/guruprasad/Desktop/Intern_IIITH/treebanks/UD_Hindi-HDTB/hi_hdtb-ud-"+spl+".conllu","r").readlines()
f1=open("/home/guruprasad/Desktop/Intern_IIITH/conll.dat","w")
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
            print(g)
            for x in g:
                f1.write(x+'\t')
            f1.write('\n')
            j=j+1
        break
f1.close()
