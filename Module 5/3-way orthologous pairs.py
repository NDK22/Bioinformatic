def blast(file):
    results = {}
    with open(file, 'r') as data:
        for entry in data:
            if not entry.startswith('#'):
                columns = entry.strip().split('\t')
                if len(columns) >= 2:
                    results[columns[0]] = columns[1]
    return results

def way3(s1_s2, s2_s3, s3_s1):
    hits = []
    for p1, p2 in s1_s2.items():
        p3 = s2_s3.get(p2)
        if p3 and s3_s1.get(p3) == p1:
            hits.append((p1, p2, p3))
    return hits

def write_rbbh(results, output_path):
    with open(output_path, 'w') as f:
        for result in results:
            f.write('\t'.join(result) + '\n')

file_path1 = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Agla_query_v_Tcas_subject.txt'
file_path2 = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Tcas_query_v_Ldec_subject.txt'
file_path3 = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Ldec_query_v_Agla_subject.txt'
output_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\3W-RBBH-list-outfile_Agla_Tcas_Ldec.txt'
agla_tcas = blast(file_path1)
tcas_ldec = blast(file_path2)
ldec_agla = blast(file_path3)
results = way3(agla_tcas, tcas_ldec, ldec_agla)
write_rbbh(results, output_path)