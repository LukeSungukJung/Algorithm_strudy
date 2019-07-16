def distance(x,y,x2,y2):
    dis = (x-x2)**2+(y-y2)**2
    return dis**(1/2)

def terret(x1, y1, r1, x2, y2, r2):
    r1_r2 =r1+r2
    dis =  distance(x1, y1, x2, y2)
    if (r1==r2) and (x1==x2) and (y1==y2):
                return -1
    elif r1_r2==dis:
        return 1
    elif dis+r1 == r2 or dis +r2 ==r1:
        return 1
    elif r1_r2>dis:
        if dis+r1 < r2 or dis +r2 < r1:
            return 0
        return 2
    else:
        return 0
ilst = []
ss =  int(input())
for a in range(ss):
    ss_2 = input()
    ilst.append(ss_2)
    


for i in range(ss):
    ll = []
    [ll.append(float(j)) for j in ilst.pop(0).split(' ')] 
    x1=ll.pop(0)
    y1=ll.pop(0)
    r1=ll.pop(0)
    x2=ll.pop(0)
    y2=ll.pop(0)
    r2=ll.pop(0)
    print(terret(x1, y1, r1, x2, y2, r2))





