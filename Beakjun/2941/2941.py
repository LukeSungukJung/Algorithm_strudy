croatia = {'c=':2,'c-':2,'dz=':3,'d-':2,'lj':2,'nj':2,'s=':2,'z=':2}

ss = input()

str_count = 0

origin_len = len(ss)

stack= []
cnt_stack =[]

for cr in croatia:
    if ss.find(cr)!=-1:
        cnt_stack.append(ss.count(cr))
        origin_len -= ss.count(cr)
        stack.append(cr)
for stk in stack:
    sl = ss.split(stk)
    cnk = cnt_stack.pop(0)
    str_count+=1
    ss=''
    for ll in sl:
        ss+=ll



print(origin_len)
