# Pronađi dna osobe iz datoteke dna.txt
kosa = {"Crna" : "CCAGCAATCGC", "smeđa" : "GCCAGTGCCG", "plava" : "TTAGCTATCGC"}
lice = {"Kockasto" : "GCCACGG", "okrugla" : "ACCACAA", "ovalna" : "AGGCCTCA"}
oci = {"Plave" : "TTGTGGTGGC", "zelene" : "GGGAGGTGGC", "smeđe" : "AAGTAGTGAC"}
spol = {"Ženski" : "TGAAGGACCTTC", "muško" : "TGCAGGAACTTC"}
rasa = {"Bijela" : "AAAACCTCA", "crna" : "CGACTACAG", "azijska" : "CGCGGGCCG"}

osobe = {"eva": ["ženski", "bijela", "plava", "plave", "ovalna"],
          "larisa": ["ženski", "bijela", "smeđa", "smeđe", "ovalna"],
          "matej": ["muško", "bijela", "crna", "plava", "ovalna"],
          "miha": ["muško", "bijela", "smeđa", "zelene", "kockasto"]}



with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

osoba = []

for a in spol:
    if spol[a] in dna:
        print(str("spol: ") + (a))
        osoba.append(a)
for a in rasa:
    if rasa[a] in dna:
        print(str("rasa: ") + (a))
        osoba.append(a)
for a in kosa:
    if kosa[a] in dna:
        print(str("kosa: ") + (a))
        osoba.append(a)
for a in oci:
    if oci[a] in dna:
        print(str("oči: ") + (a))
        osoba.append(a)
for a in lice:
    if lice[a] in dna:
        print(str("lice: ") + (a))
        osoba.append(a)

for p in osobe:
    if osobe[p] == osoba:
        print("Osoba koju tražimo je %s" % p.upper())
        break