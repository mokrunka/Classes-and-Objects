#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.

def are_anagrams(string1, string2):
    count = 0
    new_string1 = string1.lower()
    new_string2 = string2.lower()
    b = len(new_string1)
    # if len(new_string1) >= len(new_string2):
    for char in new_string1:
        print(char in new_string2)
        if char in new_string2:
            print(char)
            new_string2 = new_string2.replace(char, '', 1)
            count += 1

    if (count == b) and (len(string1) >= len(string2)):
        return True
    else:
        return False

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
# print(are_anagrams("Elvis", "Lives"))
# print(are_anagrams("Elvis", "Live Viles"))
# print(are_anagrams("Eleven plus two", "Twelve plus one"))
# print(are_anagrams("George P Burdell", "Prelude Blogger"))
# print(are_anagrams("Christmas", "Trims Cash"))
print(are_anagrams("Snooze Alarms", "Alas No More Zs"))