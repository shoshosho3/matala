def header():
  head="0xfee1900d"
  n_head=""
  for h in range(len(head)-1,1,-2):
    n_head+= "\\x"+head[h-1:h+1]
  return n_head

def rec1(first,num,word,ch):
  if num!=first:
    for s in range(0,256):
      if s==0 and num==0:
        word+="\\"+format(first,"#04x")
      rec1(first,num+1,word+"\\"+format(s,"#04x"),ch)
  else:
    if ch:
      for l in range(0,256):
        sects(l,word)
    else:
      print(word)

def sects(n,w):
  if n==0:
    print(w+"\\"+format(n,"#04x"))
  else:
    rec1(n,0,w,w==header())

for i in range(0,256):
  sects(i,header())
