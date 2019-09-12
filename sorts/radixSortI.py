def radix_sort(arr):
	s = arr[:]
	for i in range(len(str(max(arr)))):
		b = [[] for x in range(10)]

		for n in s:
			str_n = str(n)
			try:
				d = int(str_n[-(i + 1)])
			except IndexError:
				d = 0
			b[d].append(n)
		s = []
		for n in b:
			s.extend(n)

	return s


unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

sorted_list = radix_sort(unsorted_list)
print(sorted_list)