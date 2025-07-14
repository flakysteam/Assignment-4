file1 = open('output.txt', 'w')
content = input('Enter text to write in the file: ')
print("data successfully written to file 'output.txt' ")
file1.write(content)
file1.close()

file2 = open('output.txt', 'a')
content = input('Enter text to append in the file: ')
file2.write(content)
file2.close()

file3 = open('output.txt', 'r')
print('Final content of file: \n' ,file3.read())