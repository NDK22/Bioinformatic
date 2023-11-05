def extracting_even_lines(input_file, output_file):
    with open(input_file,"r") as input:
        even_lines=[]
        line_number = 0
        for line in input:
            line_number += 1
            if line_number % 2 == 0:
                even_lines.append(line)

    with open(output_file,"w") as output:
        for line in even_lines:
            output.write(line)

input_file_path = r"D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q 4\rosalind_ini5.txt"
output_file_path = r"D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q 4\output.txt"
extracting_even_lines(input_file_path,output_file_path)