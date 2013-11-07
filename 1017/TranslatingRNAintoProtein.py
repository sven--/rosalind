a = {}
ans = ""
with open("CodonTable", "r") as f:
  for line in f:
    for i in range(0, 4):
      a[line.split()[2*i]] = line.split()[2*i+1]
with open("TranslatingRNAintoProtein.input", "r") as f:
  b = f.readline()
  for i in range(0, len(b)/3):
    if(a[b[i*3] + b[i*3+1] + b[i*3+2]] == "Stop"):
      break
    ans += a[b[i*3] + b[i*3+1] + b[i*3+2]]
print ans
