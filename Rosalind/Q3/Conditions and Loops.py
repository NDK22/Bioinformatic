def sumofoddintegers(input_file):
    with open(input_file,"r") as input:
        numbers_list = input.read().split()
        numbers_list = [int(num) for num in numbers_list]
        length = numbers_list[1] -numbers_list[0]
        sum_of_odd_numbers = 0
        for i in range(length):
            number = numbers_list[0] + i
            if number % 2 == 1:
                sum_of_odd_numbers += number
    return sum_of_odd_numbers

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q3\rosalind_ini4.txt'
print(sumofoddintegers(input_file_path))