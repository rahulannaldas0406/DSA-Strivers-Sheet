#Capacity to Ship Packages within D Days

'''Problem Statement: You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. 
The packages must be shipped within 'd' days. The weights of the packages are given in an array 'of weights'.
 The packages are loaded on the conveyor belts every day in the same order as they appear in the array. The loaded weights must not exceed the maximum weight capacity of the ship. 
 Find out the least-weight capacity so that you can ship all the packages within 'd' days .''' 

'''def findDays(weights, capacity):
        days = 1
        load = 0

        for w in weights:
            if load + w > capacity:
                days += 1
                load = w
            else:
                load += w
        #print(days,capacity)
        return days
def shipWithinDays(weights, days):
    low = max(weights)
    high = sum(weights)

    while low <= high:
        mid = (low + high) // 2

        required_days = findDays(weights, mid)

        if required_days <= days:
            high = mid - 1
        else:
            low = mid + 1

    return low

ans=shipWithinDays([3,5,6,7,9],5)
print(ans)'''


'''Aggressive Cows : Detailed Solution

Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.'''


'''BS on Answer:
1. Define search space
2. Check feasibility (greedy)
3. If possible → try bigger
4. Else → reduce'''

'''from numpy import sort


def canWePlace(arr,dist,cows):
    last=arr[0]
    count_cows=1

    for i in range(1,len(arr)):
        if arr[i]-last>=dist:
            count_cows+=1
            last=arr[i]

        if count_cows>=cows:
            return True
    else:
        return False
    
def aggressiveCows(arr,k):
    stalls=sort(arr) 
    n=len(stalls)

    low=1
    high=stalls[n-1]-stalls[0]

    while low<=high:
        mid=(low+high)//2

        if canWePlace(stalls,mid,k):
            low=mid+1

        else:
            high=mid-1

    return high

print(aggressiveCows([0,3,4,7,10,9],4))'''


#Same pattern used in:

# Aggressive Cows 🐄
# Koko Eating Bananas 🍌
# Allocate Books 📚
# Painters Partition 🎨
# Ship Packages 🚢



