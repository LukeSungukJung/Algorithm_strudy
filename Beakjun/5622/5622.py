dict_dick ={
        '2':['A','B','C'],
        '3':['D','E','F'],
        '4':['G','H','I'],
        '5':['J','K','L'],
        '6':['M','N','O'],
        '7':['P','Q','R','S'],
        '8':['T','U','V'],
        '9':['W','X','Y','Z'],
        }


str_s = input()
dial_list = []
for list_ in dict_dick:
    for ele in dict_dick[list_]:
        for s in str_s:
            if s==ele:
                dial_list.append(int(list_)+1)

total = 0
for i in dial_list:
    total+=i

print(total)
