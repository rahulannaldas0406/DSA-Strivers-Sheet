#Capacity to Ship Packages within D Days

'''Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. 
The packages must be shipped within 'd' days. The weights of the packages are given in an array 'of weights'.
 The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship. 
 Find out the least-weight capacity so that you can ship all the packages within 'd' days .''' 

def findDays(self,weights, capacity):
        days = 1
        load = 0

        for w in weights:
            if load + w > capacity:
                days += 1
                load = w
            else:
                load += w

        return days
def shipWithinDays(self, weights, days):
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) // 2

        required_days = self.findDays(weights, mid)

        if required_days <= days:
            high = mid - 1
        else:
            low = mid + 1

    return low