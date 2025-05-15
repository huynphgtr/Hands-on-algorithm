#5 find number of subarray smaller than value k
def findNumberSubarray(arr, k): 
  num = 0 
  for i in range(len(arr)): 
    currentSum = 0 
    for j in range(i, len(arr)): 
      currentSum += arr[j]
      if currentSum < k: 
        num+= 1
  return num  


#6 (NOT YET)find largest product sub array
def largestProductSub(arr): 
  arr.sort()
  res = arr[0]
  for i in range(len(arr)): 
    currentPro = 0 
    for j in range (i, len(arr)): 
      currentPro -= arr[j]
      res = max(res,currentPro)
    return res