import random as rm
import time as tm

print(tm.ctime())
print(tm.localtime())

print(rm.random())
#
# for i in range(10):
#     tm.sleep(1)
#     print(tm.ctime())

test_list = [x for x in range(10)]
print(f"Choice: {rm.choice(test_list)}")
