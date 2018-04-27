#Implement the mergeSort function without using the slice operator.

def mergeSort(alist, start, end):
	print("Splitting ",alist)
	newlist = list()
	if end > start:
		mid = (start + end)//2
		mergeSort(alist, start, mid)
		mergeSort(alist, mid+1, end)

		i=start
		j=mid+1

		while i < mid+1 and j < end+1:
			if alist[i] < alist[j]:
				newlist.append(alist[i])
				i=i+1
			else:
				newlist.append(alist[j])
				j=j+1

		while i < mid+1:
			newlist.append(alist[i])
			i=i+1

		while j < end+1:
			newlist.append(alist[j])
			j=j+1
	p=0
	for o in range(start, end):
		alist[o] = newlist[p]
		p=p+1

	print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist, 0, len(alist)-1)
print(alist)





