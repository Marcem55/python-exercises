# Request a number to the user and calculate n + nn + nnn

# n = 3 => 3 + 33 + 333 = 369

n = input("Enter a number: ")
# nn = f"{n}{n}"
# nnn = f"{n}{n}{n}"
# intn = int(n)
# intnn = int(nn)
# intnnn = int(nnn)
# print(intn + intnn + intnnn)

n = int(n)
nn = int("{}{}".format(n, n))
nnn = int("%s%s%s" % (n, n, n))

print(n + nn + nnn)

