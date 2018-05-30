## Project Euler - Problem 5
##
## 2520 is the smallest number that can be divided by each
## of the numbers from 1 to 10 without any remainder value.
##
## What is the smallest positive number that is evenly
## divisible by all of the numbers from 1 to 20?
##

##
## notes:
##   given (example) number
##     2520 /  2 = 1260
##     2520 /  3 =  840
##     2520 /  4 =  630
##     2520 /  5 =  504
##     2520 /  6 =  420
##     2520 /  7 =  360
##     2520 /  8 =  315
##     2520 /  9 =  280
##     2520 / 10 =  252
##
##   a multiple of 20 is also a multiple of 2, 4, 5, 10
##   a multiple of 18 is also a multiple of 2, 3, 9
##   a multiple of 16 is also a multiple of 2, 4, 8
##   a multiple of 15 is also a multiple of 3, 5
##   a multiple of 14 is also a multiple of 2, 7
##   a multiple of 12 is also a multiple of 2, 3, 4, 6
##   a multiple of 10 is also a multiple of 2, 5
##   a multiple of  9 is also a multiple of 3
##   a multiple of  8 is also a multiple of 2, 4
##   a multiple of  6 is also a multiple of 2, 3
##   a multiple of  4 is also a multiple of 2
##
## the LHS terms are non-prime and cover all the divisors contained
## within them (eg. 20 covers 2, 4, 5, 10 whereas 18 covers 2, 3, 9
## etc, and we want the smallest product covering the whole set from
## 1 to 20)
##
## "evenly divisible" simply means "without remainder"
##
def min_evenly_divisible_num(A):
	N = 1

	## start with K!
	for k in xrange(2, A + 1):
		N *= k

	## if N divided by k is still a multiple of k,
	## remove it (but only if all *other* factors
	## are unaffected, e.g. if N=800 then after we
	## divide by 20 it is no longer a multiple of
	## 25)
	## run-time is O(K^2), excluding mults for K!
	for k in xrange(A, 1, -1):
		n = N / k
		z = 0

		if ((n % k) != 0):
			continue

		## xrange(2, K + 1) is not necessary here: if
		## N / k is still a multiple of k, it is also
		## still a multiple of all factors of k
		for j in xrange(k + 1, A + 1):
			## if (j == k): continue
			z += ((n % j) != 0)

		if (z == 0):
			N /= k

	return N

assert(min_evenly_divisible_num(10) ==      2520)
assert(min_evenly_divisible_num(20) == 232792560)
print("[euler005] N=%d" % min_evenly_divisible_num(20))

