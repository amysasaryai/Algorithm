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
		k=start
		while i < mid+1 and j < end+1:
			if alist[i] < alist[j]:
				newlist[k]=alist[i]
				i=i+1
			else:
				newlist[k]=alist[j]
				j=j+1
			k=k+1

		while i < mid+1:
			newlist[k]=alist[i]
			i=i+1
			k=k+1

		while j < end+1:
			newlist[k]=alist[j]
			j=j+1
			k=k+1

	for o in range(0, len(newlist)-1):
		alist[o] = newlist[o]

	print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist, 0, len(alist)-1)
print(alist)





