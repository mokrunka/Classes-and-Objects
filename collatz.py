def collatz(current_number):
   print(current_number)
   if not current_number == 1:
       if current_number % 2 == 0:
           return collatz(current_number // 2)
       else:
           return collatz(current_number * 3 + 1)

print(collatz(5))