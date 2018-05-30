## Project Euler - Problem 3
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?
##
def max_prime_factor(N):
	d = 2

	while (N > 1):
		if ((N % d) == 0):
			N /= d
		else:
			d += 1

	return d

assert(max_prime_factor(13195) == 29)
print("[euler003] d=%d" % max_prime_factor(600851475143))

