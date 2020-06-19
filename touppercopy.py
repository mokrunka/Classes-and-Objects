#Write a function called to_upper_copy. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#to_upper_copy should copy the contents of input_file into
#output_file, capitalizing all letters (not just all words,
#each individual letter). You may use the .upper() method
#from the string class.
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# This is some text. Yay text.
#
#Then to_upper_copy would write this text to output_file (the
#first parameter):
#
# THIS IS SOME TEXT. YAY TEXT.
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.

def to_upper_copy(output_file, input_file):
    with open(input_file) as f:
        string_holder = ''
        for line in f:
            string_holder += line
        string_holder = string_holder.upper()
    file2 = open(output_file, 'w')
    file2.write(string_holder)

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left.
to_upper_copy("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")
