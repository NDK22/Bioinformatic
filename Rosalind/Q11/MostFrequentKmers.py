def mostfrequency(Text, k):
    kmer_count = {}
    maximum_count = 0
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
        maximum_count = max(maximum_count,kmer_count[kmer])
    mostfrequentKmer = [kmer for kmer, count in kmer_count.items() if count == maximum_count]
    frequent = ' '.join(mostfrequentKmer)
    return frequent

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q11\rosalind_ba1b.txt'

with open(input_file_path, 'r') as file:
    Text = file.readline().strip() 
    k = int(file.readline())

result = mostfrequency(Text, k)
print(result)