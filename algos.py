# def tri(n):
#     if n == 1:
#         return 1
#     else:
#         return n + tri(n - 1)
#
# print(tri(6))

def fib3(n):
   if n <= 3:
       return 1
   else:
       return(fib3(n-1) + fib3(n-2) + fib3(n - 3))

print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))

# 1 1 1 3 5 9 17 31