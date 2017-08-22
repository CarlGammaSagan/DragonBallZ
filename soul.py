#! /usr/bin/python

import re

print "Hello Sissel's Molde Canticle!"
inputFileName=raw_input("Please enter the file name of your dataset to enjoy some good ole fashion fun:")
inputRegEx=raw_input("Please enter a regular expression and make some good use of that miracle of human magicka, the Kleene Star:")
f = open(str(inputFileName), 'r')
z = f.readlines()
print z

print "\n\n\n\n\n__________Magic: The Gathering 10/10 Wall__________"
splits = re.split("the", str(z))
#print str(splits)

#nSplits=len(splits)
#nOccurrencesOfString=nSplits+1 #someone please check if this is correct. just to be sure...
#print "Number of splits:", len(splits)
#print "Number of occurrences of this string in this dataset:", nOccurrencesOfString

v=re.search(z,inputRegEx);

print v
print "____________________Magic: The Gathering 20/20 Wall____________________"
