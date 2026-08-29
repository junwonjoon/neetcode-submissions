from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.key_dict = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if "times" not in self.key_dict[key]:
            self.key_dict[key]["times"] =  [timestamp]
        else:
            self.key_dict[key]["times"].append(timestamp)
        self.key_dict[key] |= {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.key_dict:
            return self.key_dict[key][timestamp]
        else:
            if key not in self.key_dict:
                return ""
            lst = self.key_dict[key]["times"]
            new_timestamp = findLowerBound(lst, timestamp)
            if new_timestamp is None:
                return ""
            return self.key_dict[key][new_timestamp]

            
def findLowerBound(lst, target):
    return_val = None
    for elem in lst:
        if elem > target:
            break
        return_val = elem
    return return_val
