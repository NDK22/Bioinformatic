def patternCount(Text, pattern):
    count = 0
    text_length = len(Text)
    pattern_length = len(pattern)
    for i in range(text_length-pattern_length+1):
        if Text[i:i+pattern_length] == pattern:
            count += 1
    return count

input_file_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Rosalind\Q10\rosalind_ba1a.txt'

with open(input_file_path, 'r') as file:
    Text = file.readline().strip() 
    Pattern = file.readline().strip()

result = patternCount(Text, Pattern)
print(result)