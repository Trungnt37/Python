# Doing Things to List

ten_things = "Apples Oranges Crows Telepphone Light Sugeer"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %s item now" %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # in ra phan tu cuoi cung cua list
print stuff.pop() # sau lenh nay, stuff chi con 9 phan tu dau
print stuff
print ' '.join(stuff) # in noi cac phan tu cua stuff va khoang trang " " o giua
print '#'.join(stuff[3:5]) # = print stuff[3], "#", stuff[4]

'''
Phuong thuc .pop se xoa phan tu cuoi cung cua list, va in ra phan tu do
vd: list = ["a", "b", "c", "d", "e"]
list.pop() = "e" khi do list = ["a", "b", "c", "d"]
list.pop(2) = "c" (2 chi muc cua list), khi nay, list = ["a", "b", "d"]

'''