# Reading files
'''
Trong bai nay, chung ta su dung 2 file.
ex15.py - la script nay
ex15_sample.txt - chua noi dung van ban.

Chung ta muon mo file ex15_sample.txt, va in noi dung cua chung ra ngoai. 
Nhung khong nen 'hard code', de ex15_sample.txt trong code cua chung ta, chung 
ta nen su dung argv va raw_input de hoi nguoi dung thay vi 'hard code'

'''

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()
