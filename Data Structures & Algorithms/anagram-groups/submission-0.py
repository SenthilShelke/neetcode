class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = strs[:]
        for i in range(len(strs)):
            strs[i] = tuple(sorted(strs[i]))

        map = {}
        for i in range(len(strs)):
            if strs[i] not in map:
                map[strs[i]] = []
            map[strs[i]].append(i)

        toReturn = []
        i = 0
        for key in map:
            toReturn.append([])
            for j in range(len(map[key])):
                toReturn[i].append(temp[map[key][j]])
            i += 1
        
        return toReturn