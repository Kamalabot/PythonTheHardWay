from sys import argv

script, filename = argv

print(f"We are going to erase the {filename}")
print("Don't wanna erase, then hit Ctrl-C (^c)")
print("If you want to erase, then Return")

input('?')

print("Opening the file...")
# opening with write feature
target = open(filename,'w')

print("Truncating the file, Good day...")
target.truncate()

print("Now I want you to give me three sentences")

sen1 = input('line1')
sen2 = input('line2')
sen3 = input('line3')

print("I am going to write them to the same file")

target.write(sen1)
target.write('\n')
target.write(sen2)
target.write('\n')
target.write(sen3)
target.write('\n')

print("Write completed")
target.close()