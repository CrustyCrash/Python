with( open('file.txt', 'r')as file):
    temp = file.readlines()
with(open('new-prepend-file.txt','w')as file):
    for lines in temp:
        file.write(lines)