class Solution:

    def __init__(self):
        self.length = 0

    def isCompleteCircuit(self, Index, Gas):
        Sum = 0
        for i in range(Index - self.length, Index):
            Sum += Gas[i]
            if Sum < 0:
                return False
        return True

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # len gas => gas stations along a circular route
        # gas => amount of gas in each stations(indexes)
        # cost => amount of gas to reach next gas stations
        # start journey with empty tank in one of gas stations
        # return the starting gas where you can back to it once(unique solution) or -1

        # make array smaller => gas - cost => [-2, -2, -2, 3, 3] =>
        # [-6, 6] with start indexes [0, 3]
        tmp = counter = 0
        starts = [0]
        prev = gas[counter] - cost[counter]

        for i in range(len(gas)):  # O(n)
            gas[i] = gas[i] - cost[i]
            if (gas[i] >= 0 and prev < 0) or (gas[i] < 0 and prev >= 0):
                cost[counter] = tmp
                starts.append(i)
                counter += 1
                tmp = 0
            tmp += gas[i]
            prev = gas[i]
        if tmp != 0:
            cost[counter] = tmp
            counter += 1

        if sum(gas) < 0:  # O(n)
            return -1

        # check if car canCompleteCircuit
        cost = cost[:counter]
        self.length = counter
        for i in range(counter):
            if self.gas_delta[i] >= 0:
                if self.isCompleteCircuit(i, cost):
                    return starts[i]

        return 0


s = Solution()
print(s.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
