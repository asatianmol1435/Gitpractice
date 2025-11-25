file = open("test.txt")
print(file.read())
file.close()

file = open("test.txt")
print(file.read(7))
file.close()

file = open("test.txt")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("test.txt")
line = file.readline()
while line!="":
    print(line)
    line = file.readline()
file.close()

file = open("test.txt")
for line in file.readlines():
    print(line)
file.close()

with open('test.txt', 'r') as file:
    count = sum(1 for line in file)
    print(f'Total number of lines: {count}')


with open('test.txt', 'r') as file:
    content = file.read()
    print(content)