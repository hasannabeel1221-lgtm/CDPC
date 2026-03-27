# 1.  Compare the triplets
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# Complete the 'compareTriplets' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
# def compareTriplets(a, b):
#     alice = 0
#     bob = 0
#     for i in range(3):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1    
#     return [alice, bob]
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))
#     result = compareTriplets(a, b)
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#     fptr.close()

# 2. A very big sum
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# Complete the 'aVeryBigSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
# def aVeryBigSum(ar):
#     total = 0
#     for i in ar:
#         total += i
#     return total
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     ar_count = int(input().strip())
#     ar = list(map(int, input().rstrip().split()))
#     result = aVeryBigSum(ar)
#     fptr.write(str(result) + '\n')
#     fptr.close()

#  3. Diagonal Difference
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# def diagonalDifference(arr):
#     d1 = 0
#     d2 = 0
#     n = len(arr)
#     for i in range(n):
#         d1 += arr[i][i]
#         d2 += arr[i][n-i-1]
#     return abs(d1 - d2)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input().strip())
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     result = diagonalDifference(arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()

# 4. Plus Minus 
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
# def plusMinus(arr):
#     pos = 0
#     neg = 0
#     zero = 0
#     n = len(arr)
#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i < 0:
#             neg += 1
#         else:
#             zero += 1
#     print("{:.6f}".format(pos/n))
#     print("{:.6f}".format(neg/n))
#     print("{:.6f}".format(zero/n))         
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))
#     plusMinus(arr)
