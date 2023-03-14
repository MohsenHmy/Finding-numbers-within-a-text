import re
handle = open("Actualtxt.txt")
numList = list()
for line in handle:
    stuff = re.findall('[0-9]+', line)
    numList = numList + stuff

num = list()
for z in numList:
    num.append(int(z))


print(sum(num))



