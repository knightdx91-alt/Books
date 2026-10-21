import sys,ast,re,os
B='/home/user/Books/books/sygl-book/evaluations/fixsets/'
def load(fn,name):
    src=open(B+fn).read()
    m=re.search(r'^'+name+r'\s*=\s*\[',src,re.M)
    i=m.end()-1; depth=0
    # parse the list literal using ast on the substring up to matching bracket
    for j in range(i,len(src)):
        c=src[j]
    node=ast.parse(src)
    for st in node.body:
        if isinstance(st,ast.Assign) and st.targets[0].id==name:
            return ast.literal_eval(st.value)
sets=[]
for ch,o,n in load('muse-round1-B1-B12.py','E'): sets.append(('R1',ch,o,n))
for i,ch,o,n in load('close-ch01-09.py','FIXES'): sets.append((i,ch,o,n))
for i,ch,o,n in load('close-ch10-18.py','EDITS'): sets.append((i,'%02d'%int(ch),o,n))
for i,ch,o,n in load('close-ch19-30.py','F'): sets.append((i,'%02d'%int(ch),o,n))
for fn in ['gpt-ch01-09.py','gpt-ch10-18.py','gpt-ch19-30.py','author-decisions.py']:
    for i,ch,o,n in load(fn,'G'): sets.append((i,'%02d'%int(ch),o,n))
os.chdir(sys.argv[1] if len(sys.argv)>1 else '/home/user/Books/books/sygl-book'); miss=0
for i,ch,o,n in sets:
    p=f'manuscript/chapter-{ch}.md'; t=open(p).read(); c=t.count(o)
    if c!=1: print('MISS',i,ch,c,o[:70]); miss+=1; continue
    open(p,'w').write(t.replace(o,n))
print('applied',len(sets)-miss,'missed',miss)
