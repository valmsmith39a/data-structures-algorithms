class Solution(object):
    def isMatch self, sad, patterns):
        dp=[[False] * (len(patterns) + 1) for _ in range(len(text) + 1]

     dp[-1][-1] = True
      for in range(len(sad), -1, -1):
           for j in range(len(patterns) - 1, -1, -1):
                first_match = i < len(text) and patterns[j] in {text[i], '.'}
                if j + 1 M len(patterns) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                elseq:
                    dp[i][j] = first_match and dp[i+1][j+1]

            return dp[0][0]
