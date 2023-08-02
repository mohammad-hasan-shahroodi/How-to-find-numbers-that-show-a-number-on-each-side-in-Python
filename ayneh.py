x = int(input())
y = 0
A = []
while x != 0:
    A.append(x%10)
    y += (x%10)
    x = x //10
for i in range(len(A)):
    if A[i] == A[(len(A)-(i+1))]:
        result = 1
    else:
        result = 0
        break
if result == 1 :
    print("This number on each side is one number")
else:
    print("NORMAL")
