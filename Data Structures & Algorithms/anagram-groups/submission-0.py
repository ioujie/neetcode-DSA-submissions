class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for s in strs:
            keyStr = "".join(sorted(s))

            myDict[keyStr].append(s)

        return list(myDict.values())