class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp[key]
        if not arr:
            return ""

        l = 0
        r = len(arr)

        while l < r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                l = m + 1
            elif arr[m][1] > timestamp:
                r = m
            
        if l == 0:
            return ""
        return arr[l - 1][0]
