import random
import sys

# ================================================
#  LOTO - 4 happy digits from Your choice numbers
# ================================================

try:
    kolko = int(input("Plese enter some number in a range from 11 to 49: "))
except ValueError:
    print("Not a number")
    exit ( )

some = 0
flag = 0

for i1 in (2,kolko-3):
    some1 = random.randrange(2,kolko-3)
    # print(some1)
    if flag == 1:
        break
    for i2 in (1, kolko-2):
        some2 = random.randrange ( 1, kolko -2 )
        # print ( some2 )
        if flag == 1:
            break
        for i3 in (1, kolko-1):
            some3 = random.randrange ( 1, kolko - 1 )
            # print ( some3 )
            if flag == 1:
                break
            for i4 in (1, kolko):
                some4 = random.randrange ( 1, kolko )
                # print(some4)
                if flag == 1:
                    break
                if (some1 != some2):
                    if (some3 != some4):
                        if (some2 != some3):
                            if (some1 != some4):
                                if (some1 != some3):
                                    if  (some2 != some4):
                                        print(some1, some2, some3, some4)
                                        flag = 1
                                        break
