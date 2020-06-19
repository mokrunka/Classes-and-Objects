# def count_down2(start):
#     while start >= 0:
#         print(f'{start}')
#         start -= 1
#
#
# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #
# #If your function works correctly, this will originally
# #print: 5, 4, 3, 2, 1, 0, each on their own line.
# count_down2(5)

# def countDown(start):
#     if start <= 0:
#         print(start)
#     else:
#         countDown(start - 1)
#         print(start)
#
# countDown(5)
#################################################
# We've started a recursive function below called
# measure_string that should take in one string parameter,
# myStr, and returns its length. However, you may not use
# Python's built-in len function.
#
# Finish our code. We are missing the base case and the
# recursive call.
#
# HINT: Often when we have recursion involving strings, we
# want to break down the string to be in its simplest form.
# Think about how you could splice a string little by little.
# Then think about what your base case might be - what is
# the most basic, minimal string you can have in python?
#
# Hint 2: How can you establish the base case has been
# reached without the len() function?

# You may not use the built-in 'len()' function.

def measure_string(myStr):
    if myStr == '':
        return 0
    else:
        return 1 + measure_string(myStr[1:])


# The line below will test your function. As written, this
# should print 13. You may modify this to test your code.
print(measure_string("13 characters"))
