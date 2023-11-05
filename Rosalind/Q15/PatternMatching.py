def PatternMatching(pattern, genome):
    matching = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)]==pattern:
            matching.append(i)
    result = " ".join(map(str, matching))
    return result

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q15\rosalind_ba1d.txt'

with open(input_file_path, 'r') as file:
    pat = file.readline().strip()
    gen = file.readline().strip()

result = PatternMatching(pat, gen)   
print(result)