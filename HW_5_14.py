#Implement the mergeSort function without using the slice operator.

def mergeSort(alist, start, end, scratch):
	print("Splitting ",start, end)
	if(end - start <= 1):
		return

	mid = (start + end) / 2
	mergeSort(alist, start, mid, scratch)
	mergeSort(alist, mid, end, scratch)

	i=start
	j=mid
	k=start
	while i < mid and j < end:
		if alist[i] < alist[j]:
			scratch[k]=alist[i]
			i=i+1
		else:
			scratch[k]=alist[j]
			j=j+1
		k=k+1

	while i < mid:
		scratch[k]=alist[i]
		i=i+1
		k=k+1

	while j < end:
		scratch[j]=alist[j]
		j=j+1
		k=k+1

	for o in range(start, end):
		alist[o] = scratch[o]

	print("Merging ",scratch)

alist = [54,26,93,17,77,31,44,55,20]
scratch = [0] * len(alist)
mergeSort(alist, 0, len(alist), scratch)
print(alist)





