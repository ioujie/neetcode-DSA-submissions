# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        m = len(pairs) // 2
        
        if m == 0:
            return pairs

        return self.merge(self.mergeSort(pairs[:m]), self.mergeSort(pairs[m:]))

    def merge(self, arr1: List[Pair], arr2: List[Pair]) -> List[Pair]:
        sortedArr = []
        p1, p2 = 0, 0
        while(p1 < len(arr1) and p2 < len(arr2)):
            if arr1[p1].key <= arr2[p2].key:
                sortedArr.append(arr1[p1])
                p1 += 1
            else:
                sortedArr.append(arr2[p2])
                p2 += 1
        if p1 < len(arr1):
            for x in arr1[p1:]:
                sortedArr.append(x)
        else:
            for x in arr2[p2:]:
                sortedArr.append(x)

        return sortedArr 


        