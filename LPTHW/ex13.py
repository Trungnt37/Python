# Parameters, Unpacking, Variables
'''
Trong cac bai truoc, de thuc thi 1 doan script python, chung ta chay:
python ex1.py
Vay ex1.py do chinh la 1 doi so
Trong bai nay chung ta se chi ra nhieu doi so, cac doi so nhap vao dc su dung
trong script
'''

from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

'''
Dong dau tien cua ctrinh la "import". Them cac tinh nang vao script cua ban
==> Them tinh nang argv tu module sys.

Dong tiep theo: Giai nen argv: Hay giai nen agrv, gan cho tat cac cac bien nay
o ben trai theo thu tu.
Thay vi chung ta de 4 bien, chung ta nen no vao argv. 
Thuc thi: python ex13.py 1st 2nd 3rd
Neu chung ta nhap thieu hoac thua doi so, ==> erro
'''