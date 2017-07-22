# Nhap vao mot chuoi va in ra man hinh. Cho biet chuoi do co phai la palindrome
# hay khong? Chuoi palindrome la chuoi doi xung: vd: "abcba"

# My solution
print "===================="
s = raw_input("Enter a string: ")
s2 = []
for i in range(len(s)-1, -1, -1):
	s2.append(s[i])
s3 = ''.join(s2)

print "The contra string: %s" %s3

if s == s3:
	print "So, %s is a palindrome string" %s
else:
	print "So, %s isn't a palindrome string" %s

# Sulution
print "\n===================="
wrd = raw_input("Please enter a word: ")
wrd = str(wrd)
rvs = wrd[::-1]
print "The contra string:", rvs
if wrd == rvs:
    print "So, %s is a palindrome string" %wrd
else:
    print "So, %s isn't a palindrome string" %wrd