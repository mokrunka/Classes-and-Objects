#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.

def check_plagiarism(filename1, filename2):
    with open(filename1) as f1:
        f1_wordlist = f1.readline().split()

    with open(filename2) as f2:
        f2_wordlist = f2.readline().split()

    # make the f1_wordlist always the shorter of the two
    if len(f1_wordlist) > len(f2_wordlist):
        temp = f1_wordlist
        f1_wordlist = f2_wordlist
        f2_wordlist = temp
        print(len(f1_wordlist))
        print(len(f2_wordlist))

    b = 0
    i = 0
    d = 5
    result = ''
    while i < len(f2_wordlist):
        for c in range(len(f2_wordlist) - d):
            while f1_wordlist[c:c + d] == f2_wordlist[b: b + d]:
                result = f2_wordlist[b: b + d]
                # print(result)
                d += 1

        b += 1
        i += 1

    if len(result) == 0:
        return False
    else:
        answer = ''
        for word in result:
            answer += word + ' '
            answer.rstrip(' ')
        return answer

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
# print(check_plagiarism("file_2.txt", "file_3.txt"))
