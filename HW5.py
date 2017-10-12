import re

file_object = open("ActualData.txt","r").read()

y = re.findall('[0-9]+', file_object)
print(len(y))
total = 0

for x in y:

	total += int(x)

print(total)

#comment 

