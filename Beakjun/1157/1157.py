str_ = input()

str_ = str_.lower()

alpha='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')

cnt_alpha_dict = {}
for al in alpha:
    if str_.find(al)!=-1:
        cnt_alpha_dict[al] =  str_.count(al)

kks = list(cnt_alpha_dict.keys())
max_val = None



qumark_ = False
max_val = kks.pop(0)
for ki in range(len(kks)):
    if cnt_alpha_dict[max_val] < cnt_alpha_dict[kks[ki]]:
        max_val = kks[ki]
        qumark_=False
    elif cnt_alpha_dict[max_val] ==cnt_alpha_dict[kks[ki]]:
        qumark_=True

if qumark_:
    print('?')
else:
    print(max_val.upper())
