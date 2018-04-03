print 'string'
print 'this is also a string with multiple words'
print "this string with double quote"

# when to use "" and when ''
print "I'm learning python"
print '"this is a quote"'

# new line
print 'First line \n Second line'
# tab
print 'first word \t second tab'
# print function
print("first word")

# String basics
print (len("hello world"))  # string length
s = 'hello world'
print s
print len(s)

# indexing
print s[0]
print s[10]

# slicing s[from index: up to index]
print s[1:6]
# -1 means starts from last index
print s[-1]
print s[:-1]
# we can also do stepping
print s[::1]  # going to print everything
print s[::2]  # going to print indexes 2 4 6...
# with that we also can reverse a string
print s[::-1]  # this will start printing from last index

# String properties
# IMMUTABLE : you can't change an index after assigning it
# Concatenation: you can concatenate two strings
print s + ' concatenated'
# also
s = s + ' concatenated'
print s

# string with Arithmetic
animal = 'cat '
print 10*animal  # will print "cat cat cat cat cat cat cat cat cat cat "

# built in string methods
print s.upper()  # turns into uppercase
print s.isalnum()  # checks if it is all number
print s.title()  # makes it title




