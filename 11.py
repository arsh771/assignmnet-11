#Q1
import re
email=input('Enter ID')
a=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',email)
if a:
    print('VALID')
else:
    print('NOT VALID')
  


#Q2
import re
x=input('Enter Indian Phone number:')

match=re.fullmatch('(\+91-)[6-9][0-9]{9}',x)
if a:
    print('VALID')
else:
    print('NOT VALID')
  
