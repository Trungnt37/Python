formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing",
	"So I said goodnight."
)

'''
1. Ket qua dau ra cau lenh dong 7: tai sao cau thu 3 dung "", trong 
khi cac cau khac dung ''? ==> vi cau 3 co chua ' phia trong cau
2. Nen su dung %s hay %r
=> %s, chi nen su dung %r khi dubug, %r se hien thi dang tho.
'''