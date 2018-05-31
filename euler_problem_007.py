## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
## What is the 10 001st prime number?
##
def gen_primes(N):
	R = int(N ** 0.5) + 1
	P = [True] * (1 + N)

	## note: P[N] also exists
	P[0] = False
	P[1] = False

	## filter even numbers
	for i in xrange(4, N + 1, 2):
		P[i] = False

	## basic prime sieve; O(sqrt(N) * N)
	for i in xrange(2, R + 1):
		j = 3

		while ((i * j) <= N):
			P[i * j] = False
			j += 2

	return P

def find_kth_prime(P, k):
	N = len(P)
	c = 0

	for i in xrange(2, N):
		c += P[i]

		if (c == k):
			return i

	## fewer than k primes present in the interval [0, N]
	return -1

assert(find_kth_prime(gen_primes(20), 1) ==  2)
assert(find_kth_prime(gen_primes(20), 6) == 13)
print("[euler007] P=%d" % find_kth_prime(gen_primes(105000), 10001))

