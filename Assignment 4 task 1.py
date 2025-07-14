try:
    file1 = open('output.txt', 'r')
    Read = file1.read()
    print(Read)
    file1.close()
except FileNotFoundError:
    print("the file 'output.txt' was not found")

