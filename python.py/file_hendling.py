# As  we are going to learn about the file handling in python language.

# Diffrent file modes
# r - read
# w - write
# a - append
# r+ - read and write
# a+ append and read
# rb - read binary
# wb - write binary
# ab - append binary


file = open("python.py/data.txt", "r+")
data = file.readlines()
a = file.write('Honey singh munariya is going to be a super rich man in his life.\n')
print(data)
file.close()
