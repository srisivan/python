#This program is designed to print how much letters are there in input.
def histogram (s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

word = input()

h = histogram(word)

print(h)

