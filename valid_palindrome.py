class Solution:
    def isPalindrome(self, s: str) -> bool:

        # data cleaning
        s= s.lower()
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s = clean_s + char
        print(clean_s)
        
        # get all indexes
        first = 0
        last = len(clean_s)-1


        while(first <= last):
            if clean_s[first] == clean_s[last]:
                first += 1
                last -= 1
            else:
                return False
        return True  
