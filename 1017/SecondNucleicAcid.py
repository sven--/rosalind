b = ""
with open("SecondNucleicAcid.input", "r") as f:
  a = f.readline()
  for x in a:
    if(x == "T"):
      b += "U"
    else:
      b += x

print b

