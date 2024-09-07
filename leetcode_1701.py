class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        currentTime = 0
        waitingTime = 0
        for cus in customers:
            arrT, orderT = cus
            if currentTime < arrT:
                currentTime = arrT
            currentTime = currentTime + orderT
            waitingTime += currentTime - arrT
        return waitingTime/len(customers)
    
    
s = Solution()
print(s.averageWaitingTime([[1,2],[2,5],[4,3]]))