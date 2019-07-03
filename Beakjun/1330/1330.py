inputs =input()
inputs = inputs.split(' ')

a =int(inputs[0])
b =int(inputs[1])

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")
