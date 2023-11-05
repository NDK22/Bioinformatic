def CountingDNANucleotides(input_file):
    with open(input_file,"r") as input:
        DNA = input.read()
        Count_of_A = DNA.lower().count('a')
        Count_of_C = DNA.lower().count('c')
        Count_of_G = DNA.lower().count('g')
        Count_of_T = DNA.lower().count('t')
        return Count_of_A, Count_of_C , Count_of_G, Count_of_T

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q6\rosalind_dna.txt'
counts = CountingDNANucleotides(input_file_path)
print(*counts)

