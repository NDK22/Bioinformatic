def count_proteins(file_path):
    """
    Count the number of proteins in a FASTA file.
    """
    protein_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Check for the start of a new sequence
            if line.startswith('>'):
                protein_count += 1
    return protein_count

# Replace 'your_file.faa' with the actual file path
file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Ldec2.0_prot.faa'
protein_count = count_proteins(file_path)

print(f'Number of proteins: {protein_count}')
