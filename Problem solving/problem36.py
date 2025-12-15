# import re
# T = int(input())

# for i in range(T):
#     regex = input()
#     try:
#         re.compile(regex)
#         print("True")
#     except:
#         print("False")

import re

T = int(input())

invalid_pairs = ['**', '++', '??', '*+', '+*', '?*', '+?', '*?']

for i in range(T):
    pattern = input()
    
    if any(pair in pattern for pair in invalid_pairs):
        print("False")
        continue
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
