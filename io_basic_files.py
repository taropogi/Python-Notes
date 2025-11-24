# create and write myfile.txt
with open('myfile.txt','w') as file: # w means mode is write
    file.write("xxxxxxxxxxx, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")
    file.write("And this is the fourth line.\n")

print("File 'myfile.txt' has been created successfully!")

the_file = 'myfile.txt'
with open(the_file, 'r') as file:
    content = file.read()
    print("File Content:\n", content)

#readlines
# readlines() method returns a list containing each line in the file as a list item.
with open(the_file, 'r') as file: # r means mode is read
    lines = file.readlines()
    print("File Lines:")
    for line in lines:
        print(line.strip())

       # closing a file
       # When you use the with statement to open a file, it automatically takes care of closing the file for you when the block of code is exited, even if an error occurs within the block.

#append mode
with open(the_file, 'a') as file: # a means mode is append
    file.write("This line is appended to the file.\n")
    print(f"Line appended to '{the_file}' successfully!")
        