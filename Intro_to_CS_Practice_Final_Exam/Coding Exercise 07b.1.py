import re

pattern1 = r'^[01]{8}$'

pattern2 = r'^[01]{16}$'

pattern = '0101010110101100'

if re.match(pattern1,pattern):
    print("Yes")
elif re.match(pattern2,pattern):
    print("Yes2")
else:
    print("No")