# More files
# Chung ta se lam viec voi nhieu files, trong bai nay, thuc hien copy noi
# dung file nay sang file khac.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
# Ban co the ghep 2 lenh tren bang: indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'a')
out_file.write("\n")
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# python ex17.py ex17_from.txt ex17_to.txt
