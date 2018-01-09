import re

def checkPassword(password):    
    passRegex1 = re.compile(r'\w{8,}')
    passRegex2 = re.compile(r'\d+')
    passRegex3 = re.compile(r'[a-z]')
    passRegex4 = re.compile(r'[A-Z]')

    checking1 = passRegex1.search(password)
    checking2 = passRegex2.search(password)
    checking3 = passRegex3.search(password)
    checking4 = passRegex4.search(password)

    if bool(checking1) and bool(checking2) and bool(checking3) and bool(checking4):
        print 'Awesome!'
        print password+' is a strong password!'    
    else:
        print 'please set a more stronger password.'

password = 'ssdddDdd32323'

checkPassword(password)

'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
You may need to test the string against multiple regex patterns to validate its strength.

'''
