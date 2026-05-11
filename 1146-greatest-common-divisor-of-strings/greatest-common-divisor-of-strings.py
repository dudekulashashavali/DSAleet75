class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller = str1 if len(str1)< len(str2) else str2
        for i in range(len(smaller),0,-1):
            candidate = smaller[:i]
            if len(str1) % len(candidate) == 0 and  len(str2) % len(candidate) == 0 :
                if candidate * (len(str1) // len(candidate)) == str1 and  candidate * (len(str2) // len(candidate)) == str2 :
                    return candidate
        return ""