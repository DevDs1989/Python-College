import re

# Utilize the following functions from re module.
# match()
# search()
# sub()
# findall()
# Utilize the following metacharacters along with suitable examples.
string1 = "123"
string2 = "abc"
string3 = "123abc"
string4 = "abc123"
string5 = "abc123abc"
string6 = "0123456789"
# \A
reg = r"\A[0-9]"
print(re.findall(reg, string5))


# []
reg = r"[a-z]"
print(re.findall(reg, string5))

# [a-zA-Z]
reg = r"[a-zA-Z]"
print(re.findall(reg, string5))
# \b
reg = r"\b[0-9]"
print(re.findall(reg, string1))

# \
reg = r"\\"
print(re.findall(reg, string5))
# [0-9]
reg = r"[0-9]"
print(re.findall(reg, string1))
# \B
reg = r"\B[0-9]"
print(re.findall(reg, string5))

# [0-5]
reg = r"[0-5]"
print(re.findall(reg, string6))
# \d
reg = r"\d"
print(re.findall(reg, string1))
# ^
reg = r"^a"
print(re.findall(reg, string2))
# [a-n]
reg = r"[a-n]"
print(re.findall(reg, string5))

# \D
reg = r"\D"
print(re.findall(reg, string5))
# $
reg = r"a$"
print(re.findall(reg, string2))

# ^a+
reg = r"^a+"
print(re.findall(reg, string2))

# \s
#
# *
#
# a$
#
# \S
#
# +
#
# ^a*
#
# \w
#
# ?
#
# [a-z][A-Z]
#
# \W
#
# {}
#
# ^a+$
#
# \Z
#
# |
#
# ^.ea$
#
# [^]
#
# ()
#
# ^(ab)+$
#
