#understanding how to read and write files

#"r"=read only

file=open("first.py","r")

#read the file content

content=file.read()

print(content)

file.close()

#"w"=write only
file=open("first.py","w")

#write some text in the file
file.write("Helo, word!\n")
file.write("This is a test.\n")

file.close()
#"a"=Append only
#"x"=write only,exclusive creation
#tell and seek

"""Reading Keyboard Input

Python provides two built-in functions to 
read a line of text from standard input, which
by default comes from the keyboard.
 These functions are −

raw_input
input
The raw_input Function

The raw_input([prompt]) function 

reads one line from standard input and returns 
it as a string (removing the trailing newline).

Flat Files vs. Non-Flat Files
Flat files are data files that contain records with no structured relationships between the records, and there's also no structure for indexing like you typically find it in relational databases. These files can contain only basic formatting, have a small fixed number of fields, and can or can not have a file format.




"""