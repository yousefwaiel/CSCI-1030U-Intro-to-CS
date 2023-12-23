import re

pattern = r'^[A-Za-z]{1,10}@[a-z]{1,10}\.[a-z]{0,3}$'

print(re.match(pattern, 'bsmith@gmail.com'))

