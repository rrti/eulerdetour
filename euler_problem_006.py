## The sum of the squares of the first ten natural numbers is
## 1^2 + 2^2 + ... + 10^2 = 385
##
## The square of the sum of the first ten natural numbers is
## (1 + 2 + ... + 10)^2 = 55^2 = 3025
##
## Hence the difference between the sum of the squares of the first
## ten natural numbers and the square of the sum is 3025 - 385 = 2640.
##
## Find the difference between the sum of the squares of the
## first one hundred natural numbers and the square of the sum.
##

## useful identities
##   sum{i=1,N} (i^1) = (N^2)/2 + (N^1)/2           == (1/2) * (N)*(N+1)
##   sum{i=1,N} (i^2) = (N^3)/3 + (N^2)/2 + (N^1)/6 == (1/6) * (N)*(N+1)*(2N+1)
##   sum{i=1,N} (i^3) = (N^4)/4 + (N^3)/2 + (N^2)/4 == (1/4) * ((N^2)+(N^2))
def find_sumsq_sqsum_diff(N):
	sumSq = 0
	sqSum = 0

	for i in xrange(1, N + 1):
		sumSq += (i * i)
		sqSum += i

	return ((sqSum * sqSum) - sumSq)

print("[euler006] D=%d" % find_sumsq_sqsum_diff(100))

