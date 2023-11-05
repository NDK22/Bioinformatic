def GC_Content(DNA):
    length_of_DNA = len(DNA)
    count = 0
    for letter in DNA:
        if letter.lower() == 'c' or letter.lower() == 'g':
            count += 1
    GC = (count/length_of_DNA)*100
    return GC

def Compute_GC_Content(input_file):
    with open(input_file,"r") as input:
        Each_DNA_Name_Strings = input.read().split('\n')
        GC_Content_Dict={}
        Sequence_name=''
        DNA_sequence= ''
        for line in Each_DNA_Name_Strings:
            if line.startswith('>'):
                if Sequence_name:
                    GC_Content_Dict[Sequence_name] = GC_Content(DNA_sequence)
                Sequence_name=line[1:]
                DNA_sequence=''
            else:
                DNA_sequence += line
                print(DNA_sequence)
        if Sequence_name:
            GC_Content_Dict[Sequence_name] = GC_Content(DNA_sequence)
        print(GC_Content_Dict)
        FASTA_Format = max(GC_Content_Dict, key=GC_Content_Dict.get)
        GC_Content_value = GC_Content_Dict[FASTA_Format]
    return FASTA_Format,GC_Content_value

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q 9\input.txt'
Compute_GC_Content(input_file_path)
# print(Compute_GC_Content(input_file_path)[0])
# print(Compute_GC_Content(input_file_path)[1])
