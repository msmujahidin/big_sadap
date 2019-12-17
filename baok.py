import re

with open(input("Tulis Nama File : ")) as f:
    mylist = [line.rstrip('\n') for line in f]
#     print(mylist[2])

y = re.compile(".*Net")
x  = re.compile(".*Bill")
z  = re.compile(".*Date")
a  = re.compile(".*Item")
b  = re.compile(".*Tax")
d  = re.compile(".*Disc")

# ih = re.split("\s", x)

newlist  = list(filter(x.match, mylist)) # Baca catetan
newlist3 = list(filter(z.match, mylist)) #tanggal
newlist4 = list(filter(a.match, mylist)) #Sub Total
newlist5 = list(filter(b.match, mylist))

newlist2 = list(filter(y.match, mylist))
newlist7 = list(filter(d.match, mylist))


dictionary = {}

for x in newlist:
    p = x.find('1')
    if p > 0 and x[p-1] == '-': p -= 1
    dictionary[x[0:p].strip()] = x[p:].split()
    
for z in newlist3:
    p = x.find('1')
    if p > 0 and x[p-1] == '-': p -= 1
    dictionary[x[0:p].strip()] = x[p:].split() 

for a in newlist4:
    p = x.find('1')
    if p > 0 and x[p-1] == '-': p -= 1
    dictionary[x[0:p].strip()] = x[p:].split() 

for b in newlist5:
    p = x.find('1')
    if p > 0 and x[p-1] == '-': p -= 1
    dictionary[x[0:p].strip()] = x[p:].split() 

for c in newlist2:
    p = x.find('1')
    if p > 0 and x[p-1] == '-': p -= 1
    dictionary[x[0:p].strip()] = x[p:].split() 

str = x
str1 = z
str2 = a
str3 = b
str4 = c

ih = re.split("\s", str)
ihh = re.split("\s", str1)
ihhh = re.split('\s', str2)
ihhhh = re.split('\s', str3)
ihhhhh = re.split('\s', str4)

b = [ih[3], ihh[3], ihhh[18], ihhhh[24], ihhhhh[19]]


finalString = ''.join(ih[3])
finalString2 = ''.join(ihh[3])
finalString3 = ''.join(ihhh[18])
finalString4 = ''.join(ihhhh[24])
finalString5 = ''.join(ihhhhh[19])
finalString6 = ''.join(b)

# print(finalString)
# print(finalString2)
# print(finalString3)
# print(finalString4)
# print(finalString5)

hasil = ""+finalString+";"+finalString2+";"+finalString3+";"+finalString4+";"+finalString5+""

data = input("Simpan File : ")
text_file = open(data, "w")
text_file.write(hasil)
text_file.close()
