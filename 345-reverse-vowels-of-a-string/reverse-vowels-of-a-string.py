class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        char = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and char[left]  not in vowels:
                left += 1
            while left < right and char[right] not in vowels:
                right -= 1
            char[left],char[right] = char[right],char[left]
            left += 1
            right -= 1

        return "".join(char)
