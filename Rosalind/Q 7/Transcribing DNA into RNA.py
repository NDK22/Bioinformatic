def Transcribing_DNA_into_RNA(input_file):
    with open(input_file,"r") as input:
        DNA = input.read()
        RNA = ''
        for letter in DNA:
            if letter.lower() != 't':
                RNA += letter
            else:
                RNA += 'U'
    return RNA

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q 7\rosalind_rna.txt'
print(Transcribing_DNA_into_RNA(input_file_path))