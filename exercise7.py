# Get the file extension specified by the user

file_name = input("Enter the file name: ")
separate_file = file_name.split(".")
print("The file extension is: {}".format(separate_file[len(separate_file) - 1]))