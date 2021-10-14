file = open("Experiment.txt", "w+")
List = ["This is Dehli\n", "This is Paris\n", "This is Yerevan\n"]
file.write("Hello\n")
file.writelines(List)

print("Output of read function is:\n")
print(file.read())
file.seek(0)

print("Output of readlines function is:\n")
print(file.readlines())
file.seek(0)

print("Output of read(9) function is:\n")
print(file.read(9))
file.seek(0)

print("Output of readline(9) function is:\n")
print(file.readline(9))
file.seek(0)

print("Output of readlines function is:\n")
print(file.readlines())

file.close()
