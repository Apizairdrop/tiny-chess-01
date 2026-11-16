import json,os,sys
from urllib.request import urlopen,Request
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit("no env")
def post(p,b):
 q=Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with urlopen(q)as r:return json.load(r)
 except Exception as e:sys.exit(f"{p} {e}")
V=[0,100,320,330,500,900,0]
P=[[0,0,0,0,0,0,0,0,5,10,10,-20,-20,10,10,5,5,-5,-10,0,0,-10,-5,5,0,0,0,20,20,0,0,0,5,5,10,25,25,10,5,5,10,10,20,30,30,20,10,10,50,50,50,50,50,50,50,50,0,0,0,0,0,0,0,0],[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50],[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20],[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0],[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20],[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]]
CR=[15]*128
for s,m in((0,13),(7,14),(4,12),(112,7),(119,11),(116,3)):CR[s]=m
KG=[0,0]
def parse(f):
 b=[0]*128;p=f.split();r=7;q=0
 for c in p[0]:
  if c=="/":r-=1;q=0
  elif c.isdigit():q+=int(c)
  else:b[r*16+q]=("PNBRQK".find(c.upper())+1)*(1 if c.isupper()else -1);q+=1
 t=1 if p[1]=="w"else -1;c=0
 for ch,v in zip("KQkq",(1,2,4,8)):
  if ch in p[2]:c|=v
 e=-1
 if p[3]!="-":e=(int(p[3][1])-1)*16+"abcdefgh".find(p[3][0])
 for i,v in enumerate(b):
  if v==6:KG[0]=i
  elif v==-6:KG[1]=i
 return b,t,c,e
def atk(b,s,y):
 for d in(15,17,-15,-17):
  q=s+d
  while not q&136:
   v=b[q]
   if v:
    if v*y>0 and abs(v)in(3,5):return 1
    break
   q+=d
 for d in(1,-1,16,-16):
  q=s+d
  while not q&136:
   v=b[q]
   if v:
    if v*y>0 and abs(v)in(4,5):return 1
    break
   q+=d
 for d in(33,31,18,14,-14,-18,-31,-33):
  q=s+d
  if not q&136 and b[q]*y==2:return 1
 for d in(15,17,-15,-17,1,-1,16,-16):
  q=s+d
  if not q&136 and b[q]*y==6:return 1
 for d in(-1,1):
  q=s-y*16+d
  if not q&136 and b[q]*y==1:return 1
 return 0
def gen(b,t,c,e):
 ms=[];d=16*t
 for s,v in enumerate(b):
  if s&136 or v*t<=0:continue
  a=abs(v)
  if a==1:
   q=s+d
   if not q&136 and not b[q]:
    if q//16 in(0,7):
     for p in(5,4,3,2):ms.append(s|q<<7|p<<14)
    else:
     ms.append(s|q<<7)
     if s//16==(1 if t>0 else 6):
      q2=s+2*d
      if not b[q2]:ms.append(s|q2<<7)
   for o in(-1,1):
    q=s+d+o
    if q&136:continue
    if b[q]*t<0:
     if q//16 in(0,7):
      for p in(5,4,3,2):ms.append(s|q<<7|p<<14)
     else:ms.append(s|q<<7)
    elif q==e:ms.append(s|q<<7)
  elif a==2:
   for o in(33,31,18,14,-14,-18,-31,-33):
    q=s+o
    if not q&136 and b[q]*t<=0:ms.append(s|q<<7)
  elif a==6:
   for o in(15,17,-15,-17,1,-1,16,-16):
    q=s+o
    if not q&136 and b[q]*t<=0:ms.append(s|q<<7)
   if t>0:
    if c&1 and not b[5]and not b[6]and b[7]==4 and not atk(b,4,-1)and not atk(b,5,-1)and not atk(b,6,-1):ms.append(4|6<<7)
    if c&2 and not b[3]and not b[2]and not b[1]and b[0]==4 and not atk(b,4,-1)and not atk(b,3,-1)and not atk(b,2,-1):ms.append(4|2<<7)
   else:
    if c&4 and not b[117]and not b[118]and b[119]==-4 and not atk(b,116,1)and not atk(b,117,1)and not atk(b,118,1):ms.append(116|118<<7)
    if c&8 and not b[115]and not b[114]and not b[113]and b[112]==-4 and not atk(b,116,1)and not atk(b,115,1)and not atk(b,114,1):ms.append(116|114<<7)
  else:
   ds=(15,17,-15,-17)if a==3 else(1,-1,16,-16)if a==4 else(15,17,-15,-17,1,-1,16,-16)
   for o in ds:
    q=s+o
    while not q&136:
     if b[q]*t>0:break
     ms.append(s|q<<7)
     if b[q]:break
     q+=o
 return ms
