import math
def calDistance(a,b): 
  res = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
  return round(res, 2)

def isPrime(x):
  if(x == 2): 
    return 1
  if(x <=1 or x % 2 == 0):
    return 0  
  for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
    if x%i == 0:
      return 0
  return 1

#2 merge array
def mergeArray(arr1,arr2): 
  arr1.extend(arr2)
  arr1.sort()
  return arr1

#3 Maximum Subarray
def maxSubarraySum(arr): 
  res = arr[0]
  for i in range(len(arr)): 
    currentSum = 0 
    for j in range(i, len(arr)): 
      currentSum += arr[j]
      res = max(res, currentSum)
  return res

#4 rotate array by k step
def rotateArray(arr,n):  
  if n < len(arr):
    slice_arr = arr[:-n]
    cutted_arr = arr[(len(arr)-n):]  
    print(slice_arr, ", " , cutted_arr)
    cutted_arr.extend(slice_arr)
    print (cutted_arr)
  else: 
    print("Cannot rotate")

#13 search matrix
def searchMatrix(matrix, target): 
  for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
      if matrix[i][j] == target: 
        return True
  return False

#14 find first and last elements in a sorted array 
def findFirstAndLast(arr, target): 
  first = -1
  last = -1
  for i in range(len(arr)): 
    if arr[i] == target: 
      if first == -1: 
        first = i
      last = i
  return (first, last)


#15 index of fixed point
def findFixedPoint(arr): 
  for i in range(len(arr)): 
    if arr[i] == i: 
      return i
  return -1


#19 factorial of number
def factorial(num): 
  if num == 0: 
    return 1
  else: 
    return num * factorial(num-1)

#20 sum of digit number
def sumOfDigit(num): 
  digits = [int(x) for x in str(num)]
  res = sum(digits)
  return res

#26 find the prime factor of a number 
def findPrimeFactor(num): 
  primeFactors = []
  for i in range(2, num+1): 
    if num % i == 0: 
      if isPrime(i) == 1: 
        primeFactors.append(i)
  return primeFactors

#27 cal sum of prime < n 
def sumOfPrime(n): 
  sum = 0 
  for i in range(n+1): 
    if isPrime(i) == 1: 
      sum += i
  return sum

#32 point lines in rectangle
def ifInside(x,y,x1,y1,x2,y2):
  return (x1<=x<=x2) and (y2<=y<=y1)

#34 determine if matrix is symmetric
def isSymmetric(matrix):
  n = len(matrix)
  for i in range(n): 
    for j in range(n): 
      if matrix[i][j] != matrix[j][i]: 
        return False
  return True 


#35 rotate matrix
def rotateMatrix(matrix): 
  n = len(matrix)
  for i in range(n): 
    for j in range(i, n): 
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  for i in range(n): 
    matrix[i].reverse()
  return matrix

#36 find number of islands in given matrix

#37 return matrix after spirally traversing it


#38 find transpose of matrix
def transposeMatrix(matrix): 
  row = []
  new_matrix = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])): 
      row.append(matrix[j][i])
    new_matrix.append(row)
    row = []
  return new_matrix

#44 find majority element in array 


#45 is valid bracklets
def isValidBracklets(bracklets): 
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}
  for char in bracklets:
    if char in mapping:
      if not stack or stack.pop() != mapping[char]:
        return 0
    else:
      stack.append(char)
  return 1  

#46 reverse string
def reversedString(text): 
  words = text.split()
  for i in range(len(words)): 
    print(words[-(i+1)], end=' ')

#47 find first non-repeating character
def find1stNonRepeat(text): 
  chars = [x for x in text]
  freqMap = {}
  for char in set(chars): # use set to remove duplicates in list
    freqMap[char] = chars.count(char)
  for i, char in enumerate(text):
    if freqMap[char] == 1:
      return i
  return -1

#51 calculate dot product of two matrix
def dotProduct(matrix1, matrix2): 
  if len(matrix1[0]) != len(matrix2): 
    return -1
  res = []
  for i in range(len(matrix1)): 
    row = []
    for j in range(len(matrix2[0])): 
      sum = 0 
      for k in range(len(matrix2)): 
        sum += matrix1[i][k] * matrix2[k][j]
      row.append(sum)
    res.append(row)
  return res

#54 check specific triangle
def checkSpecificTriangle(x1,y1,x2,y2,x3,y3): 
  A = [x1,y1]
  B = [x2,y2]
  C = [x3,y3]
  a = calDistance(A,B)
  b = calDistance(B,C)
  c = calDistance(C,A)
  if a == b == c: 
    print("equilateral")
  elif (a==b) or (b==c) or (c==a): 
    print("isosceles")
  else: 
    print("scalene")

#57 distance between point and line segment
def distancePointLineSegment(x1,y1,x2,y2,x3,y3):
  P = [x1,y1]
  A = [x2,y2]
  B = [x3,y3]
  vectorAB = [B[0] - A[0], B[1] - A[1]]
  vectorAP = [P[0] - A[0], P[1] - A[1]] 
  dotProductABAP = vectorAB[0] * vectorAP[0] + vectorAB[1] * vectorAP[1]
  dotProductABAB = vectorAB[0] * vectorAB[0] + vectorAB[1] * vectorAB[1]  
  t = dotProductABAP / dotProductABAB
  if t < 0: 
    return calDistance(P, A)
  elif t > 1: 
    return calDistance(P, B)
  else: 
    x = A[0] + t * vectorAB[0]
    y = A[1] + t * vectorAB[1]
    return calDistance(P, [x,y])

#64 find the kth largest in array
def findKthLargest(arr, k): 
  sorted  = arr.copy()  
  sorted.sort()
  sorted = list(reversed(sorted))
  return sorted[k-1]

#68 sum of single digit
def sumOfSingleDigit(num): 
    while(num>9): 
      digits = [int(x) for x in str(num)]
      num = sum(digits)
    return num

#69 check Amstrong number 
def isAmstrongNumber(num): 
  arr = [int(x) for x in str(num)]
  sum = 0 
  for i in arr: 
    sum += (i**len(arr))
  if sum == num: 
    return 1
  else: 
    return 0

if __name__=="__main__":
  # n = int(input())
  # arr1 = list(map(int, input().split()))
  # k = int(input())
  # arr2 = list(map(int, input().split()))
  # print(ifInside(1,1,1,7,4,3))
  m, n = map(int, input().split())
  matrix1 = [list(map(int, input().split())) for _ in range(m)]
  # target = int(input())
  x, y = map(int, input().split())
  matrix2 = [list(map(int, input().split())) for _ in range(y)]
  print(dotProduct(matrix1, matrix2))
