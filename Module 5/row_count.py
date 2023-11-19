import csv

def count_rows(csv_file_path):
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)
        
        # Use len to count the remaining rows
        row_count = len(list(csv_reader))
    
    return row_count

# Replace 'your_file.csv' with the actual file path
file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\2W-RBBH-list-outfile_Agla_Tcas.txt'
rows = count_rows(file_path)

print(f'Number of rows: {rows}')
