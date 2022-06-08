import random
import operator
import time

def bubble_sort(a):

	for i in range(N-1):
		for j in range(N-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a
	
def merge_sort(a, compare=operator.lt):
	
	def merge(l, r, compare):
		result = []
		i, j = 0, 0
		while i < len(l) and j < len(r):
			if compare(l[i], r[j]):
				result.append(l[i])
				i += 1
			else:
				result.append(r[j])
				j += 1
		while i < len(l):
			result.append(l[i])
			i += 1
		while j < len(r):
			result.append(r[j])
			j += 1
		return result
		
	if len(a) < 2:
		return a[:]
	else:
		m = len(a)//2
		l = merge_sort(a[:m], compare)
		r = merge_sort(a[m:], compare)
		
		return merge(l, r, compare)
	
def quick_sort(a):

	if len(a) <= 1:
		return a
	else:
		q = random.choice(a)
		
	l_a = [n for n in a if n < q]
 
	e_a = [q] * a.count(q)
	b_a = [n for n in a if n > q]
	return quick_sort(l_a) + e_a + quick_sort(b_a)
	
if __name__ == '__main__':
	N = 100
	a = []
	for i in range(N):
		a.append(random.randint(-100, 100)/random.randint(1, 100))
	
	start_time = time.time()
	print(bubble_sort(a))
	print(time.time() - start_time)
	
	start_time = time.time()
	print(merge_sort(a))
	print(time.time() - start_time)
	
	start_time = time.time()
	print(quick_sort(a))
	print(time.time() - start_time)