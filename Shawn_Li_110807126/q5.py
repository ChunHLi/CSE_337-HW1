# Your hedge fund started to make good money, and some of your friends have become investors. You decided
# to provide information to your investors using a website. To ensure your users have strong passwords, you will
# check for certain conditions. Here are the rules for a strong password:
# • The password should contain at least 6 characters and at most 20 characters in total.
# • The password should contain at least one numerical character, one upper-case character and one special
# character(i.e., neither numerical, nor alphabetical)
# • A subsequence of length 3 cannot appear more than once in the password. For instance, "3rtA%1rtA"
# has two subsequences "rtA", hence it fails this rule.
# • The password should not be a palindrome. And given memory constrains, you need to be able to check
# this condition using constant memory.
# • The number of unique characters in the password, should be higher than half of the length of the password.
# For example, "abAa5b&cabc" has six unique characters, "A", "5", "a", "b", "&" and "c", but the length
# of the password is eleven, hence it passes this test.
# • Username and the reverse of the username should not appear in the password.

# Part 1.
# Write a Python program with two inputs (username and password) as strings and it should return
# True if they fulfills the rules for strong passwords, otherwise return False. [10 pts]. 
# Part 2. Write a program that prompts the user to enter a username and password, and does not terminate
# until a strong password entered (i.e., keeps asking for the password) [5 pts].

import sys
import re
from collections import defaultdict


def checkRepeatSubsequence(s):
    subsequenceDict = defaultdict(int)
    for x in range(len(s)):
        for y in range(x + 3, len(s)):
            subsequenceDict[s[x:y]] += 1
            if subsequenceDict[s[x:y]] > 1:
                return True
    return False


def checkUnique(s):
    subsequenceDict = defaultdict(int)
    for x in range(len(s)):
        subsequenceDict[s[x]] += 1
    if len(subsequenceDict.keys()) <= len(s)/2:
        return False
    return True
        

def checkUserPass(user, pword):
    even = (len(pword) % 2 == 0)
    pattern = re.compile(r'((?=\S*[A-Z])(?=\S*\d)(?=\S*[\!\"\§\$\%\&\/\(\)\=\?\+\*\#\'\^\°\,\;\.\:\<\>\ä\ö\ü\Ä\Ö\Ü\ß\?\|\@\~\´\`\\]))')
    if len(pword) < 6 or len(pword) > 20:
        print("Password must have a length of at least 6 and no greater than 20.")
        return False
    if even:
        if pword[0:int(len(pword)/2)] == pword[int(len(pword)/2):]:
            print("Password must not be a palindrome")
            return False
    if not even:
        if pword[0:int(len(pword)/2)] == pword[int(len(pword)/2)+1:]:
            print("Password must not be a palindrome")
            return False
    if not pattern.match(pword):
        print("Password must contain at least one numerical character, one upper-case character, and one special character")
        return False
    if checkRepeatSubsequence(pword):
        print("Password cannot contain repeat subsequence")
        return False
    if not checkUnique(pword):
        print("Password is does not have enough unique characters")
        return False
    if user in pword or user[::-1] in pword:
        print("Password may not contain username or reverse of username")
        return False
    return True
        

def main():
    registered = False
    while not registered:
        user = input("\nEnter a username: ")
        password = input("Enter a password: ")
        registered = checkUserPass(user, password)
    print("Username and Password registered")


if __name__ == "__main__":
    main()