def rna_to_protein(input_file):
    rna_codon_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop", "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    with open(input_file,"r") as input:
        RNA = input.read()
        protein=""
        i = 0
        while i < len(RNA):
            codon_value = RNA[i:i+3]
            if codon_value in rna_codon_table:
                amino_acid = rna_codon_table[codon_value]
                if amino_acid == "Stop":
                    break
                protein += amino_acid
                i += 3
            else:
                i += 3
    return protein

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q8\rosalind_prot.txt'
print(rna_to_protein(input_file_path))