# a = list(map(int, input('Please input  integers, some being the same, or not if you prefer: ').split()))
# Failed code. Indented incase its of SOME use...
#res = []
#for i in a:
 #   if i not in res:
 #       res.append(i)
#print(a)

def newList(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
print("Enter some integers please:")
b = input()
magicList = newList(b)
print(magicList)



#Sources used: https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
#