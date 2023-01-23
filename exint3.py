print('Input some random string: \n')
testString = input()

newFreq = {}
for i in testString:
    if i in newFreq:
        newFreq[i] += 1
    else:
        newFreq[i] = 1
print(str(newFreq))

#sources used https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
