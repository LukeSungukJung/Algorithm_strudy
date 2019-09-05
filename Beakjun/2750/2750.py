num = input()
input_list = []
for one in range(int(num)):
    input_list.append(int(input()))
input_list.sort()

for a in input_list:
    print(a)