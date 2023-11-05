def MinimumSkew(genome):
    genome = genome.upper()
    skews_pos = []
    skews= []
    skew = 0
    min_skew = float('inf')
    for i in range (len(genome)):
        if genome[i] == 'C':
            skew -= 1
        elif genome[i] == 'G':
            skew += 1
        skews_pos.append(skew)
    min_skew = min(skews_pos)
    skews = [i+1 for i, val in enumerate(skews_pos) if val == min_skew]
    skews = ' '.join(map(str,skews))
    return skews

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q17\rosalind_ba1f (4).txt'

with open(input_file_path, 'r') as file:
    genome = file.readline().strip()

result = MinimumSkew(genome)   
print(result)