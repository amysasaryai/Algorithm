notebook = dict()
notebook[0,0] = 0
notebook[0,1] = 1
notebook[1,0] = 1

def minDistance(word1, word2):
	m = len(word1)
	n = len(word2)
	if m > 0 and n > 0:
		if (m, n) in notebook.keys():
			return notebook[m, n]
		elif word1[m-1] == word2[n-1]:
			notebook[m, n] = minDistance(word1[:m-1], word2[:n-1])
			return notebook[m, n]
		else:
			notebook[m, n] = min(minDistance(word1[:m-1], word2[:n-1]), minDistance(word1[:m-1], word2[:n]), minDistance(word1[: m], word2[:n-1])) + 1
			return notebook[m, n]

	elif m == 0 and (m, n) not in notebook.keys():
		notebook[m, n] = n
		return notebook[m, n]

	elif n == 0 and (m, n) not in notebook.keys():
		notebook[m, n] = m
		return notebook[m, n]

	else:
		return notebook[m, n]


print minDistance("horse", "ros")
