def read_pairs(file_path):
    """
    Read pairs from a file and return a dictionary where keys are proteins and values are sets of interacting proteins.
    """
    pairs_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            protein1, protein2 = fields[0], fields[1]
            
            # If protein1 is not in the dictionary, add it with an empty set
            pairs_dict.setdefault(protein1, set())
            
            # Add protein2 to the set of interacting proteins for protein1
            pairs_dict[protein1].add(protein2)
    
    return pairs_dict

def find_reciprocal_best_hits(query_dict, subject_dict):
    """
    Find reciprocal best hits between two sets of proteins.
    """
    rbbh_pairs = set()

    for query, subjects in query_dict.items():
        for subject in subjects:
            if subject in subject_dict and query in subject_dict[subject]:
                rbbh_pairs.add((query, subject))

    return rbbh_pairs

def find_3way_orthologs(file1_dict, file2_dict, file3_dict):
    # Find 2-way RBBH between file1 and file2
    rbbh_2way_1_2 = find_reciprocal_best_hits(file1_dict, file2_dict)

    # Find 2-way RBBH between file2 and file3
    rbbh_2way_2_3 = find_reciprocal_best_hits(file2_dict, file3_dict)

    # Find 2-way RBBH between file3 and file1
    rbbh_2way_3_1 = find_reciprocal_best_hits(file3_dict, file1_dict)

    # Compute 3-way orthologs
    three_way_orthologs = set()
    for pair_1_2 in rbbh_2way_1_2:
        for pair_2_3 in rbbh_2way_2_3:
            for pair_3_1 in rbbh_2way_3_1:
                if pair_1_2[1] == pair_2_3[0] and pair_2_3[1] == pair_3_1[0] and pair_3_1[1] == pair_1_2[0]:
                    three_way_orthologs.add((pair_1_2[0], pair_1_2[1], pair_2_3[1]))

    return three_way_orthologs

# Replace these paths with your actual file paths
file1_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\RBH-list-outfile_Agla_Tcas.txt'
file2_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\RBH-list-outfile_Tcas_Ldec.txt'
file3_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\RBH-list-outfile_Ldec_Agla.txt'

file1_dict = read_pairs(file1_path)
file2_dict = read_pairs(file2_path)
file3_dict = read_pairs(file3_path)

# Find 3-way orthologs
three_way_orthologs = find_3way_orthologs(file1_dict, file2_dict, file3_dict)

# Print the 3-way orthologs
for ortholog in three_way_orthologs:
    print('\t'.join(ortholog))