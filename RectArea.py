
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
w = max(x1,x2) - min(x1,x2)
h = max(y1,y2)- min(y1,y2)
area = w*h

per = 2*(w+h)
print(area)
print(per)