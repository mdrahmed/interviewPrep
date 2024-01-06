# link:

# brute-force solution with time complexity O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 1 2 3 1 4
        # 2 1 1 2 1 0
        ans = []
        for i in range(len(temperatures)):
            cnt = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(cnt)
                    break
                elif j == len(temperatures)-1:
                    ans.append(0)
                cnt += 1
        return ans


# Optimal solution using stack with time complexity O(n)
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                prev_ind = stack.pop()
                ans[prev_ind] = i - prev_ind
            stack.append(i)
        return ans
            
        
        

