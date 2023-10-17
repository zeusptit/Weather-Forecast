import re

s = 'United States of America'

res = ''.join(re.findall(r'\b\w', s)).upper()

print(res)