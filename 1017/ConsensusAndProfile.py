A = []
D = {0:'A', 1:'C', 2:'G', 3:'T'}
with open("/Users/LeDief/Documents/KAIST/6th/BS481/1017/ConsensusAndProfile.input", "r") as f:
  current = -1
  index = 0
  for l in f:
    if(l[0] == ">"):
      current += 1
      index = -1
    else:
      l = l.strip()
      for i in range(0, len(l)):
        index += 1
        if(len(A) <= index):
          A.insert(len(A), [0,0,0,0])
        for j in range(0, 4):
          if(l[i] == D[j]):
            A[index][j] += 1
ans = ""
for i in range(0, len(A)):
  cand = 0
  for j in range(0, 4):
    if(A[i][cand] < A[i][j]):
      cand = j
  ans += D[cand]
print ans
for j in range(0, 4):
  print D[j] + ":",
  for i in range(0, len(A)):
    print A[i][j],
  print
