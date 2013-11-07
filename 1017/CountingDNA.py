b = [0,0,0,0]
with open("CountingDNA.input", "r") as f:
  a = f.readline()
  for x in a:
    if(x == "A"): b[0] += 1
    if(x == "C"): b[1] += 1
    if(x == "G"): b[2] += 1
    if(x == "T"): b[3] += 1

print str(b[0]) + " " + str(b[1]) + " " + str(b[2]) + " " + str(b[3])

