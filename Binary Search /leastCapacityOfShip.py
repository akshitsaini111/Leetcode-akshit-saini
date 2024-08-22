class Solution:

    def leastCap(self, weights, d):
        s = max(weights)
        e = sum(weights)
        res = e

        def cap(capacity):
            ship = 1
            currCap = capacity
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = capacity
                currCap -= w

            return ship <= d

        while s <= e:
            mid = s + ((e - s) // 2)
            if cap(mid):
                res = min(res, mid)
                e = mid - 1
            else:
                s = mid + 1
        return res
