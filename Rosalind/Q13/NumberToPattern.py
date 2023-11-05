def NumberToPattern(index,k):
    base = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    pattern = ""
    for i in range(k):
        remainder = index % 4
        word = base[remainder]
        pattern = word + pattern
        index =  index//4
    return pattern

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q13\rosalind_ba1m.txt'

with open(input_file_path, 'r') as file:
    index = int(file.readline().strip())
    k = int(file.readline().strip())

result = NumberToPattern(index,k)   
print(result)