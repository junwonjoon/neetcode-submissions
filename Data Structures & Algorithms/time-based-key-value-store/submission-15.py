import bisect
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
        if key not in self.key_dict:
                return ""
        elif timestamp in self.key_dict[key]:
            return self.key_dict[key][timestamp]
        else:
            lst = self.key_dict[key]["times"]
            new_timestamp = findLowerBound(lst, timestamp)
            if new_timestamp is None:
                return ""
            return self.key_dict[key][new_timestamp]

            
def findLowerBound(lst, target):
    index = bisect_left(lst, target)
    index = index - 1 if index - 1 >= 0 else 0
    if lst[index] > target:
        return None
    else:
        return lst[index]