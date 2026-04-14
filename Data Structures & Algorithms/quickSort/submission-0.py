# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1

        def qs(arr, s, e):
            if e <= s:
                return
            
            pivot = arr[e]
            l = s

            for i in range(s, e):
                if arr[i].key < pivot.key:
                    arr[i], arr[l] = arr[l], arr[i]
                    l += 1
            
            arr[e], arr[l] = arr[l], arr[e]

            qs(arr, s, l - 1)
            qs(arr, l + 1, e)

        qs(pairs, s, e)

        return pairs
