# Second commit
newDict = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
newDict2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

for i in newDict2:
    if i in newDict:
        newDict2[i] = newDict2[i] + newDict[i]
    else:
        pass
print(newDict2)


#Sources used: https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/