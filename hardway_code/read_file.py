from sys import argv
#unpacking
script, filename = argv
#opening and assigning the file name to txt
txt = open(filename)

print(f"Here is your file {filename}")
#using the read function on txt object
print(txt.read())

print("Type the file name again")

file_again = input(">")
#re-doing the opening of the file
txt_again = open(file_again)
#reading the file again
print(txt_again.read())
txt.close()
txt_again.close()