def make(b,t,f,to,p,e,c):
 v=b[f];cap=b[to];ep=0;rf=-1
 if abs(v)==1 and to==e and not cap:cap=b[to-16*t];b[to-16*t]=0;ep=1
 b[to]=v;b[f]=0
 if p:b[to]=p*t
 if abs(v)==6:
  KG[(1-t)//2]=to
  if abs(to-f)==2:
   if to>f:rf=to+1;b[to-1]=b[rf];b[rf]=0
   else:rf=to-2;b[to+1]=b[rf];b[rf]=0
 ne=(f+to)//2 if abs(v)==1 and abs(to-f)==32 else -1
 nc=c&CR[f]&CR[to]
 return cap,nc,ne,ep,rf
def unmake(b,t,f,to,p,cap,ep,rf):
 v=b[to]
 if p:v=t
 b[f]=v;b[to]=0
 if ep:b[to-16*t]=cap
 else:b[to]=cap
 if rf>=0:
  if to>f:b[rf]=b[to-1];b[to-1]=0
  else:b[rf]=b[to+1];b[to+1]=0
 if abs(v)==6 and not p:KG[(1-t)//2]=f
def legal(b,t,c,e):
 out=[]
 for m in gen(b,t,c,e):
  f=m&127;to=m>>7&127
  cap,nc,ne,ep,rf=make(b,t,f,to,m>>14&7,e,c)
  if not atk(b,KG[(1-t)//2],-t):out.append(m)
  unmake(b,t,f,to,m>>14&7,cap,ep,rf)
 return out
def ev(b):
 s=0;wb=0;bb=0
 for i,v in enumerate(b):
  if v and not i&136:
   a=abs(v)
   if a==3:
    if v>0:wb+=1
    else:bb+=1
   sq=(i&7)+(i//16)*8 if v>0 else(i&7)+(7-i//16)*8
   s+=(V[a]+P[a-1][sq])*(1 if v>0 else -1)
 if wb>=2:s+=25
 if bb>=2:s-=25
 return s
TT={}
KI=[[0,0]for _ in range(64)]
N=[0]
BD=200000
class TO(Exception):pass
def qs(b,t,al,be,ply,e):
 N[0]+=1
 if N[0]>BD:raise TO
 s=ev(b)*t
 if s>=be:return be
 if s>al:al=s
 if ply>10:return al
 ch=atk(b,KG[(1-t)//2],-t)
 for m in legal(b,t,0,e) if ch else gen(b,t,0,e):
  f=m&127;to=m>>7&127
  if not ch and not b[to] and not(m>>14&7) and to!=e:continue
  cap,nc,ne,ep,rf=make(b,t,f,to,m>>14&7,e,0)
  if atk(b,KG[(1-t)//2],-t):
   unmake(b,t,f,to,m>>14&7,cap,ep,rf);continue
  try:sc=-qs(b,-t,-be,-al,ply+1,ne)
  except TO:unmake(b,t,f,to,m>>14&7,cap,ep,rf);raise
  unmake(b,t,f,to,m>>14&7,cap,ep,rf)
  if sc>=be:return be
  if sc>al:al=sc
 return al
def order(b,t,ms,tt,ply):
 def sc(m):
  f=m&127;to=m>>7&127
  if tt is not None and m==tt:return -1000000
  if b[to]:return -(10000+V[abs(b[to])]*10-V[abs(b[f])])
  if m==KI[ply][0]:return -5000
  return -m
 return sorted(ms,key=sc)
def search(b,t,dep,al,be,ply,c,e):
 N[0]+=1
 if N[0]>BD:raise TO
 if dep<=0:return qs(b,t,al,be,ply,e)
 k=(tuple(b),t,c,e)
 tt=TT.get(k)
 if tt and tt[0]>=dep:
  _,sc,fl,mm=tt
  if fl==0:return sc
  if fl==1 and sc>=be:return sc
  if fl==2 and sc<=al:return sc
 ms=legal(b,t,c,e)
 if not ms:return -100000+ply if atk(b,KG[(1-t)//2],-t)else 0
 ms=order(b,t,ms,tt[3]if tt else None,ply)
 best=-10**9;bm=None;oa=al
 for m in ms:
  f=m&127;to=m>>7&127
  cap,nc,ne,ep,rf=make(b,t,f,to,m>>14&7,e,c)
  try:sc=-search(b,-t,dep-1,-be,-al,ply+1,nc,ne)
  except TO:unmake(b,t,f,to,m>>14&7,cap,ep,rf);raise
  unmake(b,t,f,to,m>>14&7,cap,ep,rf)
  if sc>best:best=sc;bm=m
  if sc>al:al=sc
  if al>=be:
   if not b[to]:KI[ply][1]=KI[ply][0];KI[ply][0]=m
   break
 TT[k]=(dep,best,2 if best<=oa else 1 if best>=be else 0,bm)
 return best
def root(b,t,c,e):
 best=None
 ms=legal(b,t,c,e)
 if not ms:return None
 N[0]=0
 for dep in range(1,64):
  try:search(b,t,dep,-10**9,10**9,0,c,e)
  except TO:break
  bm=TT.get((tuple(b),t,c,e),(0,0,0,None))[3]
  if bm is not None:best=bm
 if best is None:
  bs=-10**9
  for m in ms:
   f=m&127;to=m>>7&127
   cap,nc,ne,ep,rf=make(b,t,f,to,m>>14&7,e,c)
   s=ev(b)*t
   unmake(b,t,f,to,m>>14&7,cap,ep,rf)
   if s>bs:bs=s;best=m
 return best
def uci(m):
 p=m>>14&7
 return "abcdefgh"[m&7]+str(((m>>4)&7)+1)+"abcdefgh"[m>>7&7]+str(((m>>11)&7)+1)+("nbrq"[p-2]if p else"")
while True:
 g=post("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  b,t,c,e=parse(g["fen"])
  m=root(b,t,c,e)
  if m is None:post("/resign",{"game":g["game"]});break
  g=post("/move",{"game":g["game"],"move":uci(m)})
 print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
