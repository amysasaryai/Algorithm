#Implement the binary search using recursion without the slice operator. 
#Recall that you will need to pass the list along with the starting and 
#ending index values for the sublist. Generate a random, ordered list of integers 
#and do a benchmark analysis.


def binarySearch(alist, item, first, last):
	if last < 0:
		return False
	elif first == last:
		if alist[first] == item:
			return True
		else: return False
	elif first < last:
		midpoint = (first+last)//2
		if alist[midpoint]==item:
			return True
		elif alist[midpoint] > item:
			last = midpoint-1
			print ("first=", first)
			print ("last=", last)
			return binarySearch(alist, item, first, last)
		elif alist[midpoint] < item:
			first = midpoint+1
			print ("first=", first)
			print ("last=", last)
			return binarySearch(alist, item, first, last)
		else:
			return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print binarySearch(testlist, 3, 0, len(testlist)-1)
print binarySearch(testlist, 19, 0, len(testlist)-1)




