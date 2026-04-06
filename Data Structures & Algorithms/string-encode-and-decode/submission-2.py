class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedList = []
        for i in range(len(strs)):
            encodedList.append(strs[i] + 'é')

        encoded = ""
        for i in range(len(encodedList)):
            encoded += encodedList[i]


        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split('é')
        decoded.pop()
        return decoded