ans = 0
with open("CountingPointMutations.input", "r") as f:
  s = f.readline()
  t = f.readline()
  for i in range(0, len(s)):
    if(s[i] != t[i]):
      ans += 1
print ans
