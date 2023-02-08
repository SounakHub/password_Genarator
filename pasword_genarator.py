import string
import random
s1 = string.ascii_lowercase
# s.extend(list(s1))
# print(s1)
s2 = string.ascii_uppercase
# print(s2)
s3 = string.digits
s4 = string.punctuation
plen = int(input("Enter passwaord length\n"))
# print(plen)
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print(s)

random.shuffle(s)
# print(s)
print("".join(s[0:plen]))