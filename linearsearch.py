# linear sort algos are of O(n) (Linear) complexity
'''
Hint (1 of 2): Think in terms of how adding items will affect the run time. If you add ten items...
- ...will the runtime remain constant? Then it's constant order.
- ...will the runtime increase by 10, regardless of the previous runtime? Then it's linear order.
- ...will the runtime increase by 10 times the current size of the list? Then it's quadratic order.
- ...will the runtime increase by the current size of the list raised to some power? Then it's polynomial order.
- ...will the runtime increase like crazy? Then it's probably exponential order.
- ...will the runtime increase less the longer the list gets? Then it's logarithmic order.

Hint (2 of 2): If you're still lost, try running through the algorithm with lists of length 1, 2, 3, and 4. How many operations are required for each?
- If the number of operations stays the same, it's constant order.
- If it changes by a consistent rate (e.g. 2, then 4, then 6, then 8), it's linear order.
- If it grows quadratically (e.g. 1, then 4, then 9, then 16), it's quadratic order.
- If it grows polynomially (e.g. 1, then 8, then 27, then 64), it's polynomial order.
- If it grows exponentially (e.g. 2, then 4, then 8, then 16), it's exponential order.
- If it seems to be growing slower (e.g. 2, then 7, then 11, then 14), it's probably logarithmic order.
'''

def linear(list_of_strings, string):
    for i in range(len(list_of_strings)):
        if list_of_strings[i] == string:
            return i
        elif i == len(list_of_strings) - 1:
            return False
        else:
            pass


##############################
# another way

# First, we declare the function:
def linear(a_list, an_item):
    # Then, we iterate through the list:
    for i in range(len(a_list)):

        # If we've found the item, we're done! Go ahead and
        # return this index.
        if a_list[i] == an_item:
            return i

    # If we reach the end of the function it means we never
    # returned an index, which means we never found the item
    # and can return False.
    return False

a_list = [39, 5, 42, 24, 41, 13, 42, 8, 32, 36, 19, 37, 11, 35, 48, 17, 39, 34, 14, 34]
print(linear(a_list, 28))