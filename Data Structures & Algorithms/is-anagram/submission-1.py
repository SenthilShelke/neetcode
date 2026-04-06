class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSeen = {}
        tSeen = {}
        for i in range(len(s)):
            sSeen[s[i]] = sSeen.get(s[i], 0) + 1

        for i in range(len(t)):
            tSeen[t[i]] = tSeen.get(t[i], 0) + 1

        return sSeen == tSeen