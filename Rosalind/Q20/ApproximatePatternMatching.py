def HammingDistance(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    if len(string1) != len(string2):
        raise ValueError("Strings of different lenghts detected")
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_distance += 1
    return hamming_distance

def ApproximatePatternMatching(pattern, text, d):
    pos =[]
    for i in range(len(text)-len(pattern)+1):
        string = text[i:i+len(pattern)]
        if HammingDistance(pattern,string) <= d:
            pos.append(i)
    result = " ".join(map(str, pos))
    return result

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q20\rosalind_ba1h.txt'

with open(input_file_path, 'r') as file:
    pattern = file.readline().strip()
    text = file.readline().strip()
    d = int(file.readline().strip())

result = ApproximatePatternMatching(pattern, text, d) 
print(result)
