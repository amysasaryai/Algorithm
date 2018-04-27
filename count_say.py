def countAndSay(n):
	alist = list()

	if n == 1:
		alist = [1]
	elif n == 2:
		alist = [1,1]
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
				alist.append(currentcount) 
				alist.append(countAndSay(n-1)[i-1])
				i=i+1

			if not flag:
				alist.append(currentcount) 
				alist.append(countAndSay(n-1)[i])
				i=i+1

			if i == len(countAndSay(n-1))-1:
				if countAndSay(n-1)[i] != countAndSay(n-1)[i-1]:
					alist.append(1)
					alist.append(countAndSay(n-1)[i])

	return alist

print countAndSay(8)







