# print("Hello, World!")
# print all the subsequences of a list / arrary 
def solve(index,subset):
  if index>=len(nums):
    result.append(subset.copy())
    return
  
  subset.append(nums[index])
  solve(index+1,subset)
  subset.pop()
  solve(index+1,subset)


nums = [5,9,7]
result = []
print("the subsequences of nums are:")
solve(0,[])
print(result)
