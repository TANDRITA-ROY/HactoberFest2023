from typing import Dict, Tuple

# Initialize an empty dictionary to store the solutions of subproblems
dp: Dict[Tuple[str, str], str] = {}

# Initialize an empty dictionary to keep track of visited subproblems
vs: Dict[Tuple[str, str], int] = {}

# Utility function to reverse a string, we need it because our top-down approach
# return a reversed solution
def reverse(s: str) -> str:
	ans = list(s)
	u, v = 0, len(ans) - 1
	while u < v:
		ans[u], ans[v] = ans[v], ans[u] #swap operation
		u += 1
		v -= 1
	return "".join(ans)

# Utility function that compares two strings and return the longer in size.
def max_str(a: str, b: str) -> str:
	return a if len(a) > len(b) else b

# Recursive function that takes two strings as input, and returns the LCS of them
def LCS_core(a: str, b: str) -> str:
	# Base case
	if not a or not b:
		return ""
	# dp index to access the dp structure
	dp_i = (a, b)

	# if visited return solution from memory
	if dp_i in vs:
		return dp[dp_i]
	else:
		vs[dp_i] = 1

	# if the last two character match
	if a[-1] == b[-1]:
		ans = a[-1] + LCS_core(a[:-1], b[:-1])
		dp[dp_i] = ans
		return ans

	# Return longest string
	ans = max_str(LCS_core(a[:-1], b), LCS_core(a, b[:-1]))
	dp[dp_i] = ans
	return ans

# Final wrapper function to call the recursive function and reverse the result
def LCS(a: str, b: str) -> str:
	return reverse(LCS_core(a, b))

a = "AGGTAB"
b = "GXTXAYB"
print(LCS(a, b))

# This code is contributed by Shivam Tiwari
