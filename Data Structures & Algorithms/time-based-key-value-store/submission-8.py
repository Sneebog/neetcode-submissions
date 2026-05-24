class TimeMap:

    def __init__(self):
        self.keystores = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keystores:
            self.keystores[key].append((timestamp, value))
        else:
            self.keystores[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.keystores.get(key, [])
        
        if len(values) ==0 :
            return ""
        
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] == timestamp:
                res = values[m][1]
                break
            
            if values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res


