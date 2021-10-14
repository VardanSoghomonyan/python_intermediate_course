file = open("Experiment.txt", "r")  # r means read
for each in file:
    print(each)

file.seek(0)  # file.seek moves the cursor to the beginning of the file
print("file read is: ", file.read())
file.seek(0)  # file.seek moves the cursor to the beginning of the file
print("file read(5) is: ", file.read(5))
file.close()

file1 = open("Experiment.txt", "w")  # w means write, which deletes the file content and writes the new one
file1.write("This is new command")
file1.close()

file2 = open("Experiment.txt", "a")  # a means append, which adds the new content to the existing one
file2.write("This is new command")
file2.close()

with open(
        "Experiment.txt") as opened_file:  # when with is used it automatically closes the file in the end of the process: don't need to call close()
    print(opened_file.read())

with open("Experiment.txt", "r") as opened_file:
    data = opened_file.readlines()  # reads the file line by line
    for line in data:
        word = line.split()  # splits into words
        print(word)

file3 = open(r"C:\Users\Vardan\Documents\python_intermediate_course\classworks\cw11\Experiment.txt",
             "r+")  # the r in the front of path automatically recognises the backslashes as a path
print(file3.read())
file3.close()
