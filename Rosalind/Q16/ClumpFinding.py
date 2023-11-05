def clumpfinding(genome, k, l, t):
    clumps = set()
    kmer_count = {}
    for i in range(len(genome) - l + 1):
        split = genome[i:i+l]
        kmer_count.clear()
        for j in range(len(split) - k + 1):
            kmer = split[j:j+k]
            if kmer in kmer_count:
                kmer_count[kmer] += 1
            else:
                kmer_count[kmer] = 1
            if kmer_count[kmer] >= t:
                clumps.add(kmer)
    clumps = ' '.join(clumps)
    return clumps

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q16\rosalind_ba1e.txt'

with open(input_file_path, 'r') as file:
    genome = file.readline().strip()
    k, l, t = map(int,file.readline().strip().split())

result = clumpfinding(genome, k, l, t)   
print(result)