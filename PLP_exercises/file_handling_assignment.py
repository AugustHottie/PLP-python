#file creation
file = open("my_file.txt", 'w')
file.write("hello\n")
file.write("world\n")
file.write("2003\n")
file.close()

#read file and display
file = open("my_file.txt")
print(file.read())
file.close()

#file appending
file = open("my_file.txt", 'a')
file.write("I love Mehmet\n")
file.write("Mehmet loves Jessica\n")
file.write("3000")

#error handling 
try: 
    file = open("my_file.txt")
    print(file.read())
except: 
    FileNotFoundError
finally:
    file.close()