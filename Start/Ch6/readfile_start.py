#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
# sample_file = open("textfile.txt", "r")
# if sample_file.mode == 'r':
#   # use the read() function to read the entire file
#   content = sample_file.read()
#   print(content)


sample_file = open("textfile.txt", "r")
if sample_file.mode == 'r':
  lines = sample_file.readlines()
  for l in lines:
    print(l)
