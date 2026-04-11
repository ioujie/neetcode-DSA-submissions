class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums)

        def mergeSort(arr, tmp, s, e):
            if s >= e:
                return

            m = (s + e) // 2

            mergeSort(arr, tmp, s, m)
            mergeSort(arr, tmp, m + 1, e)

            if arr[m] <= arr[m + 1]:
                return

            merge(arr, tmp, s, m, e)

        def merge(arr, tmp, s, m, e):
            i = s
            j = m + 1
            k = s

            while i <= m and j <= e:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                else:
                    tmp[k] = arr[j]
                    j += 1
                k += 1

            while i <= m:
                tmp[k] = arr[i]
                i += 1
                k += 1

            while j <= e:
                tmp[k] = arr[j]
                j += 1
                k += 1

            for p in range(s, e + 1):
                arr[p] = tmp[p]

        mergeSort(nums, tmp, 0, len(nums) - 1)
        return nums