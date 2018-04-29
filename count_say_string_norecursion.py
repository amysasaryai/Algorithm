def countAndSay(n):
	astring = ""
	previous = ""
	if n == 1:
		astring = astring + "1"

	elif n == 2:
		astring = astring + "11"

	else:
		previous = "11"
		for j in range(3, n+1):
			i=0
			astring = ""
			while i < len(previous)-1:
				flag = False
				count = 1
			
				while i < (len(previous)-1) and previous[i] == previous[i+1]:
					count = count + 1
					i = i + 1
					flag = True
				
				if flag:
					astring = astring + str(count) 
					astring = astring + str(previous[i-1])
					i=i+1

				if not flag:
					astring = astring + str(count) 
					astring = astring + str(previous[i])
					i=i+1

				if i == len(previous)-1:
					if previous[i] != previous[i-1]:
						astring = astring + "1"
						astring = astring + str(previous[i])

			previous = astring	

	return astring

for o in range(1, 15):
	print countAndSay(o)







