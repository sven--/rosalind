a = input()
b = input()
A = [1, 1]
for i in range(0, a-1):
  A.append(A[i]*b + A[i+1])
print A[a-1]

