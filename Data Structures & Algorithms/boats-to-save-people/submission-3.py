class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #intuition use dictionary to look up optimal pairs
        weights = {}

        for i in range(len(people)):
            if people[i] not in weights:
                weights[people[i]] = 1
            else:
                weights[people[i]] += 1
        
        numBoats = 0

        while weights:
            currWeight = max(weights)
            weights[currWeight] -= 1
            if weights[currWeight] == 0:
                weights.pop(currWeight)

            boatWeight = limit - currWeight
            #now you have the highest weight in the thing, search for limit
            for i in range(boatWeight, 0, -1):
                if i in weights and i <= boatWeight:
                    weights[i] -= 1
                    if weights[i] == 0:
                        weights.pop(i)
                    boatWeight -= i
                    break

            numBoats += 1


        return numBoats