a = {}
with open("MonoisotopicTable") as f:
  for lines in f:
    l = lines.strip().split()
    a[l[0]] = l[1]
ans = 0.0
with open("CalculatingProteinMass.input") as f:
  for x in f.read().strip():
    ans += float(a[x])
print ans
