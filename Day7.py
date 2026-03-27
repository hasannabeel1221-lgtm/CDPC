#Roy and Profile Picture
# L = int(input())
# N = int(input())
# for x in range(N):
#     W, H = map(int, input().split())
#     if W < L or H < L:
#         print("UPLOAD ANOTHER")
#     elif W == H:
#         print("ACCEPTED")
#     else:
#         print("CROP IT")

# 1 Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.
# T = int(input())
# for _ in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#     K = K % N
#     a1 = arr[:-K]
#     a2 = arr[-K:]
#     a3 = a2 + a1 
#     print(*a3)

# Toggle String
# S = input()
# ans = ""
# for x in S:
#     if x.isupper():
#         ans += x.lower()
#     elif x.islower():
#         ans += x.upper()
#     else:
#         ans += x
# print(ans)


#Using Swaping Case
# s=input()
# ans.s.swapcase()
# print(ans)

#Array Rotation Task
# arr = [1, 2, 3, 4, 5]
# n = 2
# n = n % len(arr)   # Handle large n
# for _ in range(n):
#     temp = arr[-1]   # last element
#     for i in range(len(arr)-1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = temp
# print(arr)