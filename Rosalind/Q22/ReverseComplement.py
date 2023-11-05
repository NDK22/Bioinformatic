def ReverseComplement(pattern):
    comple = {'A':'T','T':'A','C':'G','G':'C'}
    result = ''.join(comple[letter] for letter in reversed(pattern))
    return result

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q22\rosalind_ba1c.txt'

with open(input_file_path, 'r') as file:
    pattern = file.readline().strip()

result = ReverseComplement(pattern)
print(result)