class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n

        for i in range(n):
            cur_temp = temperatures[i]
            valid = 0
            for j in range(i + 1, n):
                valid += 1
                next_temp = temperatures[j]

                if next_temp > cur_temp:
                    results[i] = valid
                    break

        return results
        