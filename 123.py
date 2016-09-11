from collections import defaultdict
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containskey = 1 if key in self else 0
        if len(self)-containskey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containskey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

dd = LastUpdatedOrderedDict(3)
dd['a'] = 1
dd['b'] = 2
dd['c'] = 3
dd['d'] = 4
dd['b'] = 6
print(dd)


# 具体实现细节若有忘记看廖雪峰collections章节下面的评论留言