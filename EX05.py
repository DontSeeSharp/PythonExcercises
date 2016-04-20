"""
Read animal name in latin and its corresponding 
protein sequence and tell how many times the sequence 
appears in DNA sequence (DNA gets translated to protein sequence)

Input:
filename - csv file, that contains values corresponding to organism, it's latin name and protein.
EX05_DNA - txt file, that contains a DNA sequence

Output:
A dictionary, that contains species latin name and the number of times species protein
appears in DNA.
"""
__author__ = 'Hendrig Sellik'
import csv                 #Used in read_latin_and_protein_from_csv(classification_file)

def read_dna_data_from_file(filename):
    """
    Read and return dna sequence from txt file

    Input:
    filename - (string) name of the text file

    Output:
    (string) DNA sequence from the file
    """
    with open(filename) as file:
        dna_failist = file.read().replace("\n","")
    
    if dna_failist == "":
        return None
    else:
        return dna_failist

def transcribe_dna_to_rna(dna):
    """
    Transcribe dna sequence to rna sequence

    Input:
    dna - a DNA sequence

    Output:
    rna sequence
    """
    rna = ""
    for i in dna:
        if i == 'C':
            rna += 'G'

        elif i == 'G':
            rna += 'C'

        elif i == 'T':
            rna += 'A'

        elif i == 'A':
            rna += 'U'

        else:
            return None

    if len(rna) == 0:
        return None
    else:
        return rna

def translate_rna_to_protein(rna):
    """
    Translate RNA sequence to protein sequence

    Input:
    rna - (string) RNA sequence

    Output:
    (string) protein sequence
    """

    if rna == None or rna == "":
        return None

    codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
        "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"Met",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    proteins = ""

    try:
        for i in range(len(rna) // 3 + 1):
            if i != 0:
                proteins += codons[rna[(i * 3) - 3 : i * 3]]
    except KeyError:
        return None

    return proteins

def read_latin_and_protein_from_csv(classification_file):
    """
    Read latin names of the species and their 

    Input:
    rna - (string) RNA sequence

    Output:
    (string) protein sequence
    """
    with open(classification_file) as csvfile:
        reader = csv.DictReader(csvfile)

        list_of_organisms = []
        list_of_proteins = []

        for row in reader:
            if row["Valk"] not in list_of_proteins:
                list_of_organisms.append(row["Ladinakeelne"])
                list_of_proteins.append(row["Valk"])

    return list_of_organisms, list_of_proteins

def determine_species(classification_file):
    """
    Read animal name in latin and its corresponding 
    protein sequence and tell how many times the sequence 
    appears in DNA sequence (DNA gets translated to protein sequence)

    Input:
    filename - csv file, that contains values corresponding to organism, it's latin name and protein.
    EX05_DNA - txt file, that contains a DNA sequence

    Output:
    A dictionary, that contains species latin name and the number of times species protein
    appears in DNA.
    """
    dna = read_dna_data_from_file("EX05_DNA.txt")
    rna = transcribe_dna_to_rna(dna)
    proteins = translate_rna_to_protein(rna)

    if proteins == None:
        return None

    #Create two lists with same length, latin_list[i] 
    #is the latin name and protein_list[i] has it's corresponding protein  
    a = read_latin_and_protein_from_csv(classification_file)
    latin_list = a[0]
    protein_list = a[1]

    #Create a dictionary and enter the latin_name and the count of its corresponding proteins in the (dna->rna->)proteins sequence
    species_list = {}

    for i in range(len(latin_list)):
        species_list[latin_list[i]] = 0

    for i in range(len(latin_list)):
        species_list[latin_list[i]] = species_list[latin_list[i]] + proteins.count(protein_list[i])    

    #Create a new latin list with duplicates removed
    new_latin_list = []

    for i in latin_list:
        if i not in new_latin_list:
            new_latin_list.append(i)

    #Create a dictionary where values with 0 are removed
    for i in range(len(species_list)):
        if species_list[new_latin_list[i]] == 0:
            del species_list[new_latin_list[i]]

    return species_list
