def twoNumberSum(array, targetSum):

    visited = set()

    for num in array:
        match = targetSum - num

        if match in visited:
            return [match, num]
        
        visited.add(num)


    return[]
        

n = [1,2,3,9,5]
targetNums = twoNumberSum(n, 12)
print ("targetNums:" , targetNums)
