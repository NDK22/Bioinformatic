def blast(file_path):
    results = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue 
            fields = line.strip().split('\t')
            query, subject = fields[:2] 
            if query not in results:
                results[query] = set()
            results[query].add(subject)
    return results

def find_rbbh(file1_results, file2_results):
    rbbh = []
    for query_1, subject_1 in file1_results.items():
        for subject1 in subject_1:
            if subject1 in file2_results and query_1 in file2_results[subject1]:
                rbbh.append((query_1, subject1))
    return rbbh

def write_rbbh(rbbh, output):
    with open(output, 'w') as outfl:
        for pair in rbbh:
            outfl.write(f"{pair[0]}\t{pair[1]}\n")

file1 = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Agla_query_v_Tcas_subject.txt'
file2 = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Tcas_query_v_Agla_subject.txt'
output = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\2W-RBBH-list-outfile_Agla_Tcas.txt'
file1_results = blast(file1)
file2_results = blast(file2)
rbbh = find_rbbh(file1_results, file2_results)
write_rbbh(rbbh, output)