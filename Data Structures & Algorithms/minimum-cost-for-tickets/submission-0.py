class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        memo = {}

        def dfs(current_day):

            if current_day > days[-1]:
                return 0

            if current_day in memo:
                return memo[current_day]

            if current_day not in days_set:
                memo[current_day] = dfs(current_day+1)
                return memo[current_day]

            one = costs[0] + dfs(current_day + 1)
            seven = costs[1] + dfs(current_day + 7)
            thirty = costs[2] + dfs(current_day + 30)

            memo[current_day] = min(one, seven, thirty)
            return memo[current_day]

        return dfs(days[0])