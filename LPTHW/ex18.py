# Names, variables, code, functions
'''
Trong python, ham dc bat dau bang tu khoa define: def
Sau do la ten ham. 
Tiep theo la doi so duoc dat trong dau ()
* - co nhieu doi so, ban co the khai bao giong nhu argv
sau do than ham duoc viet sau dau : va phai thut vao so voi tu khoa def
'''

# this one is like your scripts with argv: # cach nay it su dung
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one take no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()