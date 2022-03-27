from sys import argv 
from os.path import exists

script, in_file, out_file = argv

print(f"Copying file from {in_file} to {out_file}")

from_file = open(in_file)
from_data = from_file.read()

print(f"The input file is {len(from_data)} bytes long")

print(f"Does the output file exist?{exists(out_file)}")

print("Ready, hit return to continue, Ctrl-C to abort")

input('?')

to_file = open(out_file,'w')
to_file.write(from_data)

print("Done")

to_file.close()
from_file.close()