string="Python is a case sensitive language"

#a
print(len(string))
#b
rev=string[::-1]
print(rev)
#c
print(string[slice(10,26)])
 #vs print(string[10:26])

#d
print(string.replace("a case sensitive", "object oriented"))

#e
index=string.find('a')
print(index)

#f
print(string.replace(' ', ''))

