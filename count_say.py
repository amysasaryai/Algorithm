
def countAndSay(n):
	
	if n == 1:
		astring = "1"
	elif n == 2:
		astring = "11"
	else:
		i = 1
		while i < len(countAndSay(n-1)):
			count = 1
			flag = False

			while i < len(countAndSay(n-1)) and countAndSay(n-1)[i-1] == countAndSay(n-1)[i]:
					count = count + 1
					flag = True
					i = i+1
			
			if flag:
				astring = astring + str(count) + str(countAndSay(n-1)[i-2])
				i = i + 1

			if not flag:
				astring = astring + str(count) + str(countAndSay(n-1)[i-1])
				i = i + 1

	return astring

print countAndSay(4)







