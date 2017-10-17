# ---------- convert BGN to USD -------------------
# rateUSD = 1.79549
# convValue = float(input())
# newValue = convValue * rateUSD
# print(round(newValue,2))
# -------------------------------------------------
# ---------- convert BGN to EUR, USD or GBP -------

value = float ( input ( ) )
currIn = input ( )
currOut = input ( )
a = 0.00
b = 0.00

if currIn == "BGN":
    a = value
elif currIn == "USD":
    a = value * 1.79549
elif currIn == "EUR":
    a = value * 1.95583
elif currIn == "GBP":
    a = value * 2.53405

if currOut == "BGN":
    b = a / 1
elif currOut == "USD":
    b = a / 1.79549
elif currOut == "EUR":
    b = a / 1.95583
elif currOut == "GBP":
    b = a / 2.53405

print ( "%.2f" % b + " " + currOut )
# print(round(b,2))

# -------------------------------------------------

