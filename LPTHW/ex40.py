# Modules, Classes, and Objects
'''
Python duoc goi la mot ngon ngu lap trinh huong doi tuong. Dieu do co nghia la,
co mot cau truc trong Python, duoc goi la "class", cho phep ban cau truc phan
mem mot cach dac biet. Su dung "classes", ban co the them tinh nhat quan cho 
chuong trinh cua ban de chung duoc su dung trong mot cach sach se hon, hoac it 
nhat do la ly thuyet.

Bay gio toi se co gang day cho ban nhung diem bat dau cua lap trinh huong doi
tuong, cac lop-classes, va cac doi tuong - objects, su dung nhung gi chung ta da
biet ve dictionaries va modules. Doi voi toi , lap trinh HDT chi don gian la mot
van de la. Ban co gang hieu nhung gi toi noi, go code va cac bai tap tiep theo 
toi se giai thich no.

========= Modules Are Like Dictionaries (Modules giong nhu dict) ===============
	Ban da biet mot dict duoc tao va su dung nhu the nao, va no la mot cach de
map 1 thu voi mot thu khac (key-values). Dieu do co nghia, neu ban co mot dict 
voi mot key la 'apple' va ban muon nhan duoc gia tri cho no, ban lam nhu sau:
	mystuff = {'apple': "I AM APPLES!"}
	>>> print mystaff['apple']

Giu y tuong "Lay X tu Y" trong dau ban, va bay gio nghi ve modules. Ban da thuc 
hien va su dung mot so chung, theo quy trinh sau:
	1. Ban biet mot module trong 1 file python voi mot so function hoac variables
	2. Sau do ban nap (import) vao file
	3. Sau do ban co the truy cap toi functions hoac variables trong module do,
	voi dau '.' (dot)

Hay tuong tuong, neu toi co mot module, ma toi dat ten la mystuff.py, va toi dat
mot ham goi la "apple" trong do. Day la module mystuff.py:
	# Doan code nay nam trong file mystuff.py
	def apple():
		print "I AM APPLES!"

Mot khi toi co module nay, toi co the su dung module voi import va su dung ham 
apple() trong do.
	import mystuff
	mystuff.apple()
Toi cung co the dat mot bien trong no voi ten la tangerine, nhu sau:
	# Doan code nay nam trong file mystuff.py
	def apple():
		print "I AM APPLES!"	
	
	tangerine = "Living reflection of a dream"
Sau do toi su dung no giong voi cach doi voi ham:
	import mystuff
	mystaff.apple()
	print mystaff.tangerine

Tham khao nguoc lai dictionary, va ban se bat dau thay no tuong tu nhu khi su 
dung dictionary, nhung cau truc la khac nhau. Hay so sanh:
	mystuff['apple'] 	# lay apple tu dictionary
	mystuff.apple()		# lay apple tu module
	mystuff.tangerine 	# giong nhu the, doi voi bien

Dieu do, chung ta co mot khuon mau rat pho bien trong Python:
	1. Dua vao key mot gia tri
	2. Lay cai gi do ra bang ten cua Keys.

Trong truong hop cua Dict, key la mot chuoi va cau truc la [key]. Trong truong 
hop module, key la mot dinh danh, va cau truc la .key. Khac biet cho do, con lai
chung gan nhu la tuong tu.

========= Classes Are Like Modules =============================================

Mot cach de hieu mot module la mot dict chuyen biet, co the luu tru ma Python,
de ban co the lay ra va su dung bang cach dung dau '.'
Python co mot cau truc khac phuc vu muc dich tuong tu, do la "class". Mot class
la mot cach de thuc hien mot nhom cac ham va du lieu, va dat chung vao mot vung 
de ban co the truy cap chung bang dau '.'

Neu toi tao ra mot class giong nhu module mystuff, toi se lam nhu sau:
	class MyStuff(object):
		def __init__(self):
			self.tangerine = "And now a thousand year between"
		def apple(self):
			print "I AM CLASSY APPLES!"

Dieu do phuc tap hon so voi modules, va chac chan co rat nhieu bang cach so sanh,
nhung ban co the lam ra cach nay giong nhu mot "mini-module" voi MyStuff co chua
ham apple() trong no. Dieu gi co the gay nham lan voi dieu nay la ham 
__init_self() va self.tangerine de thiet lap bien tangerine

Day la ly do tai sao cac class duoc su dung thay vi module. Ban co the lay class
tren va su dung no de tao ra nhieu craft trong so ho, hang trieu lan neu ban 
muon, va chung se khong can thiep lan nhau. Voi module, khi ban import se chi co
mot cho toan bo chuong trinh, tru khi ban lam mot so hack monster.

Truoc khi ban hieu thong suot duoc dieu nay, ban can phai biet "Object" la gi va
lam the nao de su dung MyStuff giong nhu ban lam voi module mystuff.py

========= Objects Are Like Mini-Import ========================================

Neu mot class giong nhu mot "mini-module", thi se phai co mot khai niem tuong tu
nhu import nhung dung cho classes. Khai niem do duoc goi la "instantiate", ma
chi rat dac biet, thong minh thi noi la "create". Khi ban instantiate mot class,
nhung gi ban nhan duoc goi la mot object. 

Cach ban lam dieu nay la ban goi class nhu no la mot ham, giong nhu the nay:
	thing = MyStuff()
	thing.apple()
	print thing.tangerine

Dong dau tien goi la hoat dong "instantiate", va no giong nhu goi ham. Tuy nhien
khi ban goi no, co mot chuoi su kien ma Python toa do cho ban. Toi se di qua
chung bang cach su dung ma tren cho MyStuff:
	1. Python tim MyStuff(), va thay no la mot class ma ban da dinh nghia
	2. Python crafts mot object trong voi tat ca cac functions ban dinh nghia
	trong class su dung def
	3. Sau do Python tim va thay neu ban tao mot ham dung __init__, va neu ban 
	co, no goi ham do de khoi tao object rong moi cua ban.
	4. Trong MyStuff, ham __init__ sau do toi them vao bien seft, do la Object 
	Python tao cho toi, va toi co the thiet lap cac bien tren no, giong nhu ban
	se co mot module, dict hoac mot Object khac.
	5. Trong truong hop nay, toi thiet lap seft.tangerine la loi mot bai hat va 
	sau do, toi da intialized Object nay.
	6. Bay gio, Python co the lay Object nay gan no vao bien cho toi lam viec voi
'''

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bulls_on_parede = Song(["They rally around the family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parede.sing_me_a_song()