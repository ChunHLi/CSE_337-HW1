# Part 1.
# To this end, you need to write a program that gets a filename and n
# as input, retrieves the text, and returns a dictionary where keys are
# n-grams(i.e.,groups of n consecutive words), and the values are the
# number of occurrences of n-grams that appear more than once in the text [15 pts]. 
# Note: For the purposes of this question, assume 1≤n≤10.

# Part 2.
# Using the results of the previous part, find the 10n-grams with the highest total length
# (i.e., len(w1) + len(w2) + len(w3))[5 pts].
# You can test your program on this file after downloading it: http://www.gutenberg.org/files/100/100-0.txt
import re
from collections import defaultdict


def ngrams(filename, n):
    text = open(filename, encoding="utf8").read()
    text = re.sub('[\n]+', ' ', text)
    text = re.sub('[\t]+', ' ', text)
    text = ' '.join(text.split())
    gramDict = defaultdict(int)
    splitText = text.split()
    for x in range(len(splitText)-n):
        sublist = splitText[x:x+n]
        newStr = " ".join(sublist)
        gramDict[newStr] += 1
    return gramDict


def main():
    gramDict = ngrams('100-0.txt', 3)
    gramKeys = gramDict.keys()
    gramList = list(gramKeys)
    gramList.sort(key=lambda x: len(x))
    gramList = gramList[-10:]
    gramList.reverse()
    for x in range(len(gramList)):
        print(str(x)+'.', gramList[x])

if __name__ == "__main__":
    main()