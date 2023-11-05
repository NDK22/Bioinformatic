def PatternToNumber(pattern):
    base = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    pattern = pattern.upper()
    value = 0
    for i in range(len(pattern)):
        each_dna_pattern = pattern[i]
        value += base[each_dna_pattern]*(4**(len(pattern)-i-1))
    return value

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q12\rosalind_ba1l.txt'

with open(input_file_path, 'r') as file:
    pat = file.readline().strip()

result = PatternToNumber(pat)   
print(result)