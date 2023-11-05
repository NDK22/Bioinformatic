def FrequencyArray(Text, k):
    array = [0]*(4 ** k)
    base = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        index = 0
        for nucleotide in kmer:
            index = index * 4 + base[nucleotide]
        array[index] += 1
    frequency = ' '.join(map(str, array))
    return frequency

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q14\rosalind_ba1k.txt'

with open(input_file_path, 'r') as file:
    Text = file.readline().strip()
    k = int(file.readline().strip())

result = FrequencyArray(Text,k)   
print(result)