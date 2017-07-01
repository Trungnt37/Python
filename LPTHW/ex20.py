# Functions and files.
from sys import argv

script, input_file = argv

# Ham print_all chuc nang doc noi dung file la doi so dau vao cua ham
def print_all(f):
	print f.read()

# Ham rewind dua vi tri con tro ve dau trong file.
# seek(offset, [whence == 0]): offset: vi tri cua con tro, 
# whence = {0,1,2} = {vitri dung theo gtri tuyet doi, vitri theo vitri htai cua
# file, vitri theo vitri cuoi cua file}
def rewind(f):
	f.seek(0)

# Ham print_a_line doc 1 dong cua file va dua vitri con tro ve dau dong tiep 
# theo.
# Ham readline(size) doc 1 dong cua file, bao gom 1 kitu newline.
# Doi so size neu co mat va khong am, thi size chinh la so byte dc doc, bao gom
# ca kitu newline.
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

'''
Vi readline() co bao gom mot ki tu \n phia sau, de tat cac khoang trong trong
dau ra, them "," o print, giong nhu vay: print line_count, f.readline(),

Chu y: current_line tang theo thu cong, do chung ta tu tang cho.
Ben trong ham readline() ma la quet tung bye cua file cho den khi no gap \n
sau do, no dung doc va tra ve nhung gi no tim thay. 
Tep tin f co trach nhiem duy tri vitri con tro hien tai trong tep tin.
readline() tiep tuc doc tu vitri moi nay.
'''