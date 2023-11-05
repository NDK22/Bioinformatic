def pythgoras(input_file):
    with open(input_file,"r") as input:
        Numbers = input.read().split()
        hypothenuse_square = 0
        for i in range(len(Numbers)):
            hypothenuse_square += int(Numbers[i])**2
    return hypothenuse_square

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q1\rosalind_ini2.txt'
print(pythgoras(input_file_path))