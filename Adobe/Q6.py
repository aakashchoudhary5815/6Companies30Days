def AllParenthesis(self,n):
    #code here
    solutions = set()
    def helper(current, os, cs):
    	if os > cs:
    		return

    	if os == 0 == cs:
    		solutions.add(current)

    	if os:
    		helper(current + "(", os-1, cs)
    	if cs:
    		helper(current + ")", os, cs-1)

    helper("", n, n)
    return list(solutions)