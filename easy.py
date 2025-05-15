#1 second largest
def secondLargest(arr): 
    arr.sort()
    arr.reverse()
    for i in arr: 
      if i != arr[0]: 
        return i

#7 return duplicate element in array
from collections import Counter
def findDupElement(arr): 
  f = Counter(arr).most_common(1)
  return f

#8 bubble sort
def bubbleSort(arr): 
  for i in range(len(arr)):
    swap = False
    for j in range(i, len(arr)-i-1): 
      if arr[j] > arr[j+1]: 
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap = True
    if swap == False: 
      return
    
#9 Lexical graphical order
def lexicalOrder(arr): 
  arr.sort()
  return arr

#10 Binary Search
def binarySearch(arr, findNum): 
  left = 0 
  right = len(arr)-1
  while(left<=right):
    mid = (left+right) //2
    if(arr[mid] > findNum): 
      right = mid - 1
    elif(arr[mid] < findNum): 
      left = mid + 1
    else:
      return mid
  return -1

#11 Find Peak Element
def findPeak(arr):
  left = 0
  right = len(arr) - 1
  while(left<right):
    mid = (left+right) //2
    if(arr[mid] < arr[mid+1]): 
      left = mid + 1
    else:
      right = mid
  return left

#12 find all peak element
def findAllPeak(arr):
  peak = []
  for i in range(1, len(arr)-1): 
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]: 
      peak.append(arr[i])
  return peak

#16 Find GCD by Euclid
def findGCD(x,y): 
  if(x<y):
    x,y = y,x
  while(y != 0):     
     temp = y
     y = x%y
     x = temp
  return x

#17 is power of two 
def isPowerOfTwo(x):
  if(x<0):
    return False
  else: 
    while(x % 2 == 0):
      x /= 2
    return x == 1    

#18 find LCM
def findLCM(x,y):
  return (x*y)//findGCD(x,y)

#22 find ways to climb stair
def findWays(x): 
  if(x == 1):
    return 1; 
  elif(x == 2):
    return 2; 
  else: 
    return findWays(x-1) + findWays(x-2)
 
#23 check a number is Prime
import math
def isPrime(x):
  if(x == 2): 
    return 1
  if(x <=1 or x % 2 == 0):
    return 0  
  for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
    if x%i == 0:
      return 0
  return 1

#24 check a number is a perfect square
def isPerfectSquare(x): 
  if(math.sqrt(x).isnumeric()): 
    return 1
  return 0

#25 reverse positive int number
def reverseNum(x): 
  num = str(x)
  num.reverse()
  return int(num)

#29 calculate distance between two point
def calDistance(a,b): 
  res = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
  return round(res, 2)

#30 Heron's formular
def areaOfTriangle(a,b,c): 
  p = (a+b+c)/2
  S = math.sqrt(p*(p-a)*(p-b)*(p-c))
  return round(S,2)

#31  Calculate Circumference and Area of circle
def calCircumferenceAndArea(r): 
  C = 2*math.pi*r
  S = r**2*math.pi
  return round(C,2), round(S,2)

#39
def sumAllMatrix(matrix):
  sum = 0 
  for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
      sum += matrix[i][j]
  return sum

#40 max element in matrix
def maxElementMatrix(matrix): 
    max = matrix[0][0]
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            if matrix[i][j] > max:
                max = matrix[i][j]
    return max

#41 print zigzag matrix (HARD)
def zigzagTraversal(matrix, m, n):
    result = []
    for diag in range(m + n - 1):
        if diag % 2 == 0:
            # Move diagonally up
            row = min(diag, m - 1)
            col = diag - row
            while row >= 0 and col < n:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            # Move diagonally down
            col = min(diag, n - 1)
            row = diag - col
            while col >= 0 and row < m:
                result.append(matrix[row][col])
                row += 1
                col -= 1
    return result


#42 sum of element in diagonal matrix 
def sumOfDiagonalMatrix(matrix):
  sum = 0 
  for i in range(len(matrix)):
    for j in range(len(matrix[i])): 
      if i == j: 
        sum += matrix[i][j]
  return sum 

