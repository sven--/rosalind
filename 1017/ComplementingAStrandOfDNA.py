b = ""
with open("ComplementingAStrandOfDNA.input", "r") as f:
  a = f.readline()
  for x in a:
    if(x == "A"):
      b = "T" + b
    if(x == "T"):
      b = "A" + b
    if(x == "G"):
      b = "C" + b
    if(x == "C"):
      b = "G" + b

print b
