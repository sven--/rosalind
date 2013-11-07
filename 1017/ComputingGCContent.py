a = {}
ans = -1
def gc_content(a): 
  return 100.0 * a[0] / (a[0] + a[1])
with open("ComputingGCContent.input", "r") as f:
  current = ""
  for line in f:
    if(line[0] == ">"):
      if(current != "" and (ans == -1 or gc_content(a[ans]) < gc_content(a[current]))):
        ans = current
      current = line
      a[current] = [0, 0]
    else:
      for y in line:
        if(y == "G" or y == "C"):
          a[current][0] += 1
        elif(y == "A" or y == "T"):
          a[current][1] += 1
print ans[1:]
print gc_content(a[ans])

