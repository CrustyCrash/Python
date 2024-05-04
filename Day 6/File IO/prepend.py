with (open('file.txt', 'r') as file):
    temp = file.readlines()
with (open('file.txt', 'w') as file):
    for line in temp:
        file.write("HPC-"+line)
