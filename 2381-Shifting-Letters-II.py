class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        net_shift = 0  
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1
                net_shift = 0
        result = []
        for i in range(n):
            net_shift += diff[i]
            new_char = chr(((ord(s[i]) - ord('a') + net_shift) % 26) + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
        