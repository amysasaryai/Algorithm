def countAndSay(n):
	astring = ""

	if n == 1:
		astring = astring + "1"
	elif n == 2:
		astring = astring + "11"
	else:
		i = 0
		while i < len(countAndSay(n-1))-1:
			flag = False
			currentcount = 1
			while i < (len(countAndSay(n-1))-1) and countAndSay(n-1)[i] == countAndSay(n-1)[i+1]:
				currentcount = currentcount + 1
				i = i+1
				flag = True
				
			if flag:
				astring = astring + str(currentcount) 
				astring = astring + str(countAndSay(n-1)[i-1])
				i=i+1

			if not flag:
				astring = astring + str(currentcount) 
				astring = astring + str(countAndSay(n-1)[i])
				i=i+1

			if i == len(countAndSay(n-1))-1:
				if countAndSay(n-1)[i] != countAndSay(n-1)[i-1]:
					astring = astring + "1"
					astring = astring + str(countAndSay(n-1)[i])

	return astring

print countAndSay(7)







