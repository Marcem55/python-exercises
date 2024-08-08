# Get the reverse representation of a string

str = "Marcelo"
for i in range(len(str) - 1, -1, -1):
    print(str[i], end="")

print()

print(str[::-1])
