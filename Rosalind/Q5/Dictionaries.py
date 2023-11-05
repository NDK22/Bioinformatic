def word_count(input_file):
    with open(input_file,"r") as input:
        words = input.read().split()
        word_count_base_dict = {}
        for word in words:
            if word not in word_count_base_dict:
                word_count_base_dict[word] = 1
            else:
                word_count_base_dict[word] += 1
    return word_count_base_dict

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q5\rosalin.txt'
for key, value in word_count(input_file_path).items():
    print(f"{key} {value}")