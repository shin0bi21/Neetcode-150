class Solution:

    # unicode for lowercase alphabet ranges from 97-122
    # subtracting ord a normalizes value to be from 0-25
    def normalize(self, char: str) -> int:
        return ord(char) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:

        # python stores string length inside the object
        # for O(1) retreival
        if len(s) != len(t):
            return False

        # initialize direct address table
        counts = [0]*26


        # lengths are validated to be equal, can loop len of s or t
        for i in range(len(s)):
            
            s_index = self.normalize(s[i])
            t_index = self.normalize(t[i])

            counts[s_index] +=1
            counts[t_index] -=1

        # once array has been updated, loop for verification 
        # if isAnagram, all counts will be 0
        for count in counts:
            if count !=0:
                return False

        return True