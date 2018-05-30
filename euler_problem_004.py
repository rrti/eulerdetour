## Project Euler - Problem 4
##
## A palindromic number reads the same both ways. The
## largest palindrome made from the product of two 2-
## digit numbers is 9009 = 91 * 99.
##
## Find the largest palindrome made from the product
## of two 3-digit numbers.
##
def find_max_palindrome(d):
	N = 0
	P = [(10 ** (d * 2 - i - 1)) for i in xrange(d * 2)]
	D = [0] * (d * 2)

	## do not need to search the entire d-digit range
	N_MIN = int((10 ** d) - (10 ** (d - 1)))
	N_MAX = int( 10 ** d)

	for n0 in xrange(N_MAX - 1, N_MIN, -1):
		## skip a*b == b*a, saves a factor of two
		## for n1 in xrange(N_MAX - 1, N_MIN, -1):
		for n1 in xrange(n0, N_MIN, -1):
			r = n0 * n1
			k = 0

			## split the (d*2)-digit product into digits
			for i in xrange(d * 2):
				D[i] = (r < P[i] and -1) or ((r / P[i]) % 10)

			## check palindrome-condition; true if k == 0
			for i in xrange(d * 2 - 1):
				k += (D[i] != -1 and ((D[i] % 10) != (D[-i - 1] % 10)))

			## keep maximum palindrome value
			N = max(N, r * (k == 0))

	return N

assert(find_max_palindrome(2) ==   9009)
assert(find_max_palindrome(3) == 906609)
print("[euler004] n=%d" % find_max_palindrome(3))

