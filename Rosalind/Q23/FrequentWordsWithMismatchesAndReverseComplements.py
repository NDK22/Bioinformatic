from collections import defaultdict

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

def ReverseComplement(pattern):
    comple = {'A':'T','T':'A','C':'G','G':'C'}
    result = ''.join(comple[letter] for letter in reversed(pattern))
    return result


def FrequentWordsWithMismatchesAndReverseComplements(text,k,d):
    freq_pattern = set()
    pat_count = defaultdict(int)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        neighorhood = neighbors(pattern, d)
        for neighbor in neighorhood:
            pat_count[neighbor] += 1
            rc_neighbor = ReverseComplement(neighbor)
            if neighbor != rc_neighbor:
                pat_count[rc_neighbor] += 1
    max_count = max(pat_count.values())
    freq_pattern = {pattern for pattern, count in pat_count.items() if count == max_count}
    result = " ".join(freq_pattern)
    return result

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q23\rosalind_ba1j.txt'

with open(input_file_path, 'r') as file:
    text = file.readline().strip()
    k, d = map(int,file.readline().strip().split())

result = FrequentWordsWithMismatchesAndReverseComplements(text,k,d) 
print(result)