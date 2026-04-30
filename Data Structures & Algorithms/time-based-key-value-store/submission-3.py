class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                items = list(self.store[key].items())
                l, r = 0, len(items) - 1
                res = ""
                while l <= r:
                    m = l + ((r-l)//2)

                    if items[m][0] > timestamp:
                        r = m - 1
                    elif items[m][0] <= timestamp:
                        res = items[m][1]
                        l = m + 1
                return res
        return ""