#43 add two matrix
def addMatrix(matrix1, matrix2):
  result = []
  for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[i])):
      row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
  return result

#48 calculate length of last word
def lengthOfLastWord(sentence): 
  words = sentence.split()
  lastWord = list(words[-1])
  return len(lastWord)

#49 dot product of two arrays
def calDotProduct(arr1, arr2): 
  product = arr1[0]*arr2[0] + arr1[1]*arr2[1] + arr1[2]*arr2[2]
  return round(product,2)

#50 pool size
def maxPooling(matrix, m, n, pool_size):
  result = []
  for i in range(0, m, pool_size):
      row = []
      for j in range(0, n, pool_size):
      # Extract the pool_size x pool_size window
        max_value = float('-inf')
        for x in range(i, min(i + pool_size, m)):
          for y in range(j, min(j + pool_size, n)):
              max_value = max(max_value, matrix[x][y])
        row.append(max_value)
      result.append(row)
  return result

#52 count vowel 
def countVowel(word): 
  vowels = "ueoaiUEOAI" 
  count = sum(1 for char in word if char in vowels)
  return count

#53 is anagram 
def isAnagram(s1,s2): 
  if len(s1) != len(s2): 
    return False
  count = sum(1 for char in s1 if char in s2)
  if count == len(s2): 
    return True
  else: 
    return False

#55 if two circle is intersect
import math
def isIntersect(h1,k1,r1,h2,k2,r2): 
  d = math.sqrt((h1 - h2)**2 + (k1 - k2)**2)
  if d > (r1+r2): 
    print(0)
  elif d < abs(r1-r2): 
    print(0)
  elif (d==0) and (r1==r2): 
    print(1)
  else: 
    print(1)
  
#56 find perpendicular distance
def findPerpendicularDistance(x,y,a,b,c): 
  d = abs(a*x+b*y+c)/math.sqrt(a**2 + b**2)
  return round(d, 1)

#58 find Step
def countStep(num): 
  if num <=  0: 
    return 
  else: 
    count = 0 
    while(num>0):
      if (num%2 == 0): 
        num = num/2
        count += 1
      else:  
        num = num - 1
        count += 1
  return count

# 60 find degree of each vertex in graph
def findDegree(graph): 
  degree = {}
  for i in range(len(graph)): 
    degree[i] = 0
  for i in range(len(graph)): 
    for j in range(len(graph[i])): 
      if graph[i][j] == 1: 
        degree[i] += 1
  return degree


#61 count step to reduce number to zero
def countStepToZero(num): 
  if num <= 0: 
    return 0
  else: 
    count = 0 
    while(num>0):
      if (num%2 == 0): 
        num = num/2
        count += 1
      else:  
        num = num - 1
        count += 1
  return count

#62 generate fibonacci
def genFibo(n): 
    fibo_sequence = [0, 1]
    if n <= 2:
        return fibo_sequence[:n]
    for i in range(2, n):
        next_fib = fibo_sequence[i - 1] + fibo_sequence[i - 2]
        fibo_sequence.append(next_fib)
    return fibo_sequence

#63 Longest Continuous Subsequence
def findLCIS(nums):
  if not nums:
      return 0
  max_length = 1
  current_length = 1
  for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
      current_length += 1
      max_length = max(max_length, current_length)
    else:
      current_length = 1
  return max_length

#67 check is perfect cube
def isPerfectCube(num): 
  if num < 0:
      root = round(abs(num) ** (1/3))
      return -root ** 3 == num
  root = round(num ** (1/3))
  return root ** 3 == num

#70 find number of divisor
def findDivisors(num): 
  count = 0 
  for i in range(1,num+1): 
    if num%i == 0: 
      count += 1
  return count

if __name__=="__main__":
#   n = int(input())
  # arr1 = list(map(int, input().split()))
  # k = int(input())
  # arr2 = list(map(int, input().split()))

  m, n = map(int, input().split())
  matrix1 = [list(map(int, input().split())) for _ in range(m)]
  matrix2 = [list(map(int, input().split())) for _ in range(m)]
  print(addMatrix(matrix1, matrix2))
