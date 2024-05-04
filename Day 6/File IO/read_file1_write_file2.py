with(open('user_input.txt', 'r') as file1):
    with (open('file.txt', 'a') as file2):
        for line in file1:
            file2.write(line )
