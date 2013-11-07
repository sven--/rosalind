with open("FindingAMotifInDNA.input") as f:
  s = f.readline().strip()
  t = f.readline().strip()
  for i in range(0, len(s) - len(t)):
    chk = True
    for j in range(0, len(t)):
      chk &= s[i+j] == t[j]
      if(not chk):
        break
    if(chk):
      print i+1
