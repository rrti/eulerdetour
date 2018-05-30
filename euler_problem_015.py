## Project Euler - Problem 15
##
## Starting in the top left corner of a 2*2 grid, there are 6 routes
## (without backtracking) to the bottom right corner (along the '+'
## vertices).
##
##   +--+--+
##   |  |  |
##   +--+--+
##   |  |  |
##   +--+--+
##
## How many routes are there through a 20*20 grid?
##

## notes:
##   any permutation of the sequence {E^X S^Y} will do (E=East, S=South)
##   however this yields 4*3*2=24 routes in a 2x2 grid instead of just 6
##   need to filter out the permutations that do not produce new routes
##   (eg. E1E2S1S2 == E2E1S1S2) meaning we are only interested in those
##   interchanging different letters
##
##   all valid routes have a length of X+Y with <X> E's and <Y> S's
##   if choosing <X> E's, then all <Y> S's are fixed and vice versa
##   problem reduces to choosing X (or Y) out of (X + Y) directions,
##   i.e. choose(2N N) if grid is square (X=Y)
##
##     1x1 grid; 2 routes
##       E S
##       S E
##     2x1 grid; 3 routes
##       E E S
##       E S E
##       S E E
##     2x2 grid; 6 routes
##       E E S S
##       E S E S
##       E S S E
##
##       S E E S
##       S E S E
##       S S E E
##     3x1 grid; 4 routes
##       E E E S
##       E E S E
##       E S E E
##       S E E E
##     3x2 grid; 10 routes
##       E E E S S
##       S S E E E
##
##       E E S E S
##       E E S S E
##
##       E S E E S
##       E S E S E
##       E S S E E
##
##       S E E E S
##       S E E S E
##       S E S E E
##     3x3 grid; 20 routes
##       E E E S S S
##       S S S E E E
##
##       E E S S S E
##       E E S S E S
##       E E S E S S
##
##       S S E E E S
##       S S E E S E
##       S S E S E E
##
##       E S S S E E
##       E S S E E S
##       E S S E S E
##       E S E S E S
##       E S E E S S
##       E S E S S E
##
##       S E E E S S
##       S E E S S E
##       S E S E S E
##       S E S E E S
##       S E S S E E
##       S E E S E S
##

## recursive solution, useless without memoization
def count_routes_rec(X, Y, T = {}):
	if ((X, Y) in T):
		return T[(X, Y)]

	if (X == 0 and Y == 0):
		return 1

	N = 0

	if (X > 0): N += count_routes_rec(X - 1, Y    , T)
	if (Y > 0): N += count_routes_rec(X    , Y - 1, T)

	T[(X, Y)] = N
	return N

def count_routes_dp(X, Y):
	grid = [0] * ((X + 1) * (Y + 1))

	## initialise bottom-most row and right-most colum
	for i in xrange(X):
		grid[Y * X + i] = 1
	for j in xrange(Y):
		grid[j * X + X] = 1

	## work from bottom-right corner back to top-left
	for j in xrange(Y - 1, 0, -1):
		for i in xrange(X - 1, 0, -1):
			grid[j * X + i] = grid[j * X + (i + 1)] + grid[(j + 1) * X + i]

	return (sum(grid) + 1)

## analytical combinatoric solution
def count_routes_square(X):
	N = 1

	## choose(n k) = (n*(n-1)*n(-2)*...*(n-k+1)) / (k*(k-1)*(k-2)*...*1) = PRODUCT[i=1,k] (n-k+i)/i
	for i in xrange(X):
		N *= ((2 * X) - i)
		N /= (i + 1)

	return N


assert(count_routes_rec(2, 1) ==  3)
assert(count_routes_rec(3, 1) ==  4)
assert(count_routes_rec(3, 2) == 10)

assert(count_routes_square( 1) ==            2)
assert(count_routes_square( 2) ==            6)
assert(count_routes_square( 3) ==           20)
assert(count_routes_square(20) == 137846528820)

assert(count_routes_dp( 1,  1) == count_routes_rec( 1,  1))
assert(count_routes_dp( 2,  2) == count_routes_rec( 2,  2))
assert(count_routes_dp( 3,  3) == count_routes_rec( 3,  3))
assert(count_routes_dp(20, 20) == count_routes_rec(20, 20))

print("[euler015] C=%d" % count_routes_square(20))

