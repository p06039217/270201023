class DNA:
  def __init__(self,dna):
    self.dna = dna
  
  def count_nucleotides(self):
    nucleotide_dict = dict()
    A = 0
    G = 0
    T = 0
    C = 0
  
    for i in self.dna:
      if i == "A":
        A += 1
      elif i == "G":
        G += 1
      elif i == "T":
        T += 1 
      elif i == "C":
        C += 1

    nucleotide_dict["A"] = A
    nucleotide_dict["G"] = G
    nucleotide_dict["T"] = T
    nucleotide_dict["C"] = C
    return nucleotide_dict
  def calculate_complement(self):
    dna_comp = ""
    for i in self.dna:
      if i == "A":
        dna_comp += "T"
      elif i == "G":
        dna_comp += "C"
      elif i == "T":
        dna_comp += "A"
      elif i == "C":
        dna_comp += "G"

    return dna_comp

  def count_point_mutations(self,dna):
    hamming_distance = 0
    for i in range(len(dna)):
      if self.dna[i] != dna[i]:
        hamming_distance += 1
    return hamming_distance

  def find_motif(self,dna):
    locations = []
    for i in range(len(dna)):
      if self.dna == dna[i:i+len(self.dna)]:
        locations += [i]

    return locations


dna1 = DNA("ATAT")

print(dna1.find_motif("GATATATGCATATACTT"))





  



    
