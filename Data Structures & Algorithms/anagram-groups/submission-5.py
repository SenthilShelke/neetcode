class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original = strs.copy()

        for i in range(len(strs)):
            strs[i] = "".join(sorted(strs[i]))

        map = {}
        for i in range(len(strs)):
            if strs[i] not in map:
                map[strs[i]] = []
            map[strs[i]].append(original[i])

        toReturn = []
        for key in map:
            toReturn.append(map[key])

        return toReturn


        