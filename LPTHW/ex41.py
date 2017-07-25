# Learn to Speak Object Oriented
"""
Trong bai nay, chung ta se hoc "huong doi tuong". Toi se cung cap cho ban mot bo
tu vung voi dinh nghia can thiet. Sau do cung cap cho ban bo cau hoi voi nhung 
lo hong trong do ma ban phai hieu. Cuoi cung toi se cung cap mot bai tap lon ma 
ban phai hoan thanh de hieu ro cac thuat ngu cua ban.

class: Lop, Noi Python tao ra mot loai gi do moi
object—Two meanings: the most basic kind of thing, and any instance of some thing
Đối tượng-Hai ý nghĩa: điều cơ bản nhất của điều, và bất kỳ ví dụ của một số điều
instance: Thuc the, doi tuong cua mot class, nhung gi ban tao ra trong class
def: Cach ban dinh nghia mot ham trong mot class
self: Nam phia trong ham cua 1 class, self la 1 bien cho instance/object duoc phep
truy cap
inheritance - Tinh ke thua, mot lop co the ke thua cac dac diem tu mot lop khac
compositon - Mot lop co the bao gom cac lon khac
attribute: danh sach thuoc tinh co trong mot class, thuong la cac bien
is-a: Mot cum tu de noi rang cai gi do ke thua tu mot cai khac
has-a: Mot cum tu de noi rang mot cai gi do bao gom cac thu khac.

class X(Y): "Make a class named X that is-a Y" - Tao mot class ten la X ke thua Y
class X(object):
	def __init__(self, J): "class X has-a __init__ that takes self and J parameter"

class X(object):
	def M(self, J): "class X has-a function named M that takes self anh J parameter"

foo = X(): "Set foo to an instance of class X" - Thiet lap foo la 1 doi tuong
trong class X

foo.M(J) "From foo get the M function, and call it which parameters self, J"
foo.K = Q "From foo get the K attribute, and set it to Q"

"""