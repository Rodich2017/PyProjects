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

some1 = random.randrange(2,kolko-3)
some2 = random.randrange ( 1, kolko -2 )
some3 = random.randrange ( 1, kolko - 1 )
some4 = random.randrange ( 1, kolko )

if (some1 != some2):
    if (some3 != some4):
        if (some2 != some3):
            if (some1 != some4):
                if (some1 != some3):
                    if  (some2 != some4):
                        print(some1, some2, some3, some4)


