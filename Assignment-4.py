# Task 1: Read a File and Handle Errors

def read_file(fil):
        try:
            with open(fil, 'r') as f:
                print("Reading the File Content: ")
                for i, line in enumerate(f, start=1):
                    print(f"Line {i} : {line.strip()}")
        except FileNotFoundError:
            print("The File not Found. Please Create one First")

read_file('sample.txt')


# Task 2: Write and Append Data to a File

with open('output.txt','w') as f: # Opening file in "WRITE" mode
    f.write(input("Enter your text here: "))
print("File content added!!")

with open('output.txt', 'a') as fil: # Opening file in "APPEND" mode
    fil.write(input("Enter your text here: "))
print("Append Successful!!")

with open('output.txt', 'r') as f: # Opening file in "READ" mode
    for line in f:
        print("file content: ", line.strip())
