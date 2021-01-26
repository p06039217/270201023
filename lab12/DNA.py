class DNA:
  dna = ""
  def __init__(self,d_n_a):
    self.dna = d_n_a
  
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

  def get_dna_string(self):
    return self.dna
  
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


dna = DNA("ATGCA")
print(dna.count_nucleotides())

 

complement_dna = dna.calculate_complement()
print(complement_dna)

 

dna_1 = DNA("GAGCC")
dna_2 = DNA("CATCG")
print(dna_1.count_point_mutations(dna_2.get_dna_string()))

 

dna_3 = DNA("GATATATGCATATACTT")
dna_4 = DNA("ATAT")
print(dna_4.find_motif(dna_3.get_dna_string()))





  



    
