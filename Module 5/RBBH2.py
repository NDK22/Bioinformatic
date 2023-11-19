def read_blast_file(file_path):
    blast_hits = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.split()
                blast_hits[parts[0]] = parts[1]
    return blast_hits

def find_rbbh(blast_hits_1, blast_hits_2):
    return {query: hit for query, hit in blast_hits_1.items() if blast_hits_2.get(hit) == query}

def write_rbbh_to_file(rbbh, output_file_path):
    with open(output_file_path, 'w') as file:
        for query, hit in rbbh.items():
            file.write(f"{query}\t{hit}\n")

file_path_1 = 'Agla_query_v_Tdas_subject.txt'
file_path_2 = 'Tdas_query_v_Agla_subject.txt'
output_file_path = '2rbbh_results.txt'

blast_hits_1 = read_blast_file(file_path_1)
blast_hits_2 = read_blast_file(file_path_2)
rbbh = find_rbbh(blast_hits_1, blast_hits_2)

write_rbbh_to_file(rbbh, output_file_path)

print(f"RBBH results have been written to {output_file_path}")
