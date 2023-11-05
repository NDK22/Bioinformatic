def stringslicing(input_file):
    with open(input_file,"r") as input:
        string_and_list = input.read().split('\n')
        string = string_and_list[0]
        numbers = string_and_list[1].split()
        numbers = [int(num) for num in numbers]
        slice1 = string[numbers[0]:numbers[1]+1]
        slice2 = string[numbers[2]:numbers[3]+1]
        sliced_string =  slice1 + ' ' + slice2
    return sliced_string

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q2\rosalind_ini3.txt'
print(stringslicing(input_file_path))