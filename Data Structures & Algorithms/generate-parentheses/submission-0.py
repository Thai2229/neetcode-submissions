class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #choice: you are allowed to place n "("
        #at each step, you either choose to place "("
        #or a previous one using ")" -> n - total placed
        #need to track both open and closed strings
        res = []

        def dfs(open_p, closed_p, curr_string):
            #stop when length of curr_string is len(n)
            if len(curr_string) == n * 2:
                res.append(curr_string)
                return 
            
            #two choices, either place an open or closed parenthesis
            #when can you place an open string? when open_p < n
            #when can you place a close string? when closed_p < open_p
            if open_p < n:
                open_string = curr_string + "("
                dfs(open_p+1, closed_p, open_string)

            if closed_p < open_p:
                closed_string = curr_string + ")"
                dfs(open_p, closed_p+1, closed_string)
        
        dfs(0,0,"")
        return res