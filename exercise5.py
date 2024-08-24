# Get the reverse representation of a string

str1 = "Marcelo"
for i in range(len(str1) - 1, -1, -1):
    print(str1[i], end="")

print(str1[::-1])
