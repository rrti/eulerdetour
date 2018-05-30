## If we list all the natural numbers below 10 that are multiples
## of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
## 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.
##

def find_multiples_sum(N):
	S = 0

	a = 1
	b = 1

	for n in xrange(1, N):
		mod3 = (a == 3)
		mod5 = (b == 5)

		a *= (1 - mod3)
		b *= (1 - mod5)
		a += 1
		b += 1

		## do not double-count multiples of both 3 and 5
		S += (n * mod3             )
		S += (n * mod5 * (1 - mod3))

	assert((N == 10 and S == 23) or (N == 1000 and S == 233168))
	return S

print("[euler001] S=%d" % find_multiples_sum(1000))

