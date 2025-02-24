import re

# str1 = "she sells seashells by the seashore"
# pattern = r"\d+"
# if re.search(pattern, "LXI 2013,VX[ 2014, VDI 20104, Maruti Suzuki Cars in India"):
#     print("Match")
# else:
#     print("No match")


str2 = "wazzaaaap wazzaap wazzaaap"
pattern = r".*a{4}p"

x = re.findall(pattern, str2)

for i in x:
    print(i, end=" ")
