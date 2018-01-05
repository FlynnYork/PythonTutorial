#Build with python 2.7.14

def fun(spam):
    value2=''
    for value in spam:
        if value !=spam[-1]:
            value = value+', '
            print value
            value2 = value2 + value
            print value2+'and '+spam[-1]
    return value2+'and '+spam[-1]


spam = ['apples', 'bananas', 'tofu', 'cats','cat', 'bat', 'rat', 'elephant','A', 'B']
fun(spam)
print fun(spam)
