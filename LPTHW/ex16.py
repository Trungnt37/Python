# Reading and writing files
'''
Chung ta co the tuong tac voi file bang nhieu cach thuc.
close --> Dong file, giong nhu File -> save
read  --> Doc noi dung file. Ban co the gan ket qua vao 1 bien
readline --> Chi doc 1 dong trong file
truncate --> lam trong file. Dung khi ban k quan tam den noi dung cua file
write(stuff) --> Ghi noi dung vao file
'''

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# w: mo file voi che do write, a: append (them vao), r: read
# r: Che do mac dinh cua open, ban se khong the lam gi file dc, chi doc.
# a: them noi dung vao file text
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate() #Loi neu phia tren la open(filename, 'r')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()


