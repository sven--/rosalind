import urllib
with open("FindingAProteinMotif.input", "r") as f:
  for l in f:
    fh = urllib.urlopen("http://www.uniprot.org/uniprot/%s.fasta\n" % l.strip())
    fh.readline()
    a = "".join([i.strip() for i in fh.read().split('\n')])
    fh.close()
    b = []
    for i in range(0, len(a)-3):
      if a[i] is 'N' and not a[i+1] is 'P' and (a[i+2] is 'S' or a[i+2] is 'T') and not a[i+3] is 'P':
        b.append(i+1)
    if not len(b) is 0:
      print l.strip()
      for i in range(0, len(b)):
        print b[i],
      print
