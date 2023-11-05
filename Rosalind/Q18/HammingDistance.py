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

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q18\rosalind_ba1g.txt'

with open(input_file_path, 'r') as file:
    string1 = file.readline().strip()
    string2 = file.readline().strip()

result = HammingDistance(string1, string2)   
print(result)