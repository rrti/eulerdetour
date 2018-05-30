## Project Euler - Problem 14
##
## The following iterative sequence is defined for the set of positive integers:
##
## n -> n/2 (if n is even)
## n -> 3n + 1 (if n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
## 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
##
## It can be seen that this sequence (starting at 13 and finishing at 1) contains
## 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
## that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?
##
## NOTE: Once the chain starts the terms are allowed to go above one million.

## recursive memoized version
def collatz_r(n, s = 1, t = {}):
	if (n <= 1):
		return 1
	if (n in t):
		return t[n]

	r = 0

	if ((n & 1) == 0):
		r = (collatz_r(n >> 1, s, t) + 1)
	else:
		## skip a step since 3n+1 will be even
		## t[n] = (collatz_r(n * 3 + 1, t) + 1)
		r = (collatz_r((n * 3 + 1) >> s, s, t) + (1 + s))

	t[n] = r
	return r

## iterative memoized version
def collatz_i(n, s = 1, t = {}):
	i = 1
	c = [(n, i)]

	while (n != 1):
		if (n in t):
			return t[n]

		if ((n & 1) == 0):
			n >>= 1
			i += 1
			c += [(n, i)]
		else:
			n = (n * 3 + 1) >> s
			i += (1 + s)
			c += [(n, i)]

	for k in xrange(len(c)):
		v = c[k][0]
		t[v] = (len(c) - k) + 1

	return i


"""
ti = {}; tr = {}; print(collatz_i( 5, 0, ti), collatz_r( 5, 0, tr))
ti = {}; tr = {}; print(collatz_i( 5, 0, ti), collatz_r( 5, 0, tr))
print()
ti = {}; tr = {}; print(collatz_i(13, 0, ti), collatz_r(13, 0, tr))
ti = {}; tr = {}; print(collatz_i(13, 0, ti), collatz_r(13, 0, tr))
print()
ti = {}; tr = {}; print(collatz_i(525, 0, ti), collatz_r(525, 0, tr))
ti = {}; tr = {}; print(collatz_i(525, 0, ti), collatz_r(525, 0, tr))
print()
"""


## for n in [8932475984765890982437508035678947560456904756084356084356985690840568054609576, 11 ** 111, 23 ** 456]:
for n in [5, 13, 21, 525, 837799, 328738568497897575]:
	print("collatz(%d)=%d :: %d" % (n, collatz_i(n, 0, {}), collatz_r(n, 0, {})))
	assert(collatz_i(n, 0, {}) == collatz_r(n, 0, {}))


def max_chain_collatz(N):
	t = {}
	j = 0
	m = 0

	for n in xrange(1, N):
		i = collatz_r(N - n, 0, t)

		if (i > m):
			j = n
			m = i

	return (j, m)

print("[euler014] (n,l)=(%d,%d)" % max_chain_collatz(1000 * 1000))

