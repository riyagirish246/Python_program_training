class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
       
        if k == 0:
            return res
       
        
        if k > 0:
            start, end = 1, k
        else:
            start, end = n + k, n - 1
           
        current_sum = 0
        for i in range(start, end + 1):
            current_sum += code[i % n]
           
        for i in range(n):
            res[i] = current_sum
            
            current_sum -= code[start % n]
            start += 1
            end += 1
            current_sum += code[end % n]
           
        return res


