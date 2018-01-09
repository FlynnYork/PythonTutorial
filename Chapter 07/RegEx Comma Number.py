#Build with Python 2.7.14

import re
text = '''  
        42
        1,234
        6,368,745
        12,34,567
        1234 
                    '''

numRegex = re.compile(r'(?<!\S)\d{1,3}(?:,\d{3})*(?!\S)')
num = numRegex.findall(text)
print num

##################################################################
'''
Related reference pages:
https://stackoverflow.com/questions/43171883/regex-that-matches-a-number-with-commas-for-every-three-digits
'''
##################################################################
'''
20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
'42'
'1,234'
'6,368,745'

but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
'''
