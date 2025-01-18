import re


matrix = list()
for _ in range(int(input().split()[0])):
    matrix.append(list(input()))

# Rotate the matrix
matrix = list(zip(*matrix))

# Prep regex sample
sample = str()
for subset in matrix:
    for letter in subset:
        sample += letter

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))