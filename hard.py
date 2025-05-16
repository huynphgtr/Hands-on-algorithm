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


#6find largest product sub array
def largestProductSub(arr): 
  arr.sort()
  res = arr[0]
  for i in range(len(arr)): 
    currentPro = 0 
    for j in range (i, len(arr)): 
      currentPro -= arr[j]
      res = max(res,currentPro)
    return res
  
#21 number of trailling zero in factorial 
def factorial(num): 
  if num == 0: 
    return 1
  else: 
    return num * factorial(num-1)
  
def trailingZeroFactorial(num): 
  fact = factorial(num)
  count = 0 
  while (fact % 10 == 0): 
    count += 1
    fact = fact / 10
  return count

#28 find the nth prime number 
def thenNthPrime(n): 
  if n < 1: 
    return -1
  count = 0 
  num = 1
  while (count < n): 
    num += 1
    for i in range(2, num): 
      if (num % i == 0): 
        break
    else: 
      count += 1
  return num

#65 merge interval 

#66 number of ways to express n as the sum of two or more consecutive positive integers