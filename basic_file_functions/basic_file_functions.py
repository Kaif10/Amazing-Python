#Basic file functions in Python

# Open a file before performing operatopns
file_ = open('sample_file.txt')

#reads a line
print(file_.readline())
#reads the next line and so on
print(file_.readline())

#reads the second line
print(file_.readline(2))



#Write or Overwrite

#write function will write the content in an empty  file or overwwrite if the file already had some content in it.
file = open('sample_file.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# append

#write function will write the content in an empty  file or overwwrite if the file already had some content in it.
file_2 = open('sample_file.txt','a')
file_2.write("This will add this line")
file_2.close()



#Doing with the help of with statement
# Writing to file
with open("sample_file.txt", "w") as file1:

    file1.write("Hello, How's life going? \n")


# Appending to file
with open("sample_file.txt", 'a') as file2:
    file2.write("This will add this line. Today")

#Split line function
with open("sample_file.txt", "r") as file3:
    data = file3.readlines()
    for line in data:
        word = line.split()
        print (word)

