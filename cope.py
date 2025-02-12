import copy
import decimal
import math
import random
import sys
import time
import types

# test_list = [1, [2, 3], 4, 5]
# print(f"original list: {test_list}")
# copy_list = copy.copy(test_list)
# print(f"shallow copy list: {copy_list}")
# deepcopy_list = copy.deepcopy(test_list)
# print(f"deep copy list: {deepcopy_list}")
#
# test_list[1][0] = 100
# print("changing the value of test_list")
# print(f"original list: {test_list}")
# print(f"shallow copy list: {copy_list}")
# print(f"deep copy list {deepcopy_list}")


print(f"random.choice(): {random.choice([1, 2, 3, 4, 5])}")
print(f"random.random(): {random.random()}")

print(f"random.randint(): {random.randint(1, 10)}")
print(f"random.randrange(1,10): {random.randrange(1, 10)}")
print(f"random.uniform(1,10): {random.uniform(1, 10)}")
print(f"random.sample([1,2,3,4,5], 2): {random.sample([1, 2, 3, 4, 5], 2)}")
print(f"types.LambdaType(): {type(lambda x: x)}")
print(f"types.MethodType(): {type(lambda x: x)}")
print(f"decimal.Decimal(10.5): {decimal.Decimal(10.5)}")
print(f"math.sqrt(25): {math.sqrt(25)}")
print(f"time.ctime(): {time.ctime()}")
print("Sleeping for 5 seconds")
time.sleep(5)
print(f"math.pi: {math.pi}")
print(f"math.pow(2,3): {math.pow(2, 3)}")
print(f"math.trunc(10.5): {math.trunc(10.5)}")
print(f"math.floor(10.5): {math.floor(10.5)}")
print(f"time.gmtime(): {time.gmtime()}")
print(f"sys.version: {sys.version}")
print(f"sys.modules: {sys.modules}")
