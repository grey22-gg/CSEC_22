n = input()
p = 0
j = 'a'
for i in n:
	n =abs(ord(i) - ord(j))
	p += min(n, 26 - n)
	j = i
print(p)
