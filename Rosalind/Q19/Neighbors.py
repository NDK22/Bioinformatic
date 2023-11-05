def HammingDistance(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    if len(string2) != len(string2):
        raise ValueError("Strings of different lenghts detected")
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance

def neighbors(pattern,d):
    if d == 0:
        return pattern
    if len(pattern)==1:
        return{'A', 'C', 'G', 'T'}
    neighbourhood = set()
    suf = pattern[1:]
    suf_neighbours = neighbors(suf,d)
    for word in suf_neighbours:
        if HammingDistance(suf,word) < d:
            for base in "ACGT":
                neighbourhood.add(base + word)
        else:
            neighbourhood.add(pattern[0]+word)
    return neighbourhood

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q19\rosalind_ba1n.txt'

with open(input_file_path, 'r') as file:
    pattern = file.readline().strip()
    d = int(file.readline().strip())
result = neighbors(pattern,d)
with open('output.txt', 'w') as file:
    for neighbor in result:
        file.write(neighbor + '\